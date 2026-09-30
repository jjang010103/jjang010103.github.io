# ezZip 움직이는 이미지 생성기(공용 도구는 imgkit.py, 규칙은 AGENTS.md "프로젝트 이미지 만들기").
#   python3 img/gen_ezzip.py img  →  ezzip.svg(상세 데스크톱 1200×440) · ezzip-m.svg(카드·상세 모바일 668×440) + 라이트판
# 원본 참고: 이지랩 제품 소개 영상(27초) — 공유 → 원본 자동 삭제 → 끌어 놓아 압축 풀기.
# 파란 윈도우 바탕화면·형광 손글씨는 점 격자 바탕과 단계 알약으로 바꿨다. <img>로 넣어도 도는 CSS 애니메이션이다.
import os, sys
from imgkit import *

T = 18.0                                   # 한 바퀴(초). 장면마다 6초
CARD = '#f1f0ec'                           # 창 안 흰 면(다크 ink 값 → 라이트 흰색)
TILE, INK = '#d9d8d2', '#2c2c30'           # 창 안 옅은 칸 · 짙은 글자(두 테마 모두 밝은 면 위)
LIGHT_ZZ = {RED: '#b3242b', CARD: '#ffffff', TILE: '#ecebe6', INK: '#17171a'}
STEPS = [('01', 'SHARE'), ('02', 'AUTO DELETE'), ('03', 'EXTRACT')]


class Anim:
    """요소마다 @keyframes 하나. frames = [(초, 'css')] — 0초와 T초 값을 적어 한 바퀴가 이어지게 한다"""
    def __init__(self):
        self.css, self.n = [], 0

    def add(self, base, frames):
        self.n += 1
        name = f'a{self.n}'
        ks = ' '.join(f'{t / T * 100:.2f}%{{{css}}}' for t, css in frames)
        self.css.append(f'.{name}{{{base};animation:{name} {T}s linear infinite}}@keyframes {name}{{{ks}}}')
        return name

    def vis(self, t0, t1, f=0.3, poster=False):
        """t0~t1초에만 보인다(앞뒤 f초 페이드). poster=True면 움직임을 끈 사용자에게 보이는 정지 화면에 포함"""
        fr = [(0, 'opacity:0'), (max(t0, 0.01), 'opacity:0'), (t0 + f, 'opacity:1'), (t1 - f, 'opacity:1'), (t1, 'opacity:0'), (T, 'opacity:0')]
        if t0 == 0:
            fr = [(0, 'opacity:1'), (t1 - f, 'opacity:1'), (t1, 'opacity:0'), (T - f, 'opacity:0'), (T, 'opacity:1')]
        return self.add(f'opacity:{1 if poster else 0}', fr)

    def move(self, pts, base=None):
        """pts = [(초, x, y)] — 사이를 부드럽게 옮긴다"""
        fr = [(t, f'transform:translate({x}px,{y}px);animation-timing-function:ease-in-out') for t, x, y in pts]
        x, y = base or pts[0][1:]
        return self.add(f'transform:translate({x}px,{y}px)', fr)

    def fill(self, t0, t1):
        """진행 막대: t0~t1초 동안 왼쪽부터 찬다"""
        return self.add('transform:scaleX(1);transform-box:fill-box;transform-origin:0 50%',
                        [(0, 'transform:scaleX(0)'), (t0, 'transform:scaleX(0)'), (t1, 'transform:scaleX(1)'), (T, 'transform:scaleX(1)')])

    def style(self):
        return ('<style>' + ''.join(self.css) +
                '@media (prefers-reduced-motion:reduce){*{animation:none!important}}</style>')


def bars(g, x, y, widths, col, h=6, gap=12):
    for i, w in enumerate(widths):
        g.a(f'<rect x="{x:.1f}" y="{y + i * gap:.1f}" width="{w:.1f}" height="{h}" rx="{h/2}" fill="{col}"/>')


def file_icon(g, x, y, band, label, col):
    """바탕화면 파일 아이콘: 귀 접힌 종이 + 색 띠(형식) + 이름 막대"""
    g.a(f'<path d="M{x} {y+6} a6 6 0 0 1 6 -6 h26 l14 14 v42 a6 6 0 0 1 -6 6 h-34 a6 6 0 0 1 -6 -6 z" fill="{CARD}" stroke="{LINE}" stroke-width="2"/>')
    g.a(f'<path d="M{x+32} {y} v10 a4 4 0 0 0 4 4 h10" fill="none" stroke="{LINE}" stroke-width="2"/>')
    g.a(f'<rect x="{x-4}" y="{y+30}" width="40" height="16" rx="4" fill="{col}"/>')
    g.text(x + 16, y + 42, band, 10, '#ffffff', 'middle', '800', '.5')
    g.text(x + 23, y + 84, label, 11, TEXT, 'middle')


def window(g, x, y, w, h, title=True):
    g.a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{CARD}" stroke="{LINE}" stroke-width="2"/>')
    if title:
        g.a(f'<rect x="{x+16}" y="{y+14}" width="20" height="16" rx="4" fill="{RED}"/>')
        g.text(x + 26, y + 26, 'ZIP', 7, '#ffffff', 'middle', '800')
        g.text(x + 44, y + 27, 'ezZip', 13, INK, fw='700')
        for i, d in enumerate(('M-5 0 h10', 'M-5 -5 h10 v10 h-10 z', 'M-5 -5 l10 10 M5 -5 l-10 10')):
            g.a(f'<path transform="translate({x+w-62+i*20} {y+22})" d="{d}" fill="none" stroke="{MUTED}" stroke-width="2" stroke-linecap="round"/>')


def cursor(g):
    g.a(f'<path d="M0 0 v22 l6 -6 l5 11 l4 -2 l-5 -11 h8 z" fill="{TEXT}" stroke="{BG}" stroke-width="2" stroke-linejoin="round"/>')


def stage(g, A, ox, oy):
    """무대(데스크톱 아이콘 + 장면 셋 + 커서). 좌표는 668×440 기준, (ox, oy)만큼 옮겨 그린다"""
    g.a(f'<g transform="translate({ox} {oy})">')
    ZX, ZY = 34, 20                                          # 보고서.zip 아이콘
    file_icon(g, ZX, ZY, 'ZIP', 'REPORT.ZIP', RED)
    g.a(f'<g class="{A.vis(16.7, 17.8, 0.25)}">')             # 풀려 나온 보고서.xlsx
    file_icon(g, ZX, ZY + 110, 'XLS', 'REPORT.XLSX', BLUE)
    g.a('</g>')

    # ── 장면 1 SHARE: 우클릭 메뉴 → 공유 창 → 진행 막대
    MX, MY = 94, 40
    g.a(f'<g class="{A.vis(0.9, 2.3, 0.2)}">')
    g.a(f'<rect x="{MX}" y="{MY}" width="200" height="146" rx="12" fill="{CARD}" stroke="{LINE}" stroke-width="2"/>')
    for i in range(5):
        ry = MY + 10 + i * 26
        if i == 2:
            g.a(f'<rect x="{MX+8}" y="{ry}" width="184" height="24" rx="7" fill="{RED}" opacity=".16"/>')
            g.a(f'<rect x="{MX+16}" y="{ry+6}" width="12" height="12" rx="3" fill="{RED}"/>')
            g.text(MX + 36, ry + 16.5, 'SHARE TO DRIVE', 11, INK, fw='700')
        else:
            g.a(f'<rect x="{MX+16}" y="{ry+6}" width="12" height="12" rx="3" fill="{TILE}"/>')
            bars(g, MX + 36, ry + 9, [[110, 90, 0, 120, 80][i]], TILE, 6)
    g.a('</g>')
    DX, DY, DW = 164, 116, 360
    g.a(f'<g class="{A.vis(2.2, 5.8, 0.3, poster=True)}">')
    window(g, DX, DY, DW, 230, title=False)
    g.text(DX + DW / 2, DY + 32, 'SHARE', 13, INK, 'middle', '700', '1.5')
    g.a(f'<line x1="{DX+20}" y1="{DY+46}" x2="{DX+DW-20}" y2="{DY+46}" stroke="{TILE}" stroke-width="2"/>')
    icons = [('drive', BLUE), ('cloud', LAV), ('box', MUTED), ('mail', RED)]
    for i, (kind, col) in enumerate(icons):
        tx = DX + 30 + i * 78
        g.a(f'<rect x="{tx}" y="{DY+62}" width="64" height="64" rx="14" fill="{TILE}"' + (f' stroke="{INK}" stroke-width="2.5"' if i == 0 else '') + '/>')
        cx, cy = tx + 32, DY + 94
        if kind == 'drive':
            g.a(f'<path d="M{cx-4} {cy-14} h8 l14 24 l-4 7 h-28 l-4 -7 z" fill="{col}"/><path d="M{cx-18} {cy+10} l14 -24" stroke="{CARD}" stroke-width="3"/>')
        elif kind == 'cloud':
            g.a(f'<path d="M{cx-16} {cy+8} a8 8 0 0 1 2 -16 a11 11 0 0 1 21 -2 a8 8 0 0 1 9 18 z" fill="{col}"/>')
        elif kind == 'box':
            g.a(f'<path d="M{cx-14} {cy-10} l14 -6 l14 6 l-14 6 z M{cx-14} {cy-4} l14 6 l14 -6 v12 l-14 7 l-14 -7 z" fill="{col}"/>')
        else:
            g.a(f'<rect x="{cx-16}" y="{cy-11}" width="32" height="22" rx="4" fill="{col}"/><path d="M{cx-16} {cy-9} l16 11 l16 -11" fill="none" stroke="{CARD}" stroke-width="2.5"/>')
    g.a(f'<rect x="{DX+30}" y="{DY+156}" width="{DW-60}" height="14" rx="7" fill="{TILE}"/>')
    g.a(f'<rect class="{A.fill(3.0, 5.0)}" x="{DX+30}" y="{DY+156}" width="{DW-60}" height="14" rx="7" fill="{BLUE}"/>')
    g.a(f'<g class="{A.vis(5.0, 5.8, 0.2, poster=True)}"><circle cx="{DX+DW/2}" cy="{DY+200}" r="12" fill="{BLUE}"/>'
        f'<path d="M{DX+DW/2-6} {DY+200} l4 4 l8 -8" fill="none" stroke="{CARD}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></g>')
    g.a('</g>')

    # ── 장면 2 AUTO DELETE: 설정 창에서 보관 기간 드롭다운 7일 → 30일
    SX, SY, SW, SH = 130, 66, 480, 306
    g.a(f'<g class="{A.vis(6.0, 11.8)}">')
    window(g, SX, SY, SW, SH)
    bars(g, SX + 18, SY + 60, [80, 64, 88, 70, 76, 60], TILE, 10, 22)
    g.a(f'<rect x="{SX+124}" y="{SY+52}" width="{SW-142}" height="{SH-70}" rx="12" fill="{TILE}" opacity=".45"/>')
    g.a(f'<path d="M{SX+146} {SY+76} h18 M{SX+150} {SY+76} v16 a2 2 0 0 0 2 2 h8 a2 2 0 0 0 2 -2 v-16 M{SX+152} {SY+72} h6" fill="none" stroke="{RED}" stroke-width="2.5" stroke-linecap="round"/>')
    g.text(SX + 174, SY + 88, 'AUTO DELETE ORIGINAL', 13, INK, fw='700', ls='.5')
    g.text(SX + 146, SY + 128, 'KEEP FOR', 11, MUTED, ls='.5')
    DDX, DDY = SX + 146, SY + 140
    g.a(f'<rect x="{DDX}" y="{DDY}" width="150" height="34" rx="9" fill="{CARD}" stroke="{INK}" stroke-width="2"/>')
    g.a(f'<path d="M{DDX+126} {DDY+14} l6 6 l6 -6" fill="none" stroke="{INK}" stroke-width="2" stroke-linecap="round"/>')
    g.a(f'<g class="{A.vis(6.0, 9.7, 0.15)}">'); g.text(DDX + 16, DDY + 22, '7 DAYS', 13, INK, fw='700'); g.a('</g>')
    g.a(f'<g class="{A.vis(9.6, 11.8, 0.15)}">'); g.text(DDX + 16, DDY + 22, '30 DAYS', 13, RED, fw='700'); g.a('</g>')
    bars(g, DDX + 170, DDY + 14, [110], TILE, 7)
    g.a(f'<g class="{A.vis(8.0, 9.6, 0.15)}">')
    g.a(f'<rect x="{DDX}" y="{DDY+40}" width="150" height="142" rx="9" fill="{CARD}" stroke="{LINE}" stroke-width="2"/>')
    for i, d in enumerate(('7', '14', '30', '60', '180')):
        ry = DDY + 46 + i * 26
        if d == '30':
            g.a(f'<rect x="{DDX+6}" y="{ry}" width="138" height="24" rx="6" fill="{RED}" opacity=".16"/>')
        g.text(DDX + 16, ry + 16.5, f'{d} DAYS', 12, RED if d == '30' else INK, fw='700' if d == '30' else '400')
    g.a('</g>')
    g.a('</g>')

    # ── 장면 3 EXTRACT: 빈 창에 zip을 끌어 놓으면 두 칸(열기·풀기) → 풀기 진행 → 바탕화면에 xlsx
    WX, WY, WW, WH = 150, 60, 470, 316
    g.a(f'<g class="{A.vis(12.0, 17.4)}">')
    window(g, WX, WY, WW, WH)
    for i in range(8):
        g.a(f'<rect x="{WX+18+i*34}" y="{WY+48}" width="24" height="24" rx="6" fill="{RED if i < 2 else TILE}"/>')
    g.a(f'<line x1="{WX+16}" y1="{WY+84}" x2="{WX+WW-16}" y2="{WY+84}" stroke="{TILE}" stroke-width="2"/>')
    g.a(f'<g class="{A.vis(12.0, 13.4, 0.2)}"><circle cx="{WX+WW/2}" cy="{WY+210}" r="18" fill="{TILE}"/>'
        f'<path d="M{WX+WW/2-8} {WY+210} h16 M{WX+WW/2} {WY+202} v16" stroke="{INK}" stroke-width="3" stroke-linecap="round"/></g>')
    ZW = (WW - 48) / 2
    g.a(f'<g class="{A.vis(13.3, 15.1, 0.2)}">')
    for i, lab in enumerate(('OPEN', 'EXTRACT')):
        zx = WX + 16 + i * (ZW + 16)
        on = i == 1
        g.a(f'<rect x="{zx:.1f}" y="{WY+100}" width="{ZW:.1f}" height="{WH-118}" rx="12" fill="{RED if on else CARD}" fill-opacity="{0.12 if on else 1}" stroke="{RED}" stroke-width="2" stroke-dasharray="7 6"/>')
        g.text(zx + ZW / 2, WY + 100 + (WH - 118) / 2 + 5, lab, 13, RED if on else INK, 'middle', '700', '1')
    g.a('</g>')
    g.a(f'<g class="{A.vis(15.0, 16.8, 0.2)}">')
    g.a(f'<rect x="{WX}" y="{WY}" width="{WW}" height="{WH}" rx="14" fill="{INK}" opacity=".35"/>')
    PX, PY = WX + WW / 2 - 130, WY + 130
    g.a(f'<rect x="{PX}" y="{PY}" width="260" height="96" rx="12" fill="{CARD}" stroke="{LINE}" stroke-width="2"/>')
    g.text(PX + 20, PY + 32, 'EXTRACTING…', 13, INK, fw='700', ls='.5')
    g.a(f'<rect x="{PX+20}" y="{PY+52}" width="220" height="12" rx="6" fill="{TILE}"/>')
    g.a(f'<rect class="{A.fill(15.2, 16.5)}" x="{PX+20}" y="{PY+52}" width="220" height="12" rx="6" fill="{RED}"/>')
    g.a('</g>')
    g.a('</g>')

    # 끌리는 zip(장면 3): 커서와 함께 움직인다
    ghost = A.move([(0, ZX, ZY), (13.0, ZX, ZY), (14.4, 390, 250), (T, 390, 250)])
    g.a(f'<g class="{A.vis(13.0, 14.6, 0.15)}"><g class="{ghost}" opacity=".85">')
    file_icon(g, 0, 0, 'ZIP', '', RED)
    g.a('</g></g>')

    # 커서
    c0 = (330, 330)
    zx, zy = ZX + 24, ZY + 34
    pts = [(0, *c0), (0.8, zx, zy), (1.4, zx, zy), (1.9, MX + 110, MY + 74), (2.3, MX + 110, MY + 74), (2.9, DX + 62, DY + 96),
           (5.8, DX + 62, DY + 96), (6.6, DDX + 100, DDY + 18), (8.0, DDX + 100, DDY + 18), (8.9, DDX + 60, DDY + 104),
           (9.6, DDX + 60, DDY + 104), (11.8, 520, 340), (12.8, zx, zy), (13.0, zx, zy), (14.4, 420, 280), (16.8, 420, 280), (T, *c0)]
    g.a(f'<g class="{A.move(pts, (DX + 62, DY + 96))}">')
    cursor(g)
    g.a('</g>')
    g.a('</g>')


def pills_row(g, A, cx, y):
    """단계 알약(가로): 지금 장면의 알약이 켜진다"""
    ws = [26 + 8.2 * len(f'{n} {t}') for n, t in STEPS]
    x = cx - (sum(ws) + 8 * 2) / 2
    for i, ((n, t), w) in enumerate(zip(STEPS, ws)):
        g.a(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="30" rx="15" fill="{PANEL}" stroke="{LINE}" stroke-width="1.5"/>')
        g.text(x + w / 2, y + 19.5, f'{n} {t}', 11, MUTED, 'middle', '700', '.5')
        g.a(f'<g class="{A.vis(i * 6, i * 6 + 6, 0.25, poster=i == 0)}">')
        g.a(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="30" rx="15" fill="{TEXT}"/>')
        g.text(x + w / 2, y + 19.5, f'{n} {t}', 11, BG, 'middle', '700', '.5')
        g.a('</g>')
        x += w + 8


def steps_col(g, A, x, y):
    """단계 목록(세로, 데스크톱): 번호 · 이름 · 짧은 설명. 지금 장면이 켜지고 진행 막대가 찬다"""
    desc = ['Send a zip straight to cloud drives', 'Originals delete themselves on schedule', 'Drop a zip in, get the files out']
    for i, ((n, t), d) in enumerate(zip(STEPS, desc)):
        ty = y + i * 118
        g.a(f'<rect x="{x}" y="{ty}" width="340" height="100" rx="20" fill="{PANEL}" stroke="{LINE}" stroke-width="1.5"/>')
        g.a(f'<g class="{A.vis(i * 6, i * 6 + 6, 0.3, poster=i == 0)}"><rect x="{x}" y="{ty}" width="340" height="100" rx="20" fill="{INSET}" stroke="{RED}" stroke-width="2"/></g>')
        g.text(x + 22, ty + 42, n, 26, RED, fw='800')
        g.text(x + 72, ty + 36, t, 14, TEXT, fw='700', ls='1')
        g.text(x + 72, ty + 58, d, 11, MUTED)
        g.a(f'<rect x="{x+22}" y="{ty+76}" width="296" height="5" rx="2.5" fill="{LINE}"/>')
        g.a(f'<rect class="{A.add("transform:scaleX(0);transform-box:fill-box;transform-origin:0 50%", [(0, "transform:scaleX(0)"), (i * 6, "transform:scaleX(0)"), (i * 6 + 6, "transform:scaleX(1)"), (i * 6 + 6.01, "transform:scaleX(0)"), (T, "transform:scaleX(0)")])}" '
            f'x="{x+22}" y="{ty+76}" width="296" height="5" rx="2.5" fill="{RED}"/>')


def build(w, h, wide):
    g = Svg(w, h)
    A = Anim()
    body = []
    g.o, head = [], g.o          # 본문을 따로 모아 <style>을 앞에 넣는다
    if wide:
        steps_col(g, A, 50, 43)
        stage(g, A, 440, 22)
    else:
        pills_row(g, A, w / 2, 16)
        stage(g, A, 0, 34)
    body = g.o
    g.o = head + [A.style()] + body
    return g


out = sys.argv[1] if len(sys.argv) > 1 else '.'
build(1200, 440, True).save(os.path.join(out, 'ezzip.svg'), LIGHT_ZZ)
build(668, 440, False).save(os.path.join(out, 'ezzip-m.svg'), LIGHT_ZZ)
