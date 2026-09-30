# Ez-Spool 이미지 생성기(공용 도구는 imgkit.py, 규칙은 AGENTS.md "프로젝트 이미지 만들기").
#   python3 img/gen_ezspool.py img  →  ezspool.svg(상세, 1200×440) · ezspool-thumb.svg(카드, 600×840)
# 칸 실측(2026-09-29): 상세 1181×432(데스크톱)·334×220(모바일), 카드 198×277·120×159. 모두 object-fit:cover.
import math, os, sys
from imgkit import *

# 라이트에서도 하이라이트(선택 스풀)는 빨강으로 둔다(사용자 결정, 2026-09-30). 사이트 accent 다크 값
LIGHT_SPOOL = {RED: '#b3242b'}

# ── 배관 모델(3D). 본관 엘보 7개 + 티 분기(밸브). 스풀 셋으로 나뉜다
P = [(0, 0, 3), (0, 0, 0), (3.5, 0, 0), (3.5, 0, 2.5), (3.5, -3, 2.5), (3.5, -3, 4.5),
     (6, -3, 4.5), (6, -3, 2), (6, -5, 2)]
T = (1.5, 0, 0)
BR = [T, (1.5, 2.2, 0), (1.5, 2.2, -1.5)]

F1, F2 = lerp(T, P[2], 0.5), lerp(P[5], P[6], 0.5)
SPOOLS = [([P[0], P[1], T, F1], TEXT), ([F1, P[2], P[3], P[4], P[5], F2], RED), ([F2, P[6], P[7], P[8]], MUTED)]
DIMS = [(P[0], P[1], (-0.8, 0, 0), '3000'), (P[3], P[4], (-0.8, 0, 0), '3000')]
# 칩: (점, 글자, 방향(도, 화면 기준 0=오른쪽 90=아래), 바탕, 글자색). 선 길이는 모두 같다
CHIPS = [(P[1], 'W1', 150, INSET, TEXT), (T, 'W2', -60, INSET, TEXT), (F1, 'F3', 110, RED, '#ffffff'),
         (P[2], 'W4', 30, INSET, TEXT), (P[4], 'W5', 0, INSET, TEXT), (F2, 'F6', -60, RED, '#ffffff'),
         (P[7], 'W7', 150, INSET, TEXT),
         (lerp(P[0], P[1], 0.45), 'SP-01', 0, TEXT, BG), (lerp(P[3], P[4], 0.5), 'SP-02', 60, RED, '#ffffff'),
         (lerp(P[7], P[8], 0.5), 'SP-03', 60, MUTED, BG)]
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
        add(*chip_box(*iso(p, S), ang, lab))
    return min(xs), min(ys), max(xs), max(ys)


def draw_pipe(g, box):
    S, ox, oy = fit(extents, box)
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
    # 번호 칩
    for p, lab, ang, fill, fg in CHIPS:
        chip(g, *pr(p), ang, lab, fill, fg)

def spool_list(g, x, y, w, h):
    panel(g, x, y, w, h, 'SPOOL LIST')
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

out = sys.argv[1] if len(sys.argv) > 1 else '.'

# 상세 1200×440(데스크톱). 모바일은 아래 ezspool-m.svg를 따로 쓴다.
g = Svg(1200, 440)
spool_list(g, 28, 28, 184, 384)
draw_pipe(g, (390, 40, 910, 400))
compass(g, 1010, 110)
g.save(os.path.join(out, 'ezspool.svg'), LIGHT_SPOOL)

# 모바일 상세 668×440(칸 약 1.52:1과 같다 — 안 잘린다): 도면만 크게
g = Svg(668, 440)
draw_pipe(g, (40, 36, 628, 404))
g.save(os.path.join(out, 'ezspool-m.svg'), LIGHT_SPOOL)

# 카드 600×840(데스크톱 0.71:1 · 모바일 0.76:1 — 거의 안 잘린다): 위 보기 탭 · 가운데 도면 · 아래 표제란
g = Svg(600, 840)
tabs(g, 300, 44, [('3D', 60), ('2D ISO', 92), ('WELD MAP', 112)], 2)
draw_pipe(g, (44, 124, 556, 668))
grid_block(g, 44, 700, 512, 96,
           [[('SPOOL NO', 'SP-02', RED), ('DWG NO', 'ISO-0412', TEXT), ('REV', '01', TEXT)],
            [('SHOP WELD', '4', TEXT), ('FIELD WELD', '2', RED), ('SHEET', '2 / 3', TEXT)]], [0.36, 0.38, 0.26])
g.save(os.path.join(out, 'ezspool-thumb.svg'), LIGHT_SPOOL)
