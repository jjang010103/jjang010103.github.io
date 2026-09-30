# MakeTApp 이미지 생성기(공용 도구는 imgkit.py, 규칙은 AGENTS.md "프로젝트 이미지 만들기").
#   python3 img/gen_maketapp.py img  →  maketapp.svg(상세 데스크톱) · maketapp-m.svg(상세 모바일) + 라이트판
# 무엇을 하는 서비스인지 그림만 봐도 읽히게: 브라우저 속 쇼핑몰 → CREATE → 주소창 없는 PC 앱 창(같은 쇼핑몰) + 푸시.
# 추상 카드 격자만 그렸더니 무슨 서비스인지 알 수 없었다(사용자 지적, 2026-09-30).
# 원본 참고: 티앱스토어 소개 영상·입점 혜택(쇼핑몰 PC 앱, 바탕화면 뱃지, 타겟 푸시). 1칸 카드라 썸네일은 만들지 않는다.
import os, sys
from imgkit import *

CARD = '#f1f0ec'                                   # 창 안 흰 면(다크 ink 값 → 라이트 흰색)
# 쇼핑몰 화면은 두 테마 모두 '밝은 면 + 짙은 글자'다. 사이트 색(TEXT 등)을 쓰면 다크에서 뒤집혀 전용 색을 둔다
TILE, INK = '#d9d8d2', '#2c2c30'                   # 상품 칸 · 글자 막대(다크 ink-inset 값들)
LIGHT_MT = {RED: '#b3242b', CARD: '#ffffff', TILE: '#ecebe6', INK: '#17171a'}   # 라이트에서도 뱃지·강조는 빨강
PRODUCTS = [('shirt', BLUE), ('bag', RED), ('cup', LAV), ('bag', MUTED), ('shirt', RED), ('cup', BLUE)]


def bars(g, x, y, widths, col, h=6, gap=12):
    for i, w in enumerate(widths):
        g.a(f'<rect x="{x:.1f}" y="{y + i * gap:.1f}" width="{w:.1f}" height="{h}" rx="{h/2}" fill="{col}"/>')


def glyph(g, kind, cx, cy, s, col):
    """상품 모양(옷·가방·컵). s = 크기 배율"""
    if kind == 'shirt':
        d = 'M-14 -12 l8 -4 q6 5 12 0 l8 4 l6 9 l-7 4 l-3 -4 v19 h-20 v-19 l-3 4 l-7 -4 z'
    elif kind == 'bag':
        d = 'M-13 -6 h26 l3 22 h-32 z M-6 -6 v-5 a6 6 0 0 1 12 0 v5'
    else:
        d = 'M-11 -12 h22 l-3 26 h-16 z M11 -6 h4 a5 5 0 0 1 0 10 h-5'
    g.a(f'<path transform="translate({cx:.1f} {cy:.1f}) scale({s:.2f})" d="{d}" fill="{col}" stroke="{col}" stroke-width="2" stroke-linejoin="round"/>')


def shop(g, x, y, w, h, cols=3):
    """쇼핑몰 화면: 로고·메뉴 줄 → 배너 → 상품 카드(모양 + 이름·가격 막대)"""
    g.a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{CARD}"/>')
    g.a(f'<rect x="{x+14}" y="{y+12}" width="46" height="12" rx="6" fill="{BLUE}"/>')
    for i in range(3):
        bars(g, x + w - 110 + i * 34, y + 15, [24], INK if i == 0 else TILE, 6)
    bh = h * 0.24
    g.a(f'<rect x="{x+14}" y="{y+34}" width="{w-28}" height="{bh:.1f}" rx="10" fill="{BLUE}"/>')
    bars(g, x + 30, y + 34 + bh * 0.3, [w * 0.34, w * 0.22], CARD, 8, 14)
    g.a(f'<circle cx="{x+w-60:.1f}" cy="{y+34+bh/2:.1f}" r="{bh*0.3:.1f}" fill="{CARD}" opacity=".35"/>')
    top = y + 34 + bh + 12
    gap = 10
    cw = (w - 28 - gap * (cols - 1)) / cols
    ch = (y + h - 12 - top - gap) / 2
    for k in range(cols * 2):
        r, c = divmod(k, cols)
        cx, cy = x + 14 + c * (cw + gap), top + r * (ch + gap)
        kind, col = PRODUCTS[k % len(PRODUCTS)]
        ih = ch - 30
        g.a(f'<rect x="{cx:.1f}" y="{cy:.1f}" width="{cw:.1f}" height="{ih:.1f}" rx="8" fill="{TILE}"/>')
        glyph(g, kind, cx + cw / 2, cy + ih / 2 + 1, min(cw, ih) / 48, col)
        bars(g, cx, cy + ih + 7, [cw * 0.7], MUTED, 5)
        bars(g, cx, cy + ih + 17, [cw * 0.38], INK, 6)


def browser(g, x, y, w, h):
    """브라우저 창: 탭 · 주소창(자물쇠 + https://) · 쇼핑몰"""
    g.a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{PANEL}" stroke="{LINE}" stroke-width="2"/>')
    for i, col in enumerate((RED, LAV, MUTED)):
        g.a(f'<circle cx="{x+20+i*16}" cy="{y+20}" r="5" fill="{col}"/>')
    g.a(f'<rect x="{x+76}" y="{y+10}" width="{w*0.32:.1f}" height="20" rx="8" fill="{CARD}"/>')
    bars(g, x + 88, y + 17, [w * 0.18], MUTED, 6)
    g.a(f'<rect x="{x+14}" y="{y+40}" width="{w-28}" height="26" rx="13" fill="{INSET}"/>')
    g.a(f'<path d="M{x+28} {y+52} v-3 a4 4 0 0 1 8 0 v3 M{x+26} {y+52} h12 v8 h-12 z" fill="none" stroke="{MUTED}" stroke-width="2" stroke-linejoin="round"/>')
    g.text(x + 46, y + 57, 'https://', 12, MUTED)
    bars(g, x + 112, y + 50, [w * 0.3], MUTED, 6)
    shop(g, x + 10, y + 76, w - 20, h - 86)


def app_window(g, x, y, w, h):
    """PC 앱 창: 주소창 없이 앱 아이콘 · 앱 이름 · 창 버튼만, 속은 같은 쇼핑몰"""
    g.a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{PANEL}" stroke="{LINE}" stroke-width="2"/>')
    g.a(f'<rect x="{x+14}" y="{y+12}" width="24" height="24" rx="7" fill="{BLUE}"/>')
    g.a(f'<path d="M{x+20} {y+20} h12 M{x+26} {y+20} v10" stroke="{CARD}" stroke-width="3" stroke-linecap="round"/>')
    bars(g, x + 48, y + 20, [w * 0.24], TEXT, 8)
    for i, d in enumerate(('M-5 0 h10', 'M-5 -5 h10 v10 h-10 z', 'M-5 -5 l10 10 M5 -5 l-10 10')):
        g.a(f'<path transform="translate({x+w-66+i*22} {y+24})" d="{d}" fill="none" stroke="{MUTED}" stroke-width="2" stroke-linecap="round"/>')
    shop(g, x + 10, y + 48, w - 20, h - 58)


def label(g, x, y, text, fill, fg):
    w = 20 + 8.6 * len(text)
    g.a(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="26" rx="13" fill="{fill}"/>')
    g.text(x + w / 2, y + 17.5, text, 12, fg, 'middle', '700', '1')
    return w


def app_icon(g, cx, cy, s, col, badge=None):
    x, y = cx - s / 2, cy - s / 2
    g.a(f'<rect x="{x:.1f}" y="{y:.1f}" width="{s}" height="{s}" rx="{s*0.26:.1f}" fill="{col}" stroke="{BG}" stroke-width="3"/>')
    g.a(f'<path d="M{x+s*0.28:.1f} {y+s*0.32:.1f} h{s*0.44:.1f} M{x+s*0.5:.1f} {y+s*0.32:.1f} v{s*0.4:.1f}" stroke="{CARD}" stroke-width="{s*0.12:.1f}" stroke-linecap="round"/>')
    if badge:
        g.a(f'<circle cx="{x+s-2:.1f}" cy="{y+2:.1f}" r="12" fill="{RED}" stroke="{BG}" stroke-width="3"/>')
        g.text(x + s - 2, y + 6.5, badge, 12, '#ffffff', 'middle', '700')


def arrow(g, x0, y, x1):
    g.a(f'<path d="M{x0} {y} H{x1}" stroke="{MUTED}" stroke-width="3" stroke-dasharray="7 7" stroke-linecap="round"/>')
    g.a(f'<path d="M{x1-10} {y-8} L{x1} {y} L{x1-10} {y+8}" fill="none" stroke="{MUTED}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')


def build(g, cx, cy):
    """가운데 제작 단계: 상자(앱 로고) 뒤로 여러 앱 아이콘이 부채꼴로 찍혀 나온다 + CREATE 라벨.
    상자 윗면·옆면은 두 테마 모두 밝게 — 다크에서 어두운 상자가 바탕에 묻혔다(사용자 지적, 2026-09-30)"""
    for i, (dx, dy, rot, col) in enumerate(((-34, 6, -16, LAV), (34, 6, 16, RED), (0, -6, 0, MUTED))):
        g.a(f'<g transform="translate({cx+dx} {cy-40+dy}) rotate({rot})">')
        app_icon(g, 0, 0, 46, col)
        g.a('</g>')
    # 상자: 앞면 + 윗면 뚜껑
    g.a(f'<path d="M{cx-52} {cy-6} l52 -18 l52 18 l-52 18 z" fill="{CARD}" stroke="{LINE}" stroke-width="2" stroke-linejoin="round"/>')
    g.a(f'<path d="M{cx-52} {cy-6} v54 l52 18 v-54 z" fill="{TILE}" stroke="{LINE}" stroke-width="2" stroke-linejoin="round"/>')
    g.a(f'<path d="M{cx+52} {cy-6} v54 l-52 18 v-54 z" fill="{BLUE}" stroke="{LINE}" stroke-width="2" stroke-linejoin="round"/>')
    g.a(f'<path d="M{cx+14} {cy+28} l24 -8 M{cx+26} {cy+24} v20" stroke="{CARD}" stroke-width="5" stroke-linecap="round"/>')
    w = 20 + 8.6 * len('CREATE')
    label(g, cx - w / 2, cy + 86, 'CREATE', TEXT, BG)   # BUILD는 개발로 읽혀 제작(서비스 이름 Make)으로(사용자 결정, 2026-09-30)


def toast(g, x, y, w):
    g.a(f'<rect x="{x}" y="{y}" width="{w}" height="78" rx="16" fill="{CARD}" stroke="{LINE}" stroke-width="2"/>')
    app_icon(g, x + 30, y + 30, 30, BLUE)
    g.text(x + 54, y + 28, 'PUSH', 11, BLUE, fw='700', ls='1')
    bars(g, x + 54, y + 36, [w * 0.44], INSET, 7)
    bars(g, x + 16, y + 56, [w - 50], INSET, 6)
    g.a(f'<circle cx="{x+w-20}" cy="{y+20}" r="5" fill="{RED}"/>')


out = sys.argv[1] if len(sys.argv) > 1 else '.'

# 상세 1200×440(데스크톱): 브라우저 속 쇼핑몰 → CREATE → 같은 쇼핑몰의 PC 앱 창(+ 푸시 알림)
g = Svg(1200, 440)
label(g, 60, 24, 'WEBSITE', INSET, TEXT)
browser(g, 60, 62, 400, 350)
arrow(g, 478, 236, 530)
build(g, 600, 232)
arrow(g, 670, 236, 722)
label(g, 740, 24, 'PC APP', BLUE, BG)
app_window(g, 740, 62, 400, 350)
toast(g, 888, 344, 280)
g.save(os.path.join(out, 'maketapp.svg'), LIGHT_MT)

# 상세 모바일 668×440: 브라우저 → PC 앱 두 창만(가운데 상자 없이 화살표)
g = Svg(668, 440)
label(g, 28, 24, 'WEBSITE', INSET, TEXT)
browser(g, 28, 62, 280, 350)
arrow(g, 316, 236, 352)
label(g, 360, 24, 'PC APP', BLUE, BG)
app_window(g, 360, 62, 280, 350)
g.save(os.path.join(out, 'maketapp-m.svg'), LIGHT_MT)
