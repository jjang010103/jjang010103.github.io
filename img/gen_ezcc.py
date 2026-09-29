# Ez-CC 이미지 생성기(공용 도구는 imgkit.py, 규칙은 AGENTS.md "프로젝트 이미지 만들기").
#   python3 img/gen_ezcc.py img  →  ezcc.svg(상세, 1200×440) · ezcc-thumb.svg(카드, 600×840)
# 원본 참고: 공식 페이지의 4D 시공 시각화(파이프랙을 시공 상태 색으로 칠함)·상태 범례 띠·진행률 표.
import os, sys
from imgkit import *

# 시공 상태(원본 범례 순서). 원본의 초록·파랑은 토큰 색(ai-2 라벤더·ai-3 파랑)으로 바꿨다
# 라이트에서 RED는 사이트 강조색(파랑)이 되는데, 그러면 ERECTION(ai-3 파랑)과 겹친다 — 도장은 붉은 ai-1로 둔다
LIGHT_CC = {RED: '#d05a6e'}
STATUS = [('NOT STARTED', TEXT), ('WELDING', MUTED), ('PAINTING', RED), ('ARRIVAL', LAV), ('ERECTION', BLUE)]

# ── 파이프랙 모델(3D). 두 단(z=0, z=1.4), 배관은 x 방향으로 달린다
BENTS = [0.4, 3.0, 5.6]                 # 철골 프레임 위치(x)
Y0, Y1, ZB, ZT = -0.5, 2.1, -1.4, 2.6   # 기둥 앞뒤(y)·아래·위(z)
Z2 = 2.0                                # 위 단 높이. 두 단이 화면에서 한 띠로 겹치지 않게 벌린다
BEAMS = [-0.3, Z2 - 0.3, ZT]            # 보 높이(각 단 배관 바로 아래 + 꼭대기)
# (경로, 색, 굵기 배율). 그리는 순서는 앞뒤(y+z)로 정렬한다
PIPES = [
    ([(-0.6, 0, 0), (6.6, 0, 0)], BLUE, 1.0),
    ([(-0.6, 0.55, 0), (4.4, 0.55, 0), (4.4, 0.55, ZB)], RED, 0.8),          # 랙 아래로 내려간다
    ([(-0.6, 1.1, 0), (6.6, 1.1, 0)], TEXT, 1.3),
    ([(1.7, 1.65, ZB), (1.7, 1.65, 0), (6.6, 1.65, 0)], LAV, 0.8),           # 아래에서 올라온다
    ([(-0.6, 0.2, Z2), (5.2, 0.2, Z2), (5.2, -2.2, Z2)], MUTED, 1.0),        # 랙 뒤로 빠진다
    ([(-0.6, 0.85, Z2), (6.6, 0.85, Z2)], RED, 1.3),
    ([(-0.6, 1.5, Z2), (3.5, 1.5, Z2), (3.5, 1.5, 3.4), (6.6, 1.5, 3.4)], BLUE, 0.8),  # 꼭대기 위로 올라탄다
]
# 칩: (점, 글자, 방향, 바탕, 글자색). 랙 끝의 빈자리로 뺀다
CHIPS = [((-0.2, 0.85, Z2), 'SP-02', -150, RED, '#ffffff'),
         ((6.2, 1.1, 0), 'SP-11', 30, INSET, TEXT),
         ((6.2, 1.5, 3.4), 'SP-07', -30, BLUE, BG)]


def steel():
    """철골 선분 목록: 기둥(앞뒤) + 보"""
    segs = []
    for x in BENTS:
        for y in (Y0, Y1):
            segs.append(((x, y, ZB), (x, y, ZT)))
        for z in BEAMS:
            segs.append(((x, Y0, z), (x, Y1, z)))
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

# 상세 1200×440: 모바일은 가운데 약 668px(266~934)만 보인다 — 양쪽 패널은 빠지고 랙만 남는다
g = Svg(1200, 440)
progress(g, 28, 28, 184, 384)
draw_rack(g, (300, 36, 900, 404))
legend_panel(g, 988, 28, 184, 384)
g.save(os.path.join(out, 'ezcc.svg'), LIGHT_CC)

# 카드 600×840: 위 보기 탭 · 가운데 랙 · 아래 범례 띠
g = Svg(600, 840)
tabs(g, 300, 44, [('WBS', 64), ('4D VIEW', 96), ('INSPECTION', 120)], 1)
draw_rack(g, (44, 124, 556, 668))
legend_strip(g, 44, 700, 512, 96)
g.save(os.path.join(out, 'ezcc-thumb.svg'), LIGHT_CC)
