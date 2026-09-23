"""Generate the GitHub profile banner (light + dark) as self-contained SVGs.

Text is converted to outlines (shaped with HarfBuzz, drawn with fontTools) so it
renders identically on GitHub, which shows README SVGs as images and never loads
web fonts. Colours are the portfolio's tokens (see portfolio DESIGN.md).

Regenerate:
    npm i --prefix /tmp/fonts @fontsource/inter @fontsource/jetbrains-mono
    pip install fonttools uharfbuzz
    FONTSOURCE=/tmp/fonts/node_modules/@fontsource python scripts/make_banner.py

It also writes assets/linkedin-banner.svg (1584x396, dark only: LinkedIn has no theme
switch). LinkedIn needs a PNG, so screenshot that SVG at 1584x396 in a browser. The
left third stays empty because the profile photo covers it.
"""
import io
import os
import pathlib

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONTS = pathlib.Path(os.environ["FONTSOURCE"])
INTER = str(FONTS / "inter/files/inter-latin-{w}-normal.woff")
MONO = str(FONTS / "jetbrains-mono/files/jetbrains-mono-latin-{w}-normal.woff")

THEMES = {
    "dark": dict(bg="#08090a", grid="#ffffff", grid_op=0.05, fg="#f7f8f8", fg2="#b6bac1", muted="#8a8f98",
                 line="#2f3137", surface="#141518", accent="#9296fb"),
    "light": dict(bg="#fafafa", grid="#000000", grid_op=0.055, fg="#171717", fg2="#404047", muted="#6b6b70",
                  line="#d6d6d8", surface="#ffffff", accent="#4f46e5"),
}

W, H = 1280, 320


class Face:
    def __init__(self, path: str):
        data = pathlib.Path(path).read_bytes()
        self.tt = TTFont(io.BytesIO(data))
        # HarfBuzz needs the raw sfnt; fontTools decompresses WOFF for us.
        buf = io.BytesIO()
        self.tt.flavor = None
        self.tt.save(buf)
        self.hb_font = hb.Font(hb.Face(buf.getvalue()))
        self.upem = self.tt["head"].unitsPerEm
        self.glyphs = self.tt.getGlyphSet()
        self.order = self.tt.getGlyphOrder()

    def path(self, text: str, x: float, y: float, size: float, tracking_em: float = 0.0) -> tuple[str, float]:
        """SVG path data for `text` with its baseline at (x, y); returns (d, advance width)."""
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.hb_font, buf, {"kern": True, "liga": False, "calt": False})
        scale = size / self.upem
        pen = SVGPathPen(self.glyphs)
        cursor = 0.0
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            name = self.order[info.codepoint]
            gx = x + (cursor + pos.x_offset) * scale
            gy = y - pos.y_offset * scale
            self.glyphs[name].draw(TransformPen(pen, (scale, 0, 0, -scale, gx, gy)))
            cursor += pos.x_advance + tracking_em * self.upem
        return pen.getCommands(), (cursor - tracking_em * self.upem) * scale


def grid(w: int, h: int) -> str:
    return "".join(f'<path d="M{gx} 0 V{h}"/>' for gx in range(0, w + 1, 56)) + \
           "".join(f'<path d="M0 {gy} H{w}"/>' for gy in range(0, h + 1, 56))


def diagram(t: dict, mono: Face, nx: int, ny: int) -> str:
    """Diagram motif from the portfolio's work thumbnails: nodes, hairlines, one indigo hot path."""
    nodes = [  # (x, y, w, label, strong)
        (nx, ny, 150, "request", False),
        (nx + 190, ny + 66, 150, "lock rows", True),
        (nx + 30, ny + 132, 150, "write both", False),
        (nx + 220, ny + 132, 120, "commit", True),
    ]
    node_svg = []
    for bx, by, bw, label, strong in nodes:
        d, adv = mono.path(label, 0, 0, 15)
        tx = bx + (bw - adv) / 2
        d, _ = mono.path(label, tx, by + 24, 15)
        node_svg.append(
            f'<rect x="{bx}" y="{by}" width="{bw}" height="36" rx="6" fill="{t["surface"]}" '
            f'stroke="{t["muted"] if strong else t["line"]}" stroke-width="1"/>'
            f'<path d="{d}" fill="{t["fg2"] if strong else t["muted"]}"/>'
        )
    # request -> lock rows -> write both -> commit, in reading order.
    hot = (f"M{nx + 75} {ny + 36} V{ny + 84} H{nx + 190} "
           f"M{nx + 265} {ny + 102} V{ny + 117} H{nx + 105} V{ny + 132} "
           f"M{nx + 180} {ny + 150} H{nx + 220}")
    hairline = f"M{nx - 40} {ny + 18} H{nx}  M{nx + 340} {ny + 150} H{nx + 380}"
    return f'''<path d="{hairline}" stroke="{t["line"]}" stroke-width="1" stroke-dasharray="3 4" fill="none"/>
    <path d="{hot}" stroke="{t["accent"]}" stroke-width="1.75" fill="none"/>
    {"".join(node_svg)}
    <circle cx="{nx + 190}" cy="{ny + 84}" r="3" fill="{t["accent"]}"/>
    <circle cx="{nx + 105}" cy="{ny + 132}" r="3" fill="{t["accent"]}"/>
    <circle cx="{nx + 220}" cy="{ny + 150}" r="3" fill="{t["accent"]}"/>'''


FADE = '''<linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff" stop-opacity="1"/>
      <stop offset="0.55" stop-color="#fff" stop-opacity="0.55"/>
      <stop offset="1" stop-color="#fff" stop-opacity="0.15"/>
    </linearGradient>'''


def banner(t: dict) -> str:
    inter600 = Face(INTER.format(w=600))
    mono400 = Face(MONO.format(w=400))

    x0 = 72
    name_d, _ = inter600.path("Gabryel Verissimo", x0, 132, 68, -0.038)
    role_d, _ = inter600.path("Software Engineer", x0, 206, 68, -0.038)
    tag_d, _ = mono400.path("Reliable systems for fintech  ·  Python · Java · TypeScript", x0, 262, 19)

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Gabryel Verissimo, Software Engineer. Reliable systems for fintech in Python, Java and TypeScript.">
  <defs>
    {FADE}
    <mask id="gridmask"><rect width="{W}" height="{H}" fill="url(#fade)"/></mask>
    <clipPath id="round"><rect width="{W}" height="{H}" rx="14"/></clipPath>
  </defs>
  <g clip-path="url(#round)">
    <rect width="{W}" height="{H}" fill="{t["bg"]}"/>
    <g stroke="{t["grid"]}" stroke-opacity="{t["grid_op"]}" stroke-width="1" mask="url(#gridmask)">{grid(W, H)}</g>
    <path d="{name_d}" fill="{t["fg"]}"/>
    <path d="{role_d}" fill="{t["muted"]}"/>
    <path d="{tag_d}" fill="{t["fg2"]}"/>
    {diagram(t, mono400, 872, 70)}
  </g>
  <rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="none" stroke="{t["line"]}"/>
</svg>
'''


LW, LH = 1584, 396
LINKEDIN_SAFE_X = 470  # the profile photo sits over the bottom-left of the banner


def linkedin_banner(t: dict) -> str:
    inter600 = Face(INTER.format(w=600))
    mono400 = Face(MONO.format(w=400))

    x0 = LINKEDIN_SAFE_X
    head_d, head_w = inter600.path("Reliable systems for fintech", x0, 176, 46, -0.03)
    stack_d, _ = mono400.path("Python · Java · TypeScript", x0, 232, 22)
    site_d, _ = mono400.path("gabryelverissimo.dev", x0, 282, 22)
    nx, ny = 1170, 112
    assert x0 + head_w < nx - 60, f"headline ({x0 + head_w:.0f}px) runs into the diagram"

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {LW} {LH}" width="{LW}" height="{LH}">
  <defs>
    {FADE}
    <mask id="gridmask"><rect width="{LW}" height="{LH}" fill="url(#fade)"/></mask>
  </defs>
  <rect width="{LW}" height="{LH}" fill="{t["bg"]}"/>
  <g stroke="{t["grid"]}" stroke-opacity="{t["grid_op"]}" stroke-width="1" mask="url(#gridmask)">{grid(LW, LH)}</g>
  <path d="{head_d}" fill="{t["fg"]}"/>
  <path d="{stack_d}" fill="{t["fg2"]}"/>
  <path d="{site_d}" fill="{t["accent"]}"/>
  <g>
    {diagram(t, mono400, nx, ny)}
  </g>
</svg>
'''


if __name__ == "__main__":
    out = pathlib.Path(__file__).resolve().parent.parent / "assets"
    out.mkdir(exist_ok=True)
    for name, theme in THEMES.items():
        svg = banner(theme)
        (out / f"banner-{name}.svg").write_text(svg)
        print(name, len(svg) // 1024, "KB")
    (out / "linkedin-banner.svg").write_text(linkedin_banner(THEMES["dark"]))
    print("linkedin-banner.svg written")
