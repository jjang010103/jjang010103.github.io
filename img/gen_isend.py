# 아이센드 이미지 생성기(공용 도구는 imgkit.py, 규칙은 AGENTS.md "프로젝트 이미지 만들기").
#   python3 img/gen_isend.py img  →  isend.svg(상세, 1200×440) · isend-thumb.svg(카드, 600×840) + 라이트판
# 원본 참고: 공식 사이트 첫 화면 — V자로 기운 폰 두 대(알림 메시지 카드)와 떠 있는 아이콘 타일(말풍선·과녁·봉투).
# 카카오 노랑·실제 브랜드 이름과 문구는 쓰지 않는다. 헤더는 강조색, 글자는 막대로 추상화한다.
import math, os, sys
from imgkit import *

# 라이트에서도 강조(메시지 헤더·CTA)는 빨강으로 둔다 — Ez-Spool과 같다
# 메시지 카드 바탕·카드 안 글자 막대는 전용 색이다. 다크는 ink(#f1f0ec)·ink-inset(#2c2c30) 다크 값,
# 라이트는 흰 카드·연회색 막대(ink-text-soft). TEXT로 칠하면 라이트에서 카드가 검게 뒤집혔다(사용자 지적, 2026-09-30)
CARD, BAR = '#f1f0ec', '#2c2c30'
LIGHT_IS = {RED: '#b3242b', CARD: '#ffffff', BAR: '#b3b2ab'}
# 폰 화면 안의 강조(헤더·쿠폰·아래 버튼)는 파랑으로 둔다(사용자 결정, 2026-09-30)


def bars(g, x, y, widths, col=BAR, h=6, gap=13):
    for i, w in enumerate(widths):
        g.a(f'<rect x="{x}" y="{y + i * gap}" width="{w}" height="{h}" rx="3" fill="{col}"/>')


def phone(g, cx, cy, s, rot, variant):
    """폰 한 대. 로컬 좌표 200×410(가운데 원점)을 옮기고 돌리고 줄인다"""
    g.a(f'<g transform="translate({cx} {cy}) rotate({rot}) scale({s})">')
    # 측면 버튼(왼쪽 볼륨 둘 · 오른쪽 전원) — 몸체 뒤에 깔아 가장자리만 보인다
    for x, y, h in ((-104, -122, 26), (-104, -88, 26), (100, -104, 44)):
        g.a(f'<rect x="{x}" y="{y}" width="4" height="{h}" rx="2" fill="{LINE}"/>')
    g.a(f'<rect x="-100" y="-205" width="200" height="410" rx="32" fill="{LINE}"/>')
    g.a(f'<rect x="-91" y="-196" width="182" height="392" rx="24" fill="{PANEL}"/>')
    # 화면 안 내용은 화면 모양(둥근 모서리)으로 잘라 가장자리 막대가 삐져나오지 않게 한다
    cid = f'scr{len(g.o)}'
    g.a(f'<clipPath id="{cid}"><rect x="-91" y="-196" width="182" height="392" rx="24"/></clipPath><g clip-path="url(#{cid})">')
    # 다이나믹 아일랜드: 윗변에서 떨어진 알약. 폰 테두리와 같은 색(사용자 결정, 2026-09-30)
    g.a(f'<rect x="-30" y="-188" width="60" height="18" rx="9" fill="{LINE}"/>')
    bars(g, -74, -181.5, [22], MUTED, 5)                                                      # 시계(아일랜드와 같은 높이)
    g.a(f'<path d="M56 -175 v-4 M61 -175 v-6 M66 -175 v-8" stroke="{MUTED}" stroke-width="2.5" stroke-linecap="round"/>')
    g.a(f'<path d="M-66 -158 l-7 7 l7 7" fill="none" stroke="{MUTED}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')
    bars(g, -26, -160, [52], BODY, 7)                                                         # 대화방 이름
    bars(g, -18, -147, [36], MUTED, 5)
    g.a(f'<rect x="-50" y="-128" width="100" height="16" rx="8" fill="{LINE}"/>')              # 날짜 알약
    # 메시지 카드: 빨간 머리 + 밝은 몸통
    top, bottom = -100, (122 if variant == 'coupon' else 128)
    g.a(f'<rect x="-72" y="{top}" width="148" height="{bottom - top}" rx="14" fill="{CARD}"/>')
    g.a(f'<path d="M-72 {top+24} v-10 a14 14 0 0 1 14 -14 h120 a14 14 0 0 1 14 14 v10 z" fill="{BLUE}"/>')
    g.text(-60, top + 16, 'ALIMTALK', 9, '#ffffff', fw='700', ls='.8')
    if variant == 'coupon':
        # 쿠폰 표 + 제목 막대 + 본문 + 버튼
        g.a(f'<path d="M-22 -58 h44 v8 a6 6 0 0 0 0 12 v8 h-44 v-8 a6 6 0 0 0 0 -12 z" fill="none" stroke="{BLUE}" stroke-width="3" stroke-linejoin="round"/>')
        g.a(f'<line x1="-4" y1="-54" x2="-4" y2="-34" stroke="{BLUE}" stroke-width="2" stroke-dasharray="3 3"/>')
        bars(g, -14, -20, [28], BAR, 7)
        bars(g, -60, 0, [118, 96, 108, 70, 90])
        g.a(f'<rect x="-60" y="{bottom-30}" width="124" height="20" rx="10" fill="none" stroke="{BAR}" stroke-width="2"/>')
        # 아래 탭 줄
        g.a(f'<rect x="-91" y="148" width="182" height="48" fill="{BG}"/>')
        for i in range(3):
            g.a(f'<circle cx="{-55 + i*55}" cy="166" r="6" fill="none" stroke="{MUTED}" stroke-width="2"/>')
            bars(g, -67 + i * 55, 178, [24], MUTED, 4)
    else:
        # 긴 본문 + 링크 막대(파랑) + 아래 CTA 막대
        bars(g, -60, -64, [118, 100])
        bars(g, -60, -34, [84], BLUE)
        bars(g, -60, -8, [110, 92])
        bars(g, -60, 18, [76], BLUE)
        bars(g, -60, 44, [116, 98, 104, 60])
        g.a(f'<rect x="-91" y="152" width="182" height="44" fill="{BLUE}"/>')
        bars(g, -28, 168, [56], '#ffffff', 6)
    g.a('</g></g>')


def tile(g, cx, cy, size, rot, kind):
    """떠 있는 아이콘 타일(원본의 유리 타일을 평면 판으로). 강조는 빨강(폰 안은 파랑, 사용자 결정 2026-09-30)"""
    s = size / 120
    g.a(f'<g transform="translate({cx} {cy}) rotate({rot}) scale({s:.3f})">')
    g.a(f'<rect x="-60" y="-60" width="120" height="120" rx="30" fill="{PANEL}" stroke="{LINE}" stroke-width="2"/>')
    if kind == 'chat':
        g.a(f'<path d="M-34 -2 a28 26 0 1 1 18 24 l-16 8 l4 -14 a28 26 0 0 1 -6 -18 z" fill="{RED}"/>')
        g.a(f'<circle cx="14" cy="16" r="24" fill="{TEXT}"/>')   # 다크는 밝은 원·짙은 점, 라이트는 검은 원·흰 점(사용자 결정, 2026-09-30)
        for dx in (-10, 0, 10):   # 작은 말풍선(중심 14, 16)의 가운데에 맞춘다
            g.a(f'<circle cx="{14 + dx}" cy="16" r="3.5" fill="{BG}"/>')
    elif kind == 'target':
        for r, col in ((32, RED), (21, RED), (10, RED)):
            g.a(f'<circle cx="0" cy="4" r="{r}" fill="none" stroke="{col}" stroke-width="5"/>')
        g.a(f'<line x1="0" y1="4" x2="30" y2="-30" stroke="{TEXT}" stroke-width="5" stroke-linecap="round"/>')
        g.a(f'<path d="M22 -34 l12 -2 l-2 12" fill="none" stroke="{TEXT}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>')
    else:  # mail
        g.a(f'<rect x="-24" y="-34" width="48" height="44" rx="6" fill="{CARD}" stroke="{LINE}" stroke-width="1.5"/>')
        bars(g, -14, -24, [28, 28, 20], RED, 5, 11)
        g.a(f'<path d="M-36 -6 l36 26 l36 -26 v38 a6 6 0 0 1 -6 6 h-60 a6 6 0 0 1 -6 -6 z" fill="{RED}"/>')
    g.a('</g>')


def scene(g, cx, cy, s):
    """폰 두 대 + 타일 셋. (cx, cy) 가운데, s 배율"""
    phone(g, cx - 95 * s, cy + 30 * s, 0.9 * s, -16, 'coupon')
    phone(g, cx + 95 * s, cy - 25 * s, 0.9 * s, 16, 'links')
    tile(g, cx - 175 * s, cy - 150 * s, 100 * s, -8, 'chat')
    tile(g, cx + 185 * s, cy + 140 * s, 96 * s, 10, 'target')
    tile(g, cx - 165 * s, cy + 175 * s, 96 * s, 0, 'mail')


# 공식 사이트 "개인화 맞춤형 메시징"의 네 사례. 설명은 원문을 줄였다. 04는 쿠폰 폰과 짝이라 강조한다
CASES = [('01', '#장바구니 리마인드', '담은 상품 구매 유도'), ('02', '#결제이탈', '이탈 고객 결제 재유도'),
         ('03', '#구매완료', '구매 안내 메시지'), ('04', '#헤비유저', '헤비 유저에게 쿠폰')]


def case_card(g, cx, cy, rot, case, on):
    """떠 있는 사례 카드: 번호(큰 글자) 왼쪽 · 해시태그와 설명 오른쪽. 강조 카드는 파란 바탕"""
    num, title, desc = case
    w, h = 250, 92
    fg = BG if on else TEXT
    g.a(f'<g transform="translate({cx} {cy}) rotate({rot})">')
    g.a(f'<rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="22" fill="{BLUE if on else PANEL}"'
        + ('' if on else f' stroke="{LINE}" stroke-width="1.5"') + '/>')
    g.text(-w / 2 + 20, 12, num, 30, BG if on else BLUE, fw='800')
    g.text(-w / 2 + 78, -4, title, 15, fg, fw='700', font=SANS)
    g.text(-w / 2 + 78, 20, desc, 12, BG if on else MUTED, font=SANS)
    g.a('</g>')
    return cx, cy, rot, w


def at(cx, cy, rot, s, x, y):
    """폰 로컬 좌표(x, y)를 화면 좌표로(phone()의 translate·rotate·scale과 같은 변환)"""
    c, n = math.cos(math.radians(rot)), math.sin(math.radians(rot))
    return cx + s * (x * c - y * n), cy + s * (x * n + y * c)


def hero(g):
    """데스크톱 상세 한 장면: 가운데 폰 두 대, 둘레에 사례 카드 넷.
    강조한 04(헤비유저)에서 쿠폰 폰의 쿠폰까지 점선을 이어 '이 고객군에 이 메시지'가 보이게 한다"""
    L = (505, 232, -12, 0.8)       # 쿠폰 폰 (cx, cy, rot, s)
    R = (688, 212, 12, 0.8)        # 링크 폰
    tile(g, 812, 332, 80, 10, 'target')
    phone(g, L[0], L[1], L[3], L[2], 'coupon')
    phone(g, R[0], R[1], R[3], R[2], 'links')
    tile(g, 790, 96, 80, -8, 'chat')
    case_card(g, 215, 104, -4, CASES[0], False)
    case_card(g, 985, 150, 3, CASES[1], False)
    case_card(g, 1000, 330, -3, CASES[2], False)
    cx, cy, rot, w = case_card(g, 230, 318, 3, CASES[3], True)
    # 04 카드 오른쪽 끝 → 쿠폰
    x0, y0 = cx + w / 2 * math.cos(math.radians(rot)), cy + w / 2 * math.sin(math.radians(rot))
    x1, y1 = at(L[0], L[1], L[2], L[3], -24, -46)
    g.a(f'<path d="M{x0:.1f},{y0:.1f} C{x0+70:.1f},{y0:.1f} {x1-80:.1f},{y1+60:.1f} {x1:.1f},{y1:.1f}" fill="none" stroke="{BLUE}" stroke-width="2.5" stroke-dasharray="6 6" stroke-linecap="round"/>')
    for x, y in ((x0, y0), (x1, y1)):
        g.a(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="{BLUE}"/>')


out = sys.argv[1] if len(sys.argv) > 1 else '.'

# 상세 1200×440(데스크톱): 폰 두 대와 사례 카드 넷을 한 장면으로(두 덩어리를 나란히 놓으면 따로 논다, 사용자 지적 2026-09-30)
g = Svg(1200, 440)
hero(g)
g.save(os.path.join(out, 'isend.svg'), LIGHT_IS)

# 모바일 상세 668×440: 폰 장면만 크게(타일 글자는 모바일 폭에서 너무 작다)
g = Svg(668, 440)
scene(g, 334, 222, 0.85)
g.save(os.path.join(out, 'isend-m.svg'), LIGHT_IS)

# 카드 600×840: 폰 장면만 크게 둔다. 도면처럼 비어 보이지 않아 위 탭·아래 표제란은 두지 않는다(사용자 결정, 2026-09-30)
g = Svg(600, 840)
scene(g, 310, 420, 1.2)
g.save(os.path.join(out, 'isend-thumb.svg'), LIGHT_IS)
