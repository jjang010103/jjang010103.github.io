# 프로젝트 이미지 공용 도구. 사용법과 규칙은 AGENTS.md "프로젝트 이미지 만들기"에 있다.
# 그릴 때는 사이트 다크 토큰 색(:root의 light-dark() 두 번째 값)만 쓴다. 저장할 때 LIGHT 표로 색을 바꿔
# 라이트 테마용 파일(<이름>-light.svg)을 한 벌 더 쓴다. 새 색이 필요하면 토큰에서 골라 LIGHT에도 짝을 적는다.
import math, re

BG, PANEL, LINE, INSET = '#1b1b1e', '#232327', '#2f2f35', '#2a2a2f'   # surface · 패널 · 선 · surface-inset
TEXT, BODY, MUTED = '#ecebe6', '#c4c4c8', '#9a9a9f'                  # text · body · muted
RED = '#f05a5f'                                                        # accent-line
LAV, BLUE = '#b9a3dc', '#6f95e0'                                       # ai-2 · ai-3
# 다크 색 → 같은 토큰의 라이트 값. #ffffff(accent-text)는 두 테마 공통이라 바꾸지 않는다
LIGHT = {BG: '#ffffff', PANEL: '#ecebe6', INSET: '#dcdad3', LINE: '#dcdad3',
         TEXT: '#17171a', BODY: '#3a3a3e', MUTED: '#5b5a55',
         RED: '#2a45c7', LAV: '#8f77b5', BLUE: '#1e50a2'}
MONO = "'SF Mono','Menlo','Consolas',monospace"
C, Sn = math.cos(math.radians(30)), math.sin(math.radians(30))
LEAD = 38  # 칩 지시선 길이. 모든 칩이 같다


class Svg:
    """바탕색 + 24px 점 격자를 깐 빈 캔버스"""
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

    def save(self, path, light=None):
        """path(다크)와 <path>-light.svg(라이트) 두 장을 쓴다. light = 이 그림만의 LIGHT 덮어쓰기"""
        svg = '\n'.join(self.o + ['</svg>'])
        open(path, 'w').write(svg)
        pal = {**LIGHT, **(light or {})}
        open(path[:-4] + '-light.svg', 'w').write(re.sub(r'#[0-9a-f]{6}', lambda m: pal.get(m.group(0), m.group(0)), svg))


def iso(p, S):
    """3D (x, y, z) → 등각 화면 좌표. +x는 오른쪽 아래, +y는 왼쪽 아래, +z는 위"""
    x, y, z = p
    return ((x - y) * C * S, (x + y) * Sn * S - z * S)


def lerp(a, b, t):
    return tuple(a[i] + (b[i] - a[i]) * t for i in range(3))


def fit(extents, box):
    """extents(S) → (x0,y0,x1,y1). box 안에 가장 크게 들어가는 S와 원점 이동량"""
    x0, y0, x1, y1 = box
    S = 10
    while True:
        e = extents(S + 0.5)
        if e[2] - e[0] > x1 - x0 or e[3] - e[1] > y1 - y0:
            break
        S += 0.5
    e = extents(S)
    return S, ((x0 + x1) - (e[0] + e[2])) / 2, ((y0 + y1) - (e[1] + e[3])) / 2


def chip_w(label):
    return 14 + 8.6 * len(label)


def chip_box(x, y, ang, label):
    """칩 알약의 가운데와 반폭·반높이(extents 계산용)"""
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    return x + LEAD * c + c * chip_w(label) / 2, y + LEAD * s + s * 12, chip_w(label) / 2, 12


def chip(g, x, y, ang, label, fill, fg):
    """점(x, y)에서 ang 방향(도, 0=오른쪽 90=아래)으로 LEAD만큼 선을 긋고 끝에 알약. 선이 알약 가장자리에 닿는다"""
    c, s = math.cos(math.radians(ang)), math.sin(math.radians(ang))
    ex, ey = x + LEAD * c, y + LEAD * s
    w = chip_w(label)
    cx, cy = ex + c * w / 2, ey + s * 12
    g.a(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{ex:.1f}" y2="{ey:.1f}" stroke="{MUTED}" stroke-width="1.2"/>')
    g.a(f'<rect x="{cx - w/2:.1f}" y="{cy - 12:.1f}" width="{w:.1f}" height="24" rx="12" fill="{fill}"/>')
    g.text(cx, cy + 4.5, label, 13, fg, 'middle', '600')


def compass(g, x, y):
    ex, ey = x + C * 36, y - Sn * 36
    g.a(f'<g stroke="{MUTED}" stroke-width="1.5" fill="none" opacity=".8" stroke-linecap="round">'
        f'<line x1="{x}" y1="{y}" x2="{ex:.1f}" y2="{ey:.1f}"/>'
        f'<path d="M{ex-9:.1f},{ey-2:.1f} L{ex:.1f},{ey:.1f} L{ex-5:.1f},{ey+8:.1f}"/></g>')
    g.text(ex + 8, ey - 4, 'N', 14, MUTED)


def panel(g, x, y, w, h, title):
    """둥근 패널 + 위 라벨(대문자 12px)"""
    g.a(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="{PANEL}"/>')
    g.text(x + 20, y + 32, title, 12, MUTED, ls='1.5')


def tabs(g, cx, y, items, on):
    """앱 보기 탭을 알약으로. items = [(글자, 폭), …], on = 켜진 칸 번호"""
    pad, gap = 6, 6
    tw = sum(w for _, w in items) + gap * (len(items) - 1) + pad * 2
    x = cx - tw / 2
    g.a(f'<rect x="{x:.1f}" y="{y}" width="{tw:.1f}" height="48" rx="24" fill="{PANEL}"/>')
    x += pad
    for i, (lab, w) in enumerate(items):
        if i == on:
            g.a(f'<rect x="{x:.1f}" y="{y+pad}" width="{w}" height="36" rx="18" fill="{TEXT}"/>')
        g.text(x + w / 2, y + 29, lab, 13, BG if i == on else MUTED, 'middle', '600')
        x += w + gap


def grid_block(g, x, y, w, h, rows, ratios):
    """도면 표제란 같은 두 줄 격자. rows = [[(라벨, 값, 값 색), …], …], ratios = 칸 폭 비율"""
    cw = [w * r for r in ratios]
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
