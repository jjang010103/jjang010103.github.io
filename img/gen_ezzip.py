# ezZip 움직이는 이미지 생성기(공용 도구는 imgkit.py, 규칙은 AGENTS.md "프로젝트 이미지 만들기").
#   python3 img/gen_ezzip.py img  →  ezzip.svg(상세 데스크톱 1200×440) · ezzip-m.svg(카드·상세 모바일 668×440) + 라이트판
# 원본 참고: 이지랩 제품 소개 영상. 장면은 사용자가 고른 핵심 기능 넷(2026-09-30):
#   ① 우클릭 한 번에 압축 ② 끌어 놓아 압축 풀기 ③ 풀 때 바이러스 검사 ④ 한글 파일명 깨짐 없이
# 화면 글자는 한국어, 단계 표시(알약·목록)는 두지 않는다 — AI가 만든 티가 났다(사용자 지적).
# <img>로 넣어도 도는 CSS 애니메이션이다. 동작 줄이기 설정이면 ④의 마지막 장면에서 멈춘다.
import os, sys
from imgkit import *

T = 24.0                                   # 한 바퀴(초)
CARD = '#f1f0ec'                           # 창 안 흰 면(다크 ink 값 → 라이트 흰색)
TILE, INK = '#d9d8d2', '#2c2c30'           # 창 안 옅은 칸 · 짙은 글자(두 테마 모두 밝은 면 위)
LIGHT_ZZ = {RED: '#b3242b', CARD: '#ffffff', TILE: '#ecebe6', INK: '#17171a'}
# ④에 쓰는 파일: (깨진 이름, 바른 이름, 형식, 띠 색, 크기). 깨진 이름은 EUC-KR 한글을 Latin-1로 읽었을 때 실제로 나오는 글자다
FILES = [('º¸°í¼­.xlsx', '보고서.xlsx', 'XLS', BLUE, '84 KB'),
         ('È¸ÀÇ·Ï.pdf', '회의록.pdf', 'PDF', RED, '1.2 MB'),
         ('»çÁø.jpg', '사진.jpg', 'JPG', LAV, '3.4 MB')]


class Anim:
    """요소마다 @keyframes 하나. frames = [(초, 'css')] — 0초와 T초 값을 적어 한 바퀴가 이어지게 한다"""
    def __init__(self):
        self.css, self.n = [], 0

    def add(self, base, frames):
        self.n += 1
        name = f'a{self.n}'
        ks = ' '.join(f'{t / T * 100:.3f}%{{{css}}}' for t, css in frames)
        self.css.append(f'.{name}{{{base};animation:{name} {T}s linear infinite}}@keyframes {name}{{{ks}}}')
        return name

    def vis(self, t0, t1, f=0.3, poster=False):
        """t0~t1초에만 보인다(앞뒤 f초 페이드). poster=True면 움직임을 끈 사용자에게 보이는 정지 화면에 포함"""
        if t0 <= 0:
            fr = [(0, 'opacity:1'), (t1 - f, 'opacity:1'), (t1, 'opacity:0'), (T - f, 'opacity:0'), (T, 'opacity:1')]
        elif t1 >= T:
            fr = [(0, 'opacity:0'), (t0, 'opacity:0'), (t0 + f, 'opacity:1'), (T, 'opacity:1')]
        else:
            fr = [(0, 'opacity:0'), (t0, 'opacity:0'), (t0 + f, 'opacity:1'), (t1 - f, 'opacity:1'), (t1, 'opacity:0'), (T, 'opacity:0')]
        return self.add(f'opacity:{1 if poster else 0}', fr)

    def pop(self, t0, t1, f=0.35, poster=False):
        """t0에 작게서 튀어나와 t1에 사라진다"""
        base = 'transform-box:fill-box;transform-origin:50% 50%'
        fr = [(0, 'opacity:0;transform:scale(.4)'), (t0, 'opacity:0;transform:scale(.4)'),
              (t0 + f * 0.7, 'opacity:1;transform:scale(1.08)'), (t0 + f, 'opacity:1;transform:scale(1)'),
              (t1 - 0.3, 'opacity:1;transform:scale(1)'), (t1, 'opacity:0;transform:scale(1)'), (T, 'opacity:0;transform:scale(.4)')]
        return self.add(f'{base};opacity:{1 if poster else 0}', fr)

    def move(self, pts, base):
        fr = [(t, f'transform:translate({x:.1f}px,{y:.1f}px);animation-timing-function:ease-in-out') for t, x, y in pts]
        return self.add(f'transform:translate({base[0]:.1f}px,{base[1]:.1f}px)', fr)

    def grow(self, t0, t1, t2, axis='X', poster=True):
        """t0~t1초 동안 왼쪽(위)부터 찬다, t2에 비운다"""
        o = '0 50%' if axis == 'X' else '0 0'
        return self.add(f'transform:scale{axis}({1 if poster else 0});transform-box:fill-box;transform-origin:{o}',
                        [(0, f'transform:scale{axis}(0)'), (t0, f'transform:scale{axis}(0)'), (t1, f'transform:scale{axis}(1)'),
                         (t2, f'transform:scale{axis}(1)'), (t2 + 0.01, f'transform:scale{axis}(0)'), (T, f'transform:scale{axis}(0)')])

    def style(self):
        return ('<style>' + ''.join(self.css) +
                '@media (prefers-reduced-motion:reduce){*{animation:none!important}}</style>')


def bars(g, x, y, widths, col, h=6, gap=12):
    for i, w in enumerate(widths):
        g.a(f'<rect x="{x:.1f}" y="{y + i * gap:.1f}" width="{w:.1f}" height="{h}" rx="{h/2}" fill="{col}"/>')


def ko(g, x, y, s, size, col, anchor='start', fw='400'):
    g.text(x, y, s, size, col, anchor, fw, font=SANS)


def doc(g, x, y, band, col, s=1.0):
    """문서 아이콘(귀 접힌 종이 + 형식 띠). 높이는 폭과 비슷하게 — 길쭉하면 답답했다(사용자 지적, 2026-09-30)"""
    w, h = 40 * s, 44 * s
    f = 11 * s
    g.a(f'<path d="M{x} {y+5*s:.1f} a{5*s:.1f} {5*s:.1f} 0 0 1 {5*s:.1f} {-5*s:.1f} h{w-f-5*s:.1f} l{f:.1f} {f:.1f} v{h-f-5*s:.1f} a{5*s:.1f} {5*s:.1f} 0 0 1 {-5*s:.1f} {5*s:.1f} h{-(w-10*s):.1f} a{5*s:.1f} {5*s:.1f} 0 0 1 {-5*s:.1f} {-5*s:.1f} z" '
        f'fill="{CARD}" stroke="{LINE}" stroke-width="2"/>')
    g.a(f'<path d="M{x+w-f:.1f} {y} v{f*0.7:.1f} a{3*s:.1f} {3*s:.1f} 0 0 0 {3*s:.1f} {3*s:.1f} h{f*0.7:.1f}" fill="none" stroke="{LINE}" stroke-width="2"/>')
    g.a(f'<rect x="{x-4*s:.1f}" y="{y+h*0.46:.1f}" width="{w*0.86:.1f}" height="{14*s:.1f}" rx="{4*s:.1f}" fill="{col}"/>')
    g.text(x - 4 * s + w * 0.43, y + h * 0.46 + 10.5 * s, band, 9 * s, '#ffffff', 'middle', '800', '.4')


def desk_icon(g, cx, y, band, col, name):
    """바탕화면 아이콘 = 문서 + 이름(한국어)"""
    doc(g, cx - 20, y, band, col)
    ko(g, cx, y + 64, name, 11.5, TEXT, 'middle')


def window(g, x, y, w, h):
    g.a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{CARD}" stroke="{LINE}" stroke-width="2"/>')
    g.a(f'<rect x="{x+16}" y="{y+13}" width="22" height="17" rx="4" fill="{RED}"/>')
    g.text(x + 27, y + 25, 'ZIP', 7.5, '#ffffff', 'middle', '800')
    ko(g, x + 46, y + 26, '이지집', 13, INK, fw='700')
    for i, d in enumerate(('M-5 0 h10', 'M-5 -5 h10 v10 h-10 z', 'M-5 -5 l10 10 M5 -5 l-10 10')):
        g.a(f'<path transform="translate({x+w-62+i*20} {y+22})" d="{d}" fill="none" stroke="{MUTED}" stroke-width="2" stroke-linecap="round"/>')
    # 툴바: 압축 열기 · 압축하기 · 압축 풀기 + 나머지
    for i, lab in enumerate(('열기', '압축', '풀기')):
        bx = x + 16 + i * 58
        g.a(f'<rect x="{bx}" y="{y+44}" width="50" height="40" rx="9" fill="{TILE}"/>')
        g.a(f'<rect x="{bx+17}" y="{y+50}" width="16" height="13" rx="3" fill="{RED}"/>')
        ko(g, bx + 25, y + 78, lab, 9.5, INK, 'middle')
    for i in range(3):
        g.a(f'<rect x="{x+196+i*30}" y="{y+52}" width="22" height="22" rx="6" fill="{TILE}"/>')
    g.a(f'<line x1="{x+16}" y1="{y+96}" x2="{x+w-16}" y2="{y+96}" stroke="{TILE}" stroke-width="2"/>')


def cursor(g):
    g.a(f'<path d="M0 0 v22 l6 -6 l5 11 l4 -2 l-5 -11 h8 z" fill="{TEXT}" stroke="{BG}" stroke-width="2" stroke-linejoin="round"/>')


def scene(g, A, L):
    """L: 캔버스별 배치. icons=(x, y0, 간격) · win=(x, y, w, h)"""
    ix, iy, gap = L['icons']
    WX, WY, WW, WH = L['win']
    icons = [('XLS', BLUE, '보고서.xlsx'), ('JPG', LAV, '사진.jpg'), ('PPT', MUTED, '발표.pptx')]
    pos = [(ix, iy + i * gap) for i in range(3)]

    # ── ① 우클릭 한 번에 압축 (0~6초)
    sel = A.vis(1.5, 4.0, 0.2)                                  # 고른 아이콘 바탕
    for cx, cy in pos:
        g.a(f'<rect class="{sel}" x="{cx-40}" y="{cy-8}" width="80" height="84" rx="10" fill="{BLUE}" fill-opacity=".22" stroke="{BLUE}" stroke-opacity=".6" stroke-width="1.5"/>')
    for (cx, cy), (band, col, name) in zip(pos, icons):
        desk_icon(g, cx, cy, band, col, name)
    rx0, ry0 = ix - 52, iy - 20                                 # 끌어 고르는 사각형
    g.a(f'<g class="{A.vis(0.8, 1.7, 0.1)}"><rect class="{A.grow(0.8, 1.5, 1.7, "X", False)}" x="{rx0}" y="{ry0}" width="104" height="{gap*2+100}" fill="{BLUE}" fill-opacity=".1" stroke="{BLUE}" stroke-width="1.5" stroke-dasharray="4 3"/></g>')
    MX, MY = ix + 58, iy + gap - 6                             # 윈도우 11 우클릭 메뉴
    g.a(f'<g class="{A.pop(1.9, 3.7, 0.25)}">')
    g.a(f'<rect x="{MX}" y="{MY}" width="232" height="178" rx="12" fill="{CARD}" stroke="{LINE}" stroke-width="2"/>')
    for i in range(5):                                          # 위 아이콘 줄(잘라내기·복사…)
        g.a(f'<rect x="{MX+16+i*42}" y="{MY+12}" width="26" height="22" rx="6" fill="{TILE}"/>')
    g.a(f'<line x1="{MX+12}" y1="{MY+44}" x2="{MX+220}" y2="{MY+44}" stroke="{TILE}" stroke-width="2"/>')
    rows = ['열기', '이지집으로 압축하기', '공유', '속성']
    for i, lab in enumerate(rows):
        ry = MY + 52 + i * 30
        if i == 1:
            g.a(f'<rect class="{A.vis(2.6, 3.7, 0.12)}" x="{MX+8}" y="{ry}" width="216" height="28" rx="7" fill="{RED}" fill-opacity=".16"/>')
            g.a(f'<rect x="{MX+18}" y="{ry+7}" width="16" height="14" rx="3" fill="{RED}"/>')
            ko(g, MX + 44, ry + 19, lab, 12.5, INK, fw='700')
        else:
            g.a(f'<rect x="{MX+18}" y="{ry+7}" width="16" height="14" rx="3" fill="{TILE}"/>')
            ko(g, MX + 44, ry + 19, lab, 12.5, INK)
    g.a('</g>')
    zx, zy = ix, iy + gap * 3                                  # 새로 생기는 보고서.zip
    g.a(f'<g class="{A.pop(4.1, 23.7, 0.45, poster=True)}">')
    desk_icon(g, zx, zy, 'ZIP', RED, '보고서.zip')
    g.a('</g>')

    # ── ②~④ 이지집 창 (6~23.7초)
    g.a(f'<g class="{A.vis(5.9, 23.7, 0.35, poster=True)}">')
    window(g, WX, WY, WW, WH)
    BX, BY, BW, BH = WX + 16, WY + 110, WW - 32, WH - 126     # 창 본문
    # 빈 창: 끌어 놓으라는 안내
    g.a(f'<g class="{A.vis(5.9, 7.9, 0.25)}">')
    g.a(f'<rect x="{BX}" y="{BY}" width="{BW}" height="{BH}" rx="12" fill="none" stroke="{TILE}" stroke-width="2" stroke-dasharray="7 6"/>')
    g.a(f'<circle cx="{BX+BW/2}" cy="{BY+BH/2-14}" r="18" fill="{TILE}"/><path d="M{BX+BW/2-8} {BY+BH/2-14} h16 M{BX+BW/2} {BY+BH/2-22} v16" stroke="{INK}" stroke-width="3" stroke-linecap="round"/>')
    ko(g, BX + BW / 2, BY + BH / 2 + 26, '압축 파일을 끌어 놓으세요', 12.5, MUTED, 'middle')
    g.a('</g>')
    # ② 두 칸: 압축 열기 · 압축 풀기
    ZW = (BW - 16) / 2
    g.a(f'<g class="{A.vis(7.8, 9.5, 0.2)}">')
    for i, lab in enumerate(('압축 열기', '압축 풀기')):
        zx0 = BX + i * (ZW + 16)
        on = i == 1
        g.a(f'<rect x="{zx0:.1f}" y="{BY}" width="{ZW:.1f}" height="{BH}" rx="12" fill="{RED if on else CARD}" fill-opacity="{0.13 if on else 1}" stroke="{RED}" stroke-width="2" stroke-dasharray="7 6"/>')
        ko(g, zx0 + ZW / 2, BY + BH / 2 + 5, lab, 14, RED if on else INK, 'middle', '700')
    g.a('</g>')
    # ③ 푸는 중 + 바이러스 검사
    PW, PH = min(330, BW - 40), 150
    PX, PY = BX + (BW - PW) / 2, BY + (BH - PH) / 2
    g.a(f'<g class="{A.vis(9.4, 15.1, 0.25)}">')
    g.a(f'<rect x="{BX}" y="{BY}" width="{BW}" height="{BH}" rx="12" fill="{INK}" opacity=".12"/>')
    g.a(f'<rect x="{PX}" y="{PY}" width="{PW}" height="{PH}" rx="14" fill="{CARD}" stroke="{LINE}" stroke-width="2"/>')
    ko(g, PX + 22, PY + 34, '압축 푸는 중', 13.5, INK, fw='700')
    g.a(f'<rect x="{PX+22}" y="{PY+50}" width="{PW-44}" height="10" rx="5" fill="{TILE}"/>')
    g.a(f'<rect class="{A.grow(9.7, 12.8, 15.1, "X", False)}" x="{PX+22}" y="{PY+50}" width="{PW-44}" height="10" rx="5" fill="{RED}"/>')
    sx, sy = PX + 22, PY + 84                                  # 방패
    g.a(f'<path d="M{sx+14} {sy} l13 5 v10 c0 9 -6 15 -13 18 c-7 -3 -13 -9 -13 -18 v-10 z" fill="{BLUE}"/>')
    g.a(f'<path class="{A.vis(13.0, 15.1, 0.2)}" d="M{sx+8} {sy+16} l4 4 l8 -8" fill="none" stroke="{CARD}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    g.a(f'<g class="{A.vis(9.7, 13.0, 0.2)}">')
    ko(g, sx + 40, sy + 21, '바이러스 검사 중', 12.5, INK)
    for i in range(3):
        fr = [(0, 'opacity:.2')]
        for k in range(6):
            t = 9.7 + k * 0.55 + i * 0.15
            fr += [(t, 'opacity:.2'), (t + 0.2, 'opacity:1'), (t + 0.4, 'opacity:.2')]
        fr.append((T, 'opacity:.2'))
        g.a(f'<circle class="{A.add("opacity:.2", fr)}" cx="{sx+146+i*10}" cy="{sy+17}" r="3" fill="{BLUE}"/>')
    g.a('</g>')
    g.a(f'<g class="{A.vis(13.0, 15.1, 0.2)}">'); ko(g, sx + 40, sy + 21, '악성코드 없음 · 안전', 12.5, BLUE, fw='700'); g.a('</g>')
    g.a('</g>')
    # ④ 풀린 파일 목록: 다른 프로그램(깨진 이름) → 이지집(바른 이름)
    g.a(f'<g class="{A.vis(15.0, 23.7, 0.3, poster=True)}">')
    TGX = BX
    g.a(f'<g class="{A.vis(15.0, 17.9, 0.25)}"><rect x="{TGX}" y="{BY}" width="178" height="28" rx="14" fill="{TILE}"/>')
    ko(g, TGX + 89, BY + 19, '다른 프로그램으로 풀면', 12, INK, 'middle', '700'); g.a('</g>')
    g.a(f'<g class="{A.vis(17.8, 23.7, 0.25, poster=True)}"><rect x="{TGX}" y="{BY}" width="150" height="28" rx="14" fill="{RED}"/>')
    ko(g, TGX + 75, BY + 19, '이지집으로 풀면', 12, '#ffffff', 'middle', '700'); g.a('</g>')
    hy = BY + 44
    ko(g, BX + 14, hy + 12, '이름', 11, MUTED)
    ko(g, BX + BW * 0.62, hy + 12, '크기', 11, MUTED)
    ko(g, BX + BW * 0.8, hy + 12, '형식', 11, MUTED)
    g.a(f'<line x1="{BX}" y1="{hy+22}" x2="{BX+BW}" y2="{hy+22}" stroke="{TILE}" stroke-width="2"/>')
    for i, (bad, good, band, col, size) in enumerate(FILES):
        ry = hy + 32 + i * ((BY + BH - hy - 40) / 3)
        doc(g, BX + 14, ry, band, col, 0.62)
        g.a(f'<g class="{A.vis(15.0, 18.0, 0.2)}">'); g.text(BX + 50, ry + 19, bad, 13, RED); g.a('</g>')
        g.a(f'<g class="{A.vis(17.8, 23.7, 0.2, poster=True)}">'); ko(g, BX + 50, ry + 19, good, 13.5, INK, fw='700'); g.a('</g>')
        g.text(BX + BW * 0.62, ry + 19, size, 12, MUTED)
        g.text(BX + BW * 0.8, ry + 19, band, 12, MUTED)
    # 바른 이름으로 바뀌는 순간 목록 위를 지나가는 빛줄기
    sweep = A.add('opacity:0', [(0, 'opacity:0;transform:translateX(0px)'), (17.5, 'opacity:0;transform:translateX(0px)'),
                                (17.6, 'opacity:1;transform:translateX(0px)'), (18.4, f'opacity:1;transform:translateX({BW-40:.0f}px)'),
                                (18.5, f'opacity:0;transform:translateX({BW-40:.0f}px)'), (T, 'opacity:0;transform:translateX(0px)')])
    g.a(f'<rect class="{sweep}" x="{BX}" y="{hy+26}" width="40" height="{BY+BH-hy-30:.0f}" rx="8" fill="{RED}" fill-opacity=".22"/>')
    g.a('</g>')
    g.a('</g>')

    # ② 끌리는 보고서.zip
    dz = (BX + ZW + 16 + ZW / 2 - 20, BY + BH / 2 - 30)       # 압축 풀기 칸 가운데
    ghost = A.move([(0, zx - 20, zy), (7.2, zx - 20, zy), (8.8, *dz), (T, *dz)], (zx - 20, zy))
    g.a(f'<g class="{A.vis(7.2, 9.3, 0.15)}"><g class="{ghost}" opacity=".9">')
    doc(g, 0, 0, 'ZIP', RED)
    g.a('</g></g>')

    # 커서
    rest = (WX + WW - 46, WY + WH - 40)           # 쉴 때는 창 오른쪽 아래 구석(목록을 가리지 않게)
    menu_row = (MX + 120, MY + 52 + 30 + 14)
    pts = [(0, *rest), (0.8, rx0, ry0), (1.5, rx0 + 104, ry0 + gap * 2 + 100), (1.9, ix + 10, iy + gap + 20),
           (2.6, *menu_row), (3.4, *menu_row), (4.4, zx + 30, zy + 70), (5.9, zx + 30, zy + 70),
           (6.8, zx + 4, zy + 26), (7.2, zx + 4, zy + 26), (8.8, dz[0] + 24, dz[1] + 30), (9.4, dz[0] + 24, dz[1] + 30),
           (10.2, *rest), (23.7, *rest), (T, *rest)]
    g.a(f'<g class="{A.move(pts, rest)}">')
    cursor(g)
    g.a('</g>')


def build(w, h, L):
    g = Svg(w, h)
    head, g.o = g.o, []          # 본문을 따로 모아 <style>을 앞에 넣는다
    A = Anim()
    scene(g, A, L)
    g.o = head + [A.style()] + g.o
    return g


out = sys.argv[1] if len(sys.argv) > 1 else '.'
# 데스크톱: 왼쪽 바탕화면 아이콘 줄 · 오른쪽 넓은 이지집 창(단계 표시 없이 폭 전체)
build(1200, 440, {'icons': (96, 22, 100), 'win': (330, 26, 820, 388)}).save(os.path.join(out, 'ezzip.svg'), LIGHT_ZZ)
# 카드·모바일(약 1.5:1)
build(668, 440, {'icons': (60, 22, 100), 'win': (150, 26, 494, 388)}).save(os.path.join(out, 'ezzip-m.svg'), LIGHT_ZZ)
