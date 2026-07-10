#!/usr/bin/env python3
"""Isometric SVG render of GM650 6-panel array from real design geometry (mm)."""
import math

S = 0.148           # px per mm
OX, OY = 40, 385
COS30, SIN30 = math.cos(math.pi/6), 0.5
SLOPE = 425/2380    # 10 deg-ish, matches drawings

def proj(x, y, z):
    u, v = x, -y
    sx = (u - v) * COS30
    sy = (u + v) * SIN30 - z
    return OX + S*sx, OY + S*sy

# light from north-west-high
L = (-0.4, -0.5, 0.85)
Ln = math.sqrt(sum(c*c for c in L)); L = tuple(c/Ln for c in L)

def shade(base, n):
    d = max(0.0, n[0]*L[0] + n[1]*L[1] + n[2]*L[2])
    b = 0.52 + 0.48*d
    return '#%02x%02x%02x' % tuple(min(255, int(c*b)) for c in base)

def ccw(pts):
    a = sum((pts[i][0]*pts[(i+1) % len(pts)][1] - pts[(i+1) % len(pts)][0]*pts[i][1])
            for i in range(len(pts)))
    return pts if a > 0 else pts[::-1]

out = []
def poly(pts2, fill, stroke='none', sw=0, opacity=1.0, extra=''):
    p = ' '.join(f'{a:.1f},{b:.1f}' for a, b in pts2)
    o = f' opacity="{opacity}"' if opacity < 1 else ''
    st = f' stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"' if stroke != 'none' else ''
    out.append(f'<polygon points="{p}" fill="{fill}"{st}{o} {extra}/>')

def prism(x0, x1, yz, base):
    """Prism: CCW polygon in (y,z), extruded x0..x1. Draws visible faces, far->near."""
    yz = ccw(list(yz))
    n = len(yz)
    faces = []
    for i in range(n):
        (y1, z1), (y2, z2) = yz[i], yz[(i+1) % n]
        dy, dz = y2-y1, z2-z1
        ln = math.hypot(dy, dz)
        if ln < 1e-9: continue
        ny, nz = dz/ln, -dy/ln          # outward for CCW
        if -ny + nz > 0:                # visible to viewer at (+x,-y,+z)
            quad3 = [(x0,y1,z1),(x1,y1,z1),(x1,y2,z2),(x0,y2,z2)]
            depth = sum(px-py+pz for px,py,pz in quad3)/4
            faces.append((depth, quad3, (0.0, ny, nz)))
    # +x cap
    cap = [(x1, y, z) for y, z in yz]
    faces.append((sum(px-py+pz for px,py,pz in cap)/len(cap), cap, (1.0, 0.0, 0.0)))
    for depth, q, nrm in sorted(faces):
        poly([proj(*p) for p in q], shade(base, nrm))

# ---------------- scene ----------------
W, H = 1420, 980
out.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
out.append('<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">'
           '<stop offset="0" stop-color="#e8f1f7"/><stop offset="1" stop-color="#fdfdfb"/></linearGradient>'
           '<linearGradient id="gnd" x1="0" y1="0" x2="0" y2="1">'
           '<stop offset="0" stop-color="#e3ead6"/><stop offset="1" stop-color="#d3ddc4"/></linearGradient></defs>')
out.append(f'<rect width="{W}" height="{H}" fill="url(#sky)"/>')

# ground
g = [proj(-1200, -700, 0), proj(8900, -700, 0), proj(8900, 3400, 0), proj(-1200, 3400, 0)]
poly(g, 'url(#gnd)')

# soft shadow of tilted array (light offset ~ (0.47z, 0.59z))
def sh(x, y, z): return proj(x + 0.47*z, y + 0.59*z, 0)
poly([sh(0,1,755), sh(6909,1,755), sh(6909,2429,1189), sh(0,2429,1189)], '#31404d', opacity=0.13)

ALU  = (206, 211, 218)
RAIL = (188, 194, 202)
CONC = (183, 177, 166)
GLASS= (24, 52, 98)
DARK = (70, 76, 84)

TRE_X = [25, 1144.5, 2299.5, 3454.5, 4609.5, 5764.5, 6884]

# footings (draw far to near: far = small x - y)
foots = [(xt, yc) for xt in TRE_X for yc in (75, 2355)]
for xt, yc in sorted(foots, key=lambda p: p[0]-p[1]):
    prism(xt-250, xt+250, [(yc-250,0),(yc+250,0),(yc+250,150),(yc-250,150)], CONC)

def rafter_z(y): return 650 + SLOPE*(y-25)   # underside

# trestles far -> near (small x first)
for xt in TRE_X:
    x0, x1 = xt-25, xt+25
    prism(x0, x1, [(0,150),(2430,150),(2430,200),(0,200)], ALU)                    # chord
    prism(x0, x1, [(1190,200),(1240,200),(1240,rafter_z(1215)),(1190,rafter_z(1215))], ALU)  # strut
    prism(x0, x1, [(0,200),(50,200),(50,650),(0,650)], ALU)                        # front post
    prism(x0, x1, [(2380,200),(2430,200),(2430,1075),(2380,1075)], ALU)            # rear post
    prism(x0, x1, [(-40,rafter_z(-40)),(2470,rafter_z(2470)),
                   (2470,rafter_z(2470)+51),(-40,rafter_z(-40)+51)], ALU)          # rafter

# rails (y centres 492 / 1213 / 1935, sitting on rafter top) far -> near (big y first)
for yc in (1935, 1213, 492):
    zb = rafter_z(yc) + 51
    prism(-60, 6969, [(yc-25,zb),(yc+25,zb),(yc+25,zb+50),(yc-25,zb+50)], RAIL)

# panels
def panel_z(y):  return 843 + SLOPE*(y-492)      # underside plane (on rail tops)
for i in range(6):
    px0 = i*1155
    prism(px0, px0+1134, [(1,panel_z(1)),(2429,panel_z(2429)),
                          (2429,panel_z(2429)+30),(1,panel_z(1)+30)], (205,210,216))
    # glass top face with cell grid
    zt = lambda y: panel_z(y)+30
    c = [ (px0,1,zt(1)), (px0+1134,1,zt(1)), (px0+1134,2429,zt(2429)), (px0,2429,zt(2429)) ]
    q = [proj(*p) for p in c]
    poly(q, shade(GLASS, (0, -math.sin(math.radians(10)), math.cos(math.radians(10)))),
         stroke='#ccd2d8', sw=2.2)
    def lerp(a, b, t): return (a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t)
    lines = []
    for k in range(1, 6):     # 6 cell columns
        t = k/6
        lines.append((lerp(q[0], q[1], t), lerp(q[3], q[2], t)))
    for k in range(1, 12):    # 12 cell rows
        t = k/12
        lines.append((lerp(q[0], q[3], t), lerp(q[1], q[2], t)))
    seg = ''.join(f'M{a[0]:.1f},{a[1]:.1f}L{b[0]:.1f},{b[1]:.1f}' for a, b in lines)
    out.append(f'<path d="{seg}" stroke="#33507e" stroke-width="0.9" fill="none" opacity="0.85"/>')
    # sheen
    poly([lerp(q[0],q[1],0.04)+(), ], 'none') if False else None
    sh1 = [lerp(q[0], q[1], 0.05), lerp(q[0], q[1], 0.30),
           lerp(q[3], q[2], 0.18), lerp(q[3], q[2], 0.02)]
    poly(sh1, '#ffffff', opacity=0.07)

# clamps: at row ends and joints, on each rail, above panel tops
clamp_x = [(-55, 5)] + [(1155*i-45, 1155*i+24) for i in range(1, 6)] + [(6904, 6964)]
for (cx0, cx1) in clamp_x:
    for yc in (1935, 1213, 492):
        zb = rafter_z(yc) + 101           # rail top
        prism(cx0, cx1, [(yc-22,zb),(yc+22,zb),(yc+22,zb+68),(yc-22,zb+68)], DARK)

# person for scale (1.75 m) near right end
bx, by = proj(7500, 900, 0)
hpx = S*1750
out.append(f'<g fill="#6f7a86">'
           f'<circle cx="{bx:.0f}" cy="{by-hpx:.0f}" r="{S*115:.0f}"/>'
           f'<path d="M{bx-S*130:.0f},{by:.0f} L{bx-S*110:.0f},{by-hpx*0.62:.0f} '
           f'Q{bx:.0f},{by-hpx*0.80:.0f} {bx+S*110:.0f},{by-hpx*0.62:.0f} '
           f'L{bx+S*130:.0f},{by:.0f} L{bx+S*45:.0f},{by:.0f} L{bx:.0f},{by-hpx*0.35:.0f} '
           f'L{bx-S*45:.0f},{by:.0f} Z"/></g>')

# caption (top-right, clear sky)
out.append(f'<text x="{W-30}" y="52" text-anchor="end" font-family="Helvetica,Arial" font-size="30" '
           f'font-weight="bold" fill="#1a2733">GM650 CYCLONE GROUND MOUNT — 6-PANEL BUNDLE</text>')
out.append(f'<text x="{W-30}" y="80" text-anchor="end" font-family="Helvetica,Arial" font-size="17" fill="#51606d">'
           f'6 × JA Solar JAM72S42-LR 650 W · 7 trestles · 3 rail lines · 10° tilt, facing north · '
           f'row 6.9 m · 3.9 kW</text>')
out.append('</svg>')

path = '/home/user/WebsiteFactory/solar-mounting-kit/render-6-panel-array.svg'
open(path, 'w').write('\n'.join(out))
print('wrote', path)
