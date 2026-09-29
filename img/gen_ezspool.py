# Ez-Spool 이미지 생성기. 사이트 다크 토큰 색만 쓴다.
#   python3 gen_ezspool.py <out_dir>  →  ezspool.svg(상세, 1200×440) · ezspool-thumb.svg(카드, 600×840)
# 칸 실측(2026-09-29): 상세 1181×432(데스크톱)·334×220(모바일), 카드 198×277·120×159. 모두 object-fit:cover.
import math, os, sys

BG, PANEL, LINE, INSET = '#1b1b1e', '#232327', '#2f2f35', '#2a2a2f'
TEXT, BODY, MUTED = '#ecebe6', '#c4c4c8', '#9a9a9f'
RED = '#f05a5f'
MONO = "'SF Mono','Menlo','Consolas',monospace"
C, Sn = math.cos(math.radians(30)), math.sin(math.radians(30))

# ── 배관 모델(3D). 본관 엘보 7개 + 티 분기(밸브). 스풀 셋으로 나뉜다
P = [(0, 0, 3), (0, 0, 0), (3.5, 0, 0), (3.5, 0, 2.5), (3.5, -3, 2.5), (3.5, -3, 4.5),
     (6, -3, 4.5), (6, -3, 2), (6, -5, 2)]
T = (1.5, 0, 0)
BR = [T, (1.5, 2.2, 0), (1.5, 2.2, -1.5)]

def lerp(a, b, t):
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(3))

F1, F2 = lerp(T, P[2], 0.5), lerp(P[5], P[6], 0.5)
SPOOLS = [([P[0], P[1], T, F1], TEXT), ([F1, P[2], P[3], P[4], P[5], F2], RED), ([F2, P[6], P[7], P[8]], MUTED)]
DIMS = [(P[0], P[1], (-0.8, 0, 0), '3000'), (P[3], P[4], (-0.8, 0, 0), '3000')]
# 칩: (점, 글자, 방향(도, 화면 기준 0=오른쪽 90=아래), 바탕, 글자색). 선 길이는 모두 같다
CHIPS = [(P[1], 'W1', 150, INSET, TEXT), (T, 'W2', -60, INSET, TEXT), (F1, 'F3', 110, RED, '#ffffff'),
         (P[2], 'W4', 30, INSET, TEXT), (P[4], 'W5', 0, INSET, TEXT), (F2, 'F6', -60, RED, '#ffffff'),
         (P[7], 'W7', 150, INSET, TEXT),
         (lerp(P[0], P[1], 0.45), 'SP-01', 0, TEXT, BG), (lerp(P[3], P[4], 0.5), 'SP-02', 60, RED, '#ffffff'),
         (lerp(P[7], P[8], 0.5), 'SP-03', 60, MUTED, BG)]
LEAD = 38

def chip_w(label):
    return 14 + 8.6 * len(label)

class Svg:
    def __init__(self, w, h):
        self.w, self.h, self.o = w, h, []
        self.a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">')
        self.a(f'<rect width="{w}" height="{h}" fill="{BG}"/>')
        self.a(f'<g fill="{INSET}">' + ''.join(f'<circle cx="{x}" cy="{y}" r="1.1"/>'
               for x in range(12, w, 24) for y in range(12, h, 24)) + '</g>')
    def a(self, s):
        self.o.append(s)
    def text(self, x, y, s, size, col, anchor='start', fw='400', ls=None):
        l = f' letter-spacing="{ls}"' if ls else ''
        self.a(f'<text x="{x:.1f}" y="{y:.1f}" font-family="{MONO}" font-size="{size}" font-weight="{fw}" fill="{col}" text-anchor="{anchor}"{l}>{s}</text>')
    def save(self, path):
        open(path, 'w').write('\n'.join(self.o + ['</svg>']))

def iso(p, S):
    x, y, z = p
    return ((x - y) * C * S, (x + y) * Sn * S - z * S)

def extents(S):
    """도면 전체(배관·치수·칩)의 화면 상자, 원점 기준"""
    xs, ys = [], []
    def add(x, y, rx=0, ry=0):
        xs.extend([x - rx, x + rx]); ys.extend([y - ry, y + ry])
    for p in P + BR:
        add(*iso(p, S), 14, 14)
    for p0, p1, off, _ in DIMS:
        for p in (p0, p1):
            add(*iso(tuple(p[i] + off[i] for i in range(3)), S), 0, 16)
    for p, lab, ang, *_ in CHIPS:
        x, y = iso(p, S)
        c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        add(x + LEAD * c + c * chip_w(lab) / 2, y + LEAD * s + s * 12, chip_w(lab) / 2, 12)
    return min(xs), min(ys), max(xs), max(ys)

def fit(box):
    """box(x0,y0,x1,y1) 안에 가장 크게 들어가는 S와 원점"""
    x0, y0, x1, y1 = box
    S = 10
    while True:
        e = extents(S + 0.5)
        if e[2] - e[0] > x1 - x0 or e[3] - e[1] > y1 - y0:
            break
        S += 0.5
    e = extents(S)
    return S, ((x0 + x1) - (e[0] + e[2])) / 2, ((y0 + y1) - (e[1] + e[3])) / 2

def draw_pipe(g, box):
    S, ox, oy = fit(box)
    pr = lambda p: (iso(p, S)[0] + ox, iso(p, S)[1] + oy)
    k = S / 48  # 선 굵기·기호 크기를 도면 크기에 맞춘다
    # 치수선
    for p0, p1, off, lab in DIMS:
        a0, a1 = (pr(tuple(p[i] + off[i] for i in range(3))) for p in (p0, p1))
        b0, b1 = pr(p0), pr(p1)
        g.a(f'<g stroke="{MUTED}" stroke-width="1.2" fill="none" opacity=".7">'
            f'<line x1="{b0[0]:.1f}" y1="{b0[1]:.1f}" x2="{a0[0]:.1f}" y2="{a0[1]:.1f}" stroke-dasharray="2 4"/>'
            f'<line x1="{b1[0]:.1f}" y1="{b1[1]:.1f}" x2="{a1[0]:.1f}" y2="{a1[1]:.1f}" stroke-dasharray="2 4"/>'
            f'<line x1="{a0[0]:.1f}" y1="{a0[1]:.1f}" x2="{a1[0]:.1f}" y2="{a1[1]:.1f}"/></g>')
        for q in (a0, a1):
            g.a(f'<circle cx="{q[0]:.1f}" cy="{q[1]:.1f}" r="2.4" fill="{MUTED}"/>')
        mx, my = (a0[0] + a1[0]) / 2, (a0[1] + a1[1]) / 2
        ang = math.degrees(math.atan2(a1[1] - a0[1], a1[0] - a0[0]))
        ang = ang - 180 if ang > 90 else ang + 180 if ang < -90 else ang
        g.a(f'<text x="{mx:.1f}" y="{my - 7:.1f}" transform="rotate({ang:.1f} {mx:.1f} {my:.1f})" font-family="{MONO}" '
            f'font-size="14" fill="{MUTED}" text-anchor="middle">{lab}</text>')
    # 배관: 뒤쪽부터 그리고 겹치는 곳마다 바탕색 틈
    def poly(ps, col, w):
        g.a('<polyline points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in map(pr, ps)) +
            f'" fill="none" stroke="{col}" stroke-width="{w:.1f}" stroke-linejoin="round" stroke-linecap="round"/>')
    for ps, col in ((BR, TEXT), SPOOLS[2], SPOOLS[0], SPOOLS[1]):
        poly(ps, BG, 15 * k); poly(ps, col, 6.5 * k)
    def unit(p, q):
        (x0, y0), (x1, y1) = pr(p), pr(q)
        L = math.hypot(x1 - x0, y1 - y0)
        return x0, y0, (x1 - x0) / L, (y1 - y0) / L
    # 플랜지
    for p, q, col in ((P[0], P[1], TEXT), (BR[2], BR[1], TEXT), (P[8], P[7], MUTED)):
        x0, y0, ux, uy = unit(p, q)
        for d in (0, 7 * k):
            bx, by = x0 + ux * d, y0 + uy * d
            g.a(f'<line x1="{bx + uy*13*k:.1f}" y1="{by - ux*13*k:.1f}" x2="{bx - uy*13*k:.1f}" y2="{by + ux*13*k:.1f}" '
                f'stroke="{col}" stroke-width="{4*k:.1f}" stroke-linecap="round"/>')
    # 밸브(분기 가운데)
    x0, y0, ux, uy = unit(BR[0], BR[1])
    (x1, y1) = pr(BR[1])
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    nx, ny = -uy, ux
    h, w = 14 * k, 12 * k
    g.a(f'<path d="M{mx-ux*h+nx*w:.1f},{my-uy*h+ny*w:.1f} L{mx-ux*h-nx*w:.1f},{my-uy*h-ny*w:.1f} '
        f'L{mx+ux*h+nx*w:.1f},{my+uy*h+ny*w:.1f} L{mx+ux*h-nx*w:.1f},{my+uy*h-ny*w:.1f} Z" '
        f'fill="{BG}" stroke="{TEXT}" stroke-width="{3*k:.1f}" stroke-linejoin="round"/>')
    g.a(f'<line x1="{mx:.1f}" y1="{my:.1f}" x2="{mx+nx*24*k:.1f}" y2="{my+ny*24*k:.1f}" stroke="{TEXT}" stroke-width="{3*k:.1f}"/>'
        f'<line x1="{mx+nx*24*k-ux*9*k:.1f}" y1="{my+ny*24*k-uy*9*k:.1f}" x2="{mx+nx*24*k+ux*9*k:.1f}" '
        f'y2="{my+ny*24*k+uy*9*k:.1f}" stroke="{TEXT}" stroke-width="{3*k:.1f}" stroke-linecap="round"/>')
    # 공장 용접점(속 빈 원, 스풀 색) · 현장 용접점(꽉 찬 원 + 점선 고리)
    for p, col in ((P[1], TEXT), (T, TEXT), (P[2], RED), (P[3], RED), (P[4], RED), (P[5], RED), (P[6], MUTED), (P[7], MUTED)):
        x, y = pr(p)
        g.a(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{8*k:.1f}" fill="{BG}" stroke="{col}" stroke-width="{3*k:.1f}"/>')
    for p in (F1, F2):
        x, y = pr(p)
        g.a(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{16*k:.1f}" fill="none" stroke="{RED}" stroke-width="1.5" stroke-dasharray="3 3"/>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{7.5*k:.1f}" fill="{RED}"/>')
    # 번호 칩: 같은 길이의 선 끝에 알약. 선 방향으로 알약을 밀어 선이 알약 가장자리에 닿게 한다
    for p, lab, ang, fill, fg in CHIPS:
        x, y = pr(p)
        c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        ex, ey = x + LEAD * c, y + LEAD * s
        w = chip_w(lab)
        cx, cy = ex + c * w / 2, ey + s * 12
        g.a(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{MUTED}" stroke-width="1.2"/>')
        g.a(f'<rect x="{cx - w/2:.1f}" y="{cy - 12:.1f}" width="{w:.1f}" height="24" rx="12" fill="{fill}"/>')
        g.text(cx, cy + 4.5, lab, 13, fg, 'middle', '600')

def compass(g, x, y):
    ex, ey = x + C * 36, y - Sn * 36
    g.a(f'<g stroke="{MUTED}" stroke-width="1.5" fill="none" opacity=".8" stroke-linecap="round">'
        f'<line x1="{x}" y1="{y}" x2="{ex:.1f}" y2="{ey:.1f}"/>'
        f'<path d="M{ex-9:.1f},{ey-2:.1f} L{ex:.1f},{ey:.1f} L{ex-5:.1f},{ey+8:.1f}"/></g>')
    g.text(ex + 8, ey - 4, 'N', 14, MUTED)

def spool_list(g, x, y, w, h):
    g.a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{PANEL}"/>')
    g.text(x + 20, y + 32, 'SPOOL LIST', 12, MUTED, ls='1.5')
    pad, top, gap = 12, 48, 10
    th = (h - top - pad - gap * 2) / 3
    for i, (ps, col) in enumerate(SPOOLS):
        ty = y + top + i * (th + gap)
        sel = i == 1
        g.a(f'<rect x="{x+pad}" y="{ty:.1f}" width="{w-2*pad}" height="{th:.1f}" rx="16" fill="{INSET if sel else BG}"'
            + (f' stroke="{RED}" stroke-width="2"' if sel else '') + '/>')
        # 실제 스풀 모양을 줄여 칸 가운데(글자 위 영역)에 둔다
        pts = [iso(p, 1) for p in ps]
        x0, x1 = min(p[0] for p in pts), max(p[0] for p in pts)
        y0, y1 = min(p[1] for p in pts), max(p[1] for p in pts)
        bw, bh = w - 2 * pad - 48, th - 50
        s = min(bw / (x1 - x0 or 1), bh / (y1 - y0 or 1))
        cx, cy = x + w / 2, ty + 12 + bh / 2 + 4
        d = ' '.join(f'{cx + (px - (x0+x1)/2) * s:.1f},{cy + (py - (y0+y1)/2) * s:.1f}' for px, py in pts)
        g.a(f'<polyline points="{d}" fill="none" stroke="{RED if sel else BODY}" stroke-width="3" stroke-linejoin="round" stroke-linecap="round"/>')
        g.text(x + pad + 14, ty + th - 14, f'SP-0{i+1}', 12, TEXT if sel else MUTED)

def tabs(g, cx, y):
    items, pad, gap = [('3D', 60), ('2D ISO', 92), ('WELD MAP', 112)], 6, 6
    tw = sum(w for _, w in items) + gap * 2 + pad * 2
    x = cx - tw / 2
    g.a(f'<rect x="{x:.1f}" y="{y}" width="{tw:.1f}" height="48" rx="24" fill="{PANEL}"/>')
    x += pad
    for i, (lab, w) in enumerate(items):
        on = i == 2
        if on:
            g.a(f'<rect x="{x:.1f}" y="{y+pad}" width="{w}" height="36" rx="18" fill="{TEXT}"/>')
        g.text(x + w / 2, y + 29, lab, 13, BG if on else MUTED, 'middle', '600')
        x += w + gap

def title_block(g, x, y, w, h):
    rows = [[('SPOOL NO', 'SP-02', RED), ('DWG NO', 'ISO-0412', TEXT), ('REV', '01', TEXT)],
            [('SHOP WELD', '4', TEXT), ('FIELD WELD', '2', RED), ('SHEET', '2 / 3', TEXT)]]
    cw = [w * 0.36, w * 0.38, w * 0.26]
    st = f'stroke="{MUTED}" stroke-width="1" opacity=".6"'
    g.a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" {st}/>'
        f'<line x1="{x}" y1="{y+h/2}" x2="{x+w}" y2="{y+h/2}" {st}/>')
    cx = x
    for c in cw[:-1]:
        cx += c
        g.a(f'<line x1="{cx:.1f}" y1="{y}" x2="{cx:.1f}" y2="{y+h}" {st}/>')
    for r, row in enumerate(rows):
        cx = x
        for (k, v, col), c in zip(row, cw):
            yy = y + r * h / 2
            g.text(cx + 12, yy + 17, k, 10, MUTED, ls='.5')
            g.text(cx + 12, yy + 39, v, 16, col, fw='700')
            cx += c

out = sys.argv[1] if len(sys.argv) > 1 else '.'

# 상세 1200×440: 데스크톱은 거의 다 보이고, 모바일(1.52:1)은 가운데 약 668px(266~934)만 보인다.
# 목록은 모바일에서 통째로 빠지도록 왼쪽 끝, 도면은 그 가운데 띠 안에 둔다
g = Svg(1200, 440)
spool_list(g, 28, 28, 184, 384)
draw_pipe(g, (390, 40, 910, 400))
compass(g, 1010, 110)
g.save(os.path.join(out, 'ezspool.svg'))

# 카드 600×840(데스크톱 0.71:1 · 모바일 0.76:1 — 거의 안 잘린다): 위 보기 탭 · 가운데 도면 · 아래 표제란
g = Svg(600, 840)
tabs(g, 300, 44)
draw_pipe(g, (44, 124, 556, 668))
title_block(g, 44, 700, 512, 96)
g.save(os.path.join(out, 'ezspool-thumb.svg'))
