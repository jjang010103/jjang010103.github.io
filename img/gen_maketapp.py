# MakeTApp 이미지 생성기(공용 도구는 imgkit.py, 규칙은 AGENTS.md "프로젝트 이미지 만들기").
#   python3 img/gen_maketapp.py img  →  maketapp.svg(상세 데스크톱) · maketapp-m.svg(상세 모바일) + 라이트판
# 원본 참고: 티앱스토어 소개 영상(원근으로 겹친 PC 앱스토어 창과 앱 카드 격자)·입점 혜택(바탕화면 아이콘 뱃지·타겟 푸시).
# 1칸 카드라 카드 썸네일은 화면에 나오지 않아 만들지 않는다.
import math, os, sys
from imgkit import *

LIGHT_MT = {RED: '#b3242b'}          # 라이트에서도 뱃지·강조는 빨강(다른 이미지와 같다)
CARD = '#f1f0ec'                     # 창 안 흰 면(다크 ink 값 → 라이트 흰색)
LIGHT_MT[CARD] = '#ffffff'
TONES = [BLUE, RED, LAV, MUTED, BLUE, LAV, RED, MUTED, LAV, BLUE]   # 앱 썸네일 색


def bars(g, x, y, widths, col, h=6, gap=12):
    for i, w in enumerate(widths):
        g.a(f'<rect x="{x}" y="{y + i * gap}" width="{w}" height="{h}" rx="3" fill="{col}"/>')


def window(g, x, y, w, h, cols, rows, full=True, sel=None):
    """앱스토어 창: 제목 줄(뒤로·검색·창 버튼) + 카테고리 머리 + 앱 카드 격자"""
    g.a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{PANEL}" stroke="{LINE}" stroke-width="2"/>')
    if not full:
        return
    g.a(f'<path d="M{x+22} {y+20} l-5 5 l5 5 M{x+34} {y+20} l5 5 l-5 5" fill="none" stroke="{MUTED}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>')
    g.a(f'<rect x="{x+w/2-90}" y="{y+14}" width="180" height="22" rx="11" fill="{INSET}"/>')
    g.a(f'<circle cx="{x+w/2+72}" cy="{y+25}" r="5" fill="none" stroke="{MUTED}" stroke-width="2"/>')
    for i, d in enumerate(('M-5 0 h10', 'M-5 -5 h10 v10 h-10 z', 'M-5 -5 l10 10 M5 -5 l-10 10')):
        g.a(f'<path transform="translate({x+w-70+i*22} {y+25})" d="{d}" fill="none" stroke="{MUTED}" stroke-width="2" stroke-linecap="round"/>')
    # 카테고리 머리: 폴더 + 이름 막대, 오른쪽 정렬 탭
    g.a(f'<path d="M{x+24} {y+62} h10 l4 4 h12 v14 h-26 z" fill="{BLUE}"/>')
    bars(g, x + 58, y + 68, [96], TEXT, 8)
    for i in range(4):
        bars(g, x + w - 180 + i * 42, y + 70, [30], MUTED if i else TEXT, 5)
    # 앱 카드 격자
    gx, gy, gap = x + 24, y + 100, 14
    cw = (w - 48 - gap * (cols - 1)) / cols
    ch = (h - 100 - 20 - gap * (rows - 1)) / rows
    for r in range(rows):
        for c in range(cols):
            k = r * cols + c
            cx, cy = gx + c * (cw + gap), gy + r * (ch + gap)
            th = ch - 38
            col = TONES[k % len(TONES)]
            g.a(f'<rect x="{cx:.1f}" y="{cy:.1f}" width="{cw:.1f}" height="{th:.1f}" rx="10" fill="{col}"'
                + (f' stroke="{TEXT}" stroke-width="3"' if k == sel else '') + '/>')
            # 썸네일 안: 흰 면 한 장 + 원 하나(앱 화면 느낌)
            g.a(f'<rect x="{cx+cw*0.48:.1f}" y="{cy+th*0.22:.1f}" width="{cw*0.4:.1f}" height="{th*0.56:.1f}" rx="6" fill="{CARD}" opacity=".9"/>')
            g.a(f'<circle cx="{cx+cw*0.26:.1f}" cy="{cy+th*0.5:.1f}" r="{min(cw, th)*0.14:.1f}" fill="{CARD}" opacity=".9"/>')
            g.a(f'<rect x="{cx:.1f}" y="{cy+th+8:.1f}" width="16" height="16" rx="5" fill="{col}"/>')
            bars(g, cx + 22, cy + th + 9, [cw * 0.5], TEXT, 5, 0)
            bars(g, cx + 22, cy + th + 19, [cw * 0.34], MUTED, 4, 0)


SKEW = -6   # 창 원근(도)


def on_stack(x, y, px, py):
    """창 로컬 좌표 → 화면 좌표(stack의 translate + skewY와 같은 변환)"""
    return x + px, y + py + px * math.tan(math.radians(SKEW))


def cell(w, h, cols, rows, k):
    """window() 격자의 k번째 카드 썸네일 (가운데 x, 위 y)"""
    gap = 14
    cw = (w - 48 - gap * (cols - 1)) / cols
    ch = (h - 100 - 20 - gap * (rows - 1)) / rows
    r, c = divmod(k, cols)
    return 24 + c * (cw + gap) + cw / 2, 100 + r * (ch + gap)


def stack(g, x, y, w, h, cols, rows, sel=None):
    """원근으로 겹친 창 세 장(소개 영상처럼). 뒤 두 장은 틀만"""
    for i in (2, 1):
        g.a(f'<g transform="translate({x + i * 30} {y - i * 16}) skewY({SKEW})" opacity="{1 - i * 0.28:.2f}">')
        window(g, 0, 0, w, h, cols, rows, full=False)
        g.a('</g>')
    g.a(f'<g transform="translate({x} {y}) skewY({SKEW})">')
    window(g, 0, 0, w, h, cols, rows, sel=sel)
    g.a('</g>')


def app_icon(g, x, y, s, col, badge=None):
    """바탕화면 앱 아이콘(둥근 네모 + 흰 T) + 이름 막대. badge가 있으면 오른쪽 위 빨간 뱃지"""
    g.a(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{s*0.26:.1f}" fill="{col}"/>')
    g.a(f'<path d="M{x+s*0.28:.1f} {y+s*0.3:.1f} h{s*0.44:.1f} M{x+s*0.5:.1f} {y+s*0.3:.1f} v{s*0.42:.1f}" stroke="{CARD}" stroke-width="{s*0.12:.1f}" stroke-linecap="round"/>')
    bars(g, x + s * 0.12, y + s + 10, [s * 0.76], MUTED, 5)
    if badge:
        g.a(f'<circle cx="{x+s-2}" cy="{y+2}" r="14" fill="{RED}" stroke="{BG}" stroke-width="3"/>')
        g.text(x + s - 2, y + 7, badge, 13, '#ffffff', 'middle', '700')


def toast(g, x, y, w):
    """타겟 푸시 알림(바탕화면 오른쪽 위에 뜨는 카드)"""
    g.a(f'<rect x="{x}" y="{y}" width="{w}" height="96" rx="18" fill="{CARD}" stroke="{LINE}" stroke-width="2"/>')
    g.a(f'<rect x="{x+16}" y="{y+18}" width="28" height="28" rx="8" fill="{BLUE}"/>')
    g.a(f'<path d="M{x+23} {y+27} h14 M{x+30} {y+27} v12" stroke="{CARD}" stroke-width="3.5" stroke-linecap="round"/>')
    g.text(x + 54, y + 30, 'PUSH', 11, BLUE, fw='700', ls='1')
    bars(g, x + 54, y + 38, [w * 0.42], INSET, 7)
    bars(g, x + 16, y + 60, [w - 60, w * 0.5], INSET, 6, 12)
    g.a(f'<circle cx="{x+w-22}" cy="{y+24}" r="5" fill="{RED}"/>')


out = sys.argv[1] if len(sys.argv) > 1 else '.'

# 상세 1200×440(데스크톱): 한 장의 PC 바탕화면. 가운데 겹친 앱스토어 창, 오른쪽 가장자리 바탕화면 아이콘,
# 오른쪽 아래 구석 푸시 알림. 스토어에서 고른 앱 카드 → 바탕화면에 설치된 뱃지 아이콘을 점선으로 잇는다
g = Svg(1200, 440)
WX, WY, WW, WH, SEL = 90, 96, 640, 320, 4
stack(g, WX, WY, WW, WH, 5, 2, SEL)
IX, IS = 1066, 72
for i, (col, badge) in enumerate(((BLUE, '3'), (LAV, None), (MUTED, None))):
    app_icon(g, IX, 34 + i * 116, IS, col, badge)
px, py = cell(WW, WH, 5, 2, SEL)
x0, y0 = on_stack(WX, WY, px, py)
x1, y1 = IX - 6, 34 + IS / 2
g.a(f'<path d="M{x0:.1f},{y0-4:.1f} C{x0:.1f},{y0-90:.1f} {x1-150:.1f},{y1:.1f} {x1:.1f},{y1:.1f}" fill="none" stroke="{BLUE}" stroke-width="2.5" stroke-dasharray="6 6" stroke-linecap="round"/>')
g.a(f'<path d="M{x1-9:.1f},{y1-7:.1f} L{x1:.1f},{y1:.1f} L{x1-9:.1f},{y1+7:.1f}" fill="none" stroke="{BLUE}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')
g.a(f'<circle cx="{x0:.1f}" cy="{y0-4:.1f}" r="5" fill="{BLUE}"/>')
toast(g, 742, 318, 300)
g.save(os.path.join(out, 'maketapp.svg'), LIGHT_MT)

# 상세 모바일 668×440: 앞 창 하나 + 뱃지 아이콘
g = Svg(668, 440)
stack(g, 60, 90, 470, 300, 3, 2)
app_icon(g, 548, 250, 76, BLUE, '3')
g.save(os.path.join(out, 'maketapp-m.svg'), LIGHT_MT)
