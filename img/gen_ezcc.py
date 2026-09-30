# Ez-CC 이미지 생성기(공용 도구는 imgkit.py, 규칙은 AGENTS.md "프로젝트 이미지 만들기").
#   python3 img/gen_ezcc.py img  →  ezcc.svg(상세, 1200×440) · ezcc-thumb.svg(카드, 600×840)
# 원본 참고: 공식 페이지의 4D 시공 시각화(파이프랙을 시공 상태 색으로 칠함)·상태 범례 띠·진행률 표.
import math, os, sys
from imgkit import *

# 시공 상태(원본 범례 순서). 원본의 초록·파랑은 토큰 색(ai-2 라벤더·ai-3 파랑)으로 바꿨다
# 라이트에서 RED는 사이트 강조색(파랑)이 되는데, 그러면 ERECTION(ai-3 파랑)과 겹친다 — 도장은 붉은 ai-1로 둔다
LIGHT_CC = {RED: '#d05a6e'}
STATUS = [('NOT STARTED', TEXT), ('WELDING', MUTED), ('PAINTING', RED), ('ARRIVAL', LAV), ('ERECTION', BLUE)]

# ── 파이프랙 모델(3D). 두 단(z=0, z=Z2), 배관은 x 방향으로 달리고 일부는 랙 밖으로 빠진다
BENTS = [0.4, 3.0, 5.6]                 # 철골 프레임 위치(x)
Y0, Y1, ZB, ZT = -0.5, 2.1, -1.4, 2.6   # 기둥 앞뒤(y)·아래·위(z)
Z2 = 2.0                                # 위 단 높이. 두 단이 화면에서 한 띠로 겹치지 않게 벌린다
BEAMS = [-0.3, Z2 - 0.3, ZT]            # 보 높이(각 단 배관 바로 아래 + 꼭대기)
X0, X1 = -0.6, 6.6                      # 배관 양 끝
# (경로, 색, 굵기 배율). 그리는 순서는 앞뒤(y+z)로 정렬한다
PIPES = [
    # 아래 단
    ([(X0, 0, 0), (X1, 0, 0)], BLUE, 1.0),
    ([(X0, 0.35, 0), (2.2, 0.35, 0), (2.2, -1.8, 0), (2.2, -1.8, ZB)], RED, 0.7),    # 랙 뒤로 빠져 내려간다
    ([(X0, 0.7, 0), (X1, 0.7, 0)], TEXT, 1.3),
    ([(X0, 1.05, 0), (4.2, 1.05, 0), (4.2, 1.05, ZB)], MUTED, 0.8),                  # 랙 안에서 떨어진다
    ([(1.2, 1.4, ZB), (1.2, 1.4, 0), (X1, 1.4, 0)], LAV, 0.8),                       # 아래에서 올라온다
    ([(X0, 1.75, 0), (X1, 1.75, 0)], RED, 0.5),
    # 위 단
    ([(X0, 0.1, Z2), (5.2, 0.1, Z2), (5.2, -2.0, Z2)], MUTED, 1.0),                   # 랙 뒤로 빠진다
    ([(X0, 0.5, Z2), (X1, 0.5, Z2)], RED, 1.3),
    ([(X0, 0.9, Z2), (3.5, 0.9, Z2), (3.5, 0.9, 3.3), (X1, 0.9, 3.3)], BLUE, 0.8),    # 꼭대기 위로 올라탄다
    ([(X0, 1.3, Z2), (4.6, 1.3, Z2), (4.6, 3.0, Z2), (4.6, 3.0, ZB)], LAV, 0.9),      # 앞으로 나와 떨어진다
    ([(X0, 1.7, Z2), (X1, 1.7, Z2)], TEXT, 0.5),
]
VALVES = [((2.2, -1.8, -0.7), (2.2, -1.8, 0), RED), ((4.6, 3.0, 0.3), (4.6, 3.0, Z2), LAV)]   # (가운데, 배관 방향 기준점, 색)
FLANGES = [((2.2, -1.8, ZB), (2.2, -1.8, 0), RED), ((4.2, 1.05, ZB), (4.2, 1.05, 0), MUTED),
           ((1.2, 1.4, ZB), (1.2, 1.4, 0), LAV), ((4.6, 3.0, ZB), (4.6, 3.0, 0), LAV)]         # (끝점, 배관 쪽 점, 색)
# 칩: (점, 글자, 방향, 바탕, 글자색). 배관이 없는 빈자리로 뺀다
CHIPS = [((-0.2, 0.5, Z2), 'SP-02', -150, RED, '#ffffff'),
         ((6.3, 0.9, 3.3), 'SP-07', -30, BLUE, BG),
         ((4.6, 3.0, ZB), 'SP-11', 150, LAV, BG)]


def steel():
    """철골 선분 목록: 기둥(앞뒤) + 가로보 + 앞뒤 세로보(스트링거)"""
    segs = []
    for x in BENTS:
        for y in (Y0, Y1):
            segs.append(((x, y, ZB), (x, y, ZT)))
        for z in BEAMS:
            segs.append(((x, Y0, z), (x, Y1, z)))
    for y in (Y0, Y1):
        for z in (BEAMS[0], ZT):
            segs.append(((BENTS[0], y, z), (BENTS[-1], y, z)))
    return segs


def extents(S):
    xs, ys = [], []
    def add(x, y, rx=0, ry=0):
        xs.extend([x - rx, x + rx]); ys.extend([y - ry, y + ry])
    for ps, *_ in PIPES:
        for p in ps:
            add(*iso(p, S), 10, 10)
    for a, b in steel():
        add(*iso(a, S)); add(*iso(b, S))
    for p, lab, ang, *_ in CHIPS:
        add(*chip_box(*iso(p, S), ang, lab))
    return min(xs), min(ys), max(xs), max(ys)


def draw_rack(g, box):
    S, ox, oy = fit(extents, box)
    pr = lambda p: (iso(p, S)[0] + ox, iso(p, S)[1] + oy)
    k = S / 48
    # 철골: 배관 뒤에 옅게
    g.a(f'<g stroke="{MUTED}" stroke-width="{2.2*k:.1f}" stroke-linecap="round" opacity=".4">' + ''.join(
        f'<line x1="{pr(a)[0]:.1f}" y1="{pr(a)[1]:.1f}" x2="{pr(b)[0]:.1f}" y2="{pr(b)[1]:.1f}"/>' for a, b in steel()) + '</g>')
    # 배관: 뒤(y+z 작은 쪽)부터, 겹치는 곳마다 바탕색 틈
    for ps, col, d in sorted(PIPES, key=lambda t: sum(p[1] + p[2] for p in t[0]) / len(t[0])):
        pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in map(pr, ps))
        for c, w in ((BG, (7 * d + 7) * k), (col, 7 * d * k)):
            g.a(f'<polyline points="{pts}" fill="none" stroke="{c}" stroke-width="{w:.1f}" stroke-linejoin="round" stroke-linecap="round"/>')
    def unit(p, q):
        (x0, y0), (x1, y1) = pr(p), pr(q)
        L = math.hypot(x1 - x0, y1 - y0)
        return x0, y0, (x1 - x0) / L, (y1 - y0) / L
    # 플랜지: 배관 끝에 수직인 짧은 두 줄
    for p, q, col in FLANGES:
        x0, y0, ux, uy = unit(p, q)
        for d in (0, 6 * k):
            bx, by = x0 + ux * d, y0 + uy * d
            g.a(f'<line x1="{bx + uy*11*k:.1f}" y1="{by - ux*11*k:.1f}" x2="{bx - uy*11*k:.1f}" y2="{by + ux*11*k:.1f}" '
                f'stroke="{col}" stroke-width="{3.5*k:.1f}" stroke-linecap="round"/>')
    # 밸브: 배관 방향으로 맞댄 두 삼각형
    for c, q, col in VALVES:
        mx, my, ux, uy = unit(c, q)
        nx, ny, h, w = -uy, ux, 12 * k, 10 * k
        g.a(f'<path d="M{mx-ux*h+nx*w:.1f},{my-uy*h+ny*w:.1f} L{mx-ux*h-nx*w:.1f},{my-uy*h-ny*w:.1f} '
            f'L{mx+ux*h+nx*w:.1f},{my+uy*h+ny*w:.1f} L{mx+ux*h-nx*w:.1f},{my+uy*h-ny*w:.1f} Z" '
            f'fill="{BG}" stroke="{col}" stroke-width="{2.6*k:.1f}" stroke-linejoin="round"/>')
    for p, lab, ang, fill, fg in CHIPS:
        chip(g, *pr(p), ang, lab, fill, fg)


def progress(g, x, y, w, h):
    """작업 패키지 진행률(원본 Progress % 표를 막대로)"""
    panel(g, x, y, w, h, 'PROGRESS')
    rows = [('AWP-01', 100), ('AWP-02', 100), ('AWP-03', 64), ('AWP-04', 18), ('AWP-05', 0)]
    pad, top, gap = 12, 48, 8
    rh = (h - top - pad - gap * (len(rows) - 1)) / len(rows)
    for i, (lab, v) in enumerate(rows):
        ty = y + top + i * (rh + gap)
        sel = i == 2
        g.a(f'<rect x="{x+pad}" y="{ty:.1f}" width="{w-2*pad}" height="{rh:.1f}" rx="16" fill="{INSET if sel else BG}"'
            + (f' stroke="{RED}" stroke-width="2"' if sel else '') + '/>')
        g.text(x + pad + 14, ty + rh / 2 - 4, lab, 12, TEXT if sel else MUTED)
        g.text(x + w - pad - 14, ty + rh / 2 - 4, f'{v}%', 12, TEXT if sel else BODY, 'end', '700')
        bw = w - 2 * pad - 28
        by = ty + rh / 2 + 8
        g.a(f'<rect x="{x+pad+14}" y="{by:.1f}" width="{bw}" height="6" rx="3" fill="{LINE}"/>')
        if v:
            g.a(f'<rect x="{x+pad+14}" y="{by:.1f}" width="{bw*v/100:.1f}" height="6" rx="3" fill="{RED if sel else BODY}"/>')


def legend_panel(g, x, y, w, h):
    """시공 상태 범례(원본 범례 띠를 세로 목록으로)"""
    panel(g, x, y, w, h, 'STATUS')
    pad, top, gap = 12, 48, 8
    rh = (h - top - pad - gap * (len(STATUS) - 1)) / len(STATUS)
    for i, (lab, col) in enumerate(STATUS):
        ty = y + top + i * (rh + gap)
        g.a(f'<rect x="{x+pad}" y="{ty:.1f}" width="{w-2*pad}" height="{rh:.1f}" rx="16" fill="{BG}"/>')
        g.a(f'<line x1="{x+pad+18}" y1="{ty+rh/2:.1f}" x2="{x+pad+42}" y2="{ty+rh/2:.1f}" stroke="{col}" stroke-width="8" stroke-linecap="round"/>')
        g.text(x + pad + 56, ty + rh / 2 + 4, lab, 12, BODY)


def legend_strip(g, x, y, w, h):
    """카드 아래 범례 띠: 다섯 칸, 칸마다 색 막대 위 · 이름 아래"""
    g.a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="24" fill="{PANEL}"/>')
    cw = w / len(STATUS)
    for i, (lab, col) in enumerate(STATUS):
        cx = x + cw * (i + 0.5)
        g.a(f'<line x1="{cx-18:.1f}" y1="{y+h/2-10:.1f}" x2="{cx+18:.1f}" y2="{y+h/2-10:.1f}" stroke="{col}" stroke-width="8" stroke-linecap="round"/>')
        g.text(cx, y + h / 2 + 18, lab, 10, MUTED, 'middle', ls='.5')


out = sys.argv[1] if len(sys.argv) > 1 else '.'

# 상세 1200×440(데스크톱). 모바일은 아래 ezcc-m.svg를 따로 쓴다
g = Svg(1200, 440)
progress(g, 28, 28, 184, 384)
draw_rack(g, (300, 36, 900, 404))
legend_panel(g, 988, 28, 184, 384)
g.save(os.path.join(out, 'ezcc.svg'), LIGHT_CC)

# 모바일 상세 668×440: 랙만 크게
g = Svg(668, 440)
draw_rack(g, (40, 30, 628, 410))
g.save(os.path.join(out, 'ezcc-m.svg'), LIGHT_CC)

# 카드 600×840: 위 보기 탭 · 가운데 랙 · 아래 범례 띠
g = Svg(600, 840)
tabs(g, 300, 44, [('WBS', 64), ('4D VIEW', 96), ('INSPECTION', 120)], 1)
draw_rack(g, (44, 124, 556, 668))
legend_strip(g, 44, 700, 512, 96)
g.save(os.path.join(out, 'ezcc-thumb.svg'), LIGHT_CC)
