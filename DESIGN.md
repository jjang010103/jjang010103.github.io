---
name: 장민규 이력서
description: 한 가지 잉크로 이름·강조·타임라인·서명을 찍는 3개 국어 개발자 이력서
colors:
  paper: "light-dark(#fbfbf9,#101011)"
  text: "light-dark(#1c1b19,#d9d9db)"
  ink: "light-dark(#151514,#d9d9db)"
  ink-text: "light-dark(#fbfbf9,#101011)"
  ink-text-soft: "light-dark(#adadab,#545456)"
  card: "light-dark(#f1f1f0,#1c1c20)"
  card-hover: "light-dark(#eaeae9,#222227)"
  card-item: "light-dark(#fbfbf9,#292930)"
  hairline: "light-dark(#dcdbd5,#34343b)"
  hairline-soft: "light-dark(#e3e2dc,#2c2c33)"
  control-border: "light-dark(#8d8b84,#72727c)"
  muted: "light-dark(#5f5f59,#98989d)"
  muted-2: "light-dark(#6f6e68,#838388)"
  chip-text: "light-dark(#3f3f3a,#bebec2)"
  body: "light-dark(#2b2a27,#cbcbce)"
  sub: "light-dark(#45453f,#adadb1)"
  dot: "light-dark(#6f6f68,#9a9aa3)"
  stripe: "light-dark(#d3d1ca,#3c3c44)"
  ai-blue: "light-dark(#4f46e5,#a5b4fc)"
typography:
  display:
    fontFamily: "'Pretendard JP Variable', 'Pretendard Variable', Pretendard, system-ui, sans-serif"
    fontSize: "clamp(38px, 9vw, 86px)"
    fontWeight: 600
    lineHeight: 0.93
    letterSpacing: "-0.042em"
  headline:
    fontFamily: "'Pretendard JP Variable', 'Pretendard Variable', Pretendard, system-ui, sans-serif"
    fontSize: "30px"
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: "-0.032em"
  title:
    fontFamily: "'Pretendard JP Variable', 'Pretendard Variable', Pretendard, system-ui, sans-serif"
    fontSize: "22px"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "-0.028em"
  lead:
    fontFamily: "'Pretendard JP Variable', 'Pretendard Variable', Pretendard, system-ui, sans-serif"
    fontSize: "24px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "-0.018em"
  body:
    fontFamily: "'Pretendard JP Variable', 'Pretendard Variable', Pretendard, system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.72
    letterSpacing: "normal"
  stat:
    fontFamily: "'Pretendard JP Variable', 'Pretendard Variable', Pretendard, system-ui, sans-serif"
    fontSize: "30px"
    fontWeight: 600
    lineHeight: 1
    letterSpacing: "-0.035em"
  label:
    fontFamily: "'JetBrains Mono', ui-monospace, SFMono-Regular, monospace"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: "0.1em"
rounded:
  chip: "3px"
  control: "10px"
  stat: "12px"
  card: "14px"
  sheet: "24px"
  pill: "999px"
spacing:
  xs: "8px"
  sm: "12px"
  md: "16px"
  lg: "24px"
  xl: "36px"
  section-gap: "80px"
  page-bottom: "96px"
components:
  keyword-chip:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-text}"
    rounded: "{rounded.chip}"
    padding: "0.08em 0.28em 0.12em"
    typography: "{typography.body}"
  icon-button:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    rounded: "{rounded.control}"
    size: "32px"
  icon-button-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-text}"
  segment-on:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-text}"
    padding: "0 10px"
    height: "32px"
  segment-off:
    backgroundColor: "transparent"
    textColor: "{colors.muted}"
    padding: "0 10px"
    height: "32px"
  pill-core:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-text}"
    rounded: "{rounded.control}"
    padding: "5px 11px"
    typography: "{typography.label}"
  pill:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    rounded: "{rounded.control}"
    padding: "5px 11px"
    typography: "{typography.label}"
  project-card:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.text}"
    rounded: "{rounded.card}"
    padding: "24px 24px 22px"
  project-card-hover:
    backgroundColor: "{colors.card}"
  nav-pill:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.muted}"
    rounded: "999px"
    padding: "6px 8px"
  nav-chapter-on:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-text}"
    rounded: "999px"
    height: "30px"
  stat-card:
    backgroundColor: "{colors.card-item}"
    textColor: "{colors.text}"
    rounded: "{rounded.stat}"
    padding: "18px 20px 16px"
  sheet:
    backgroundColor: "{colors.card}"
    textColor: "{colors.text}"
    rounded: "{rounded.sheet}"
    padding: "22px 44px 40px"
    width: "min(720px, calc(100vw - 32px))"
---

# Design System: 장민규 이력서

## Overview

**Creative North Star: "한 가지 잉크 (One Ink)"**

이 페이지에는 액센트 색이 없다. 이름, 강조 키워드, 경력 타임라인, 푸터, 상단 pill의 활성 챕터가 전부 **같은 잉크의 반전 블록**이다. 잉크 하나가 "무엇이 중요한가"를 찍고, 나머지는 종이색 위의 회색 단계로 물러난다. 라이트와 다크는 이 잉크의 방향만 뒤집은 것이라 두 테마가 한 벌의 토큰(`light-dark()`)으로 성립한다.

어조는 에디토리얼하고 자신감 있고 조용하다. 86px 이름 블록과 넓은 여백이 잡지 편집 같은 첫인상을 만들지만, 그 아래는 근무 기간 비율로 그려진 타임라인 바, 데이터가 칸 수를 정하는 벤토 그리드, `metrics` 문장에서만 뽑은 수치 카드처럼 **장식이 아니라 계측이 형태를 정한다.** 1차 독자는 비개발자 인사담당자이고 2차 독자는 기술 면접관이라, 표면은 쉽고 세부는 정확해야 한다.

거부한 것: 그라디언트와 네온 액센트, 아이콘·사진이 가득한 카드 그리드, 이모지와 장식 아이콘. 아이콘은 1.4~1.8px 스트로크의 선 아이콘 몇 개(테마·프린터·닫기·복사·화살표)뿐이고, 외부 링크 표시 `↗`는 글리프로 쓴다.

**Key Characteristics:**
- 잉크 반전 하나가 강조·서명·현재 상태를 모두 맡는다. 유채색은 `ai-blue` 한 곳(모달 05 AI 섹션 번호와 불릿)뿐이다.
- 종이색 → 카드 → 카드 위 면의 세 단 톤 레이어링. 그림자는 열린 모달에만 있다.
- 본문은 Pretendard, 계측값(날짜·번호·라벨·스택 태그)은 JetBrains Mono. 모노스페이스는 데이터에만 쓴다.
- 모서리는 `corner-shape: squircle`을 지원하는 브라우저에서 스쿼클로 부드러워진다.
- 3개 국어가 같은 DOM에 살고 `html[lang]`으로만 보인다. 줄바꿈 규칙(`keep-all`)은 한국어에만 건다.

## Colors

거의 무채색 팔레트다. 라이트는 따뜻한 종이색 계열, 다크는 차가운 흑연 계열이며 한 토큰이 두 값을 모두 가진다.

### Primary
- **잉크 (ink)**: 반전 블록의 바탕. 이름(`.hero-name`), 강조 칩(`.kw`, `strong`), 타임라인 세그먼트, 푸터, pill의 활성 챕터·시트의 켜진 언어·핵심 스택 필. 라이트에선 거의 검정, 다크에선 밝은 회백색이라 "잉크"는 색이 아니라 **역할**이다.
- **잉크 글자 (ink-text)**: 잉크 위 글자. 종이색과 같다.
- **잉크 보조 글자 (ink-text-soft)**: 잉크 블록 안의 보조 정보(타임라인 날짜, 푸터 역할·전화·저작권). 불투명도가 아니라 색 토큰이다.

### Secondary
- **AI 블루 (ai-blue)**: 페이지에서 유일한 유채색. 프로젝트 모달 05 "AI 협업 경험" 섹션의 번호와 불릿 점에만 쓴다. 다른 곳에 쓰면 규칙이 깨진다.

### Neutral
- **종이 (paper)**: 페이지 배경. 모달 뒤도 블러가 아니라 이 색으로 불투명하게 덮는다.
- **글자 (text)**: 제목과 본문 최상위 글자.
- **본문 (body)** / **보조 본문 (sub)**: 불릿 항목 / 카드·모달 요약. 글자보다 한 단계 낮다.
- **카드 (card)** → **카드 호버 (card-hover)** → **카드 위 면 (card-item)**: 세 단 톤 레이어링. 카드 위 면은 라이트에서 종이색과 같고 다크에서 한 단계 밝다.
- **뮤트 (muted)** / **뮤트 2 (muted-2)**: 라벨·아이브로우·챕터 번호 / 연락처 행·모달 번호·서명 줄. 둘 다 **카드 위에서** 4.5:1을 넘긴다.
- **헤어라인 (hairline)** / **부드러운 헤어라인 (hairline-soft)** / **컨트롤 테두리 (control-border)**: 구분선 / 카드 테두리 / 버튼·세그먼트 테두리. 컨트롤 테두리는 카드 위 면에서도 3:1이다.
- **점 (dot)**, **줄무늬 (stripe)**, **칩 글자 (chip-text)**: 불릿 점, 타임라인 공백 빗금, 로고 글자.

### Named Rules
**The One Ink Rule.** 강조하고 싶으면 잉크로 반전한다. 새 액센트 색을 만들지 않는다. `ai-blue`는 예외가 아니라 "AI 섹션"이라는 한 자리의 이름표다.

**The Surface Contrast Rule.** 글자 토큰은 놓이는 면(종이가 아니라 카드·카드 위 면) 기준으로 4.5:1, 테두리·로고 잉크는 3:1을 지킨다. 토큰 값을 바꾸면 카드 위에서 다시 잰다.

**The No-JS-Color Rule.** 색은 시트에서만 온다. 활성 챕터·활성 언어는 `is-on` 클래스로 CSS가 칠하고, JS는 클래스 이름만 넘긴다. `dark ? '#…' : '#…'` 리터럴 쌍을 다시 만들지 않는다(2026-09-05에 전부 제거).

## Typography

**Display / Body Font:** Pretendard Variable (JP 서브셋 우선, system-ui 폴백)
**Label / Mono Font:** JetBrains Mono (ui-monospace 폴백)

**Character:** 하나의 산세리프가 86px 이름부터 16px 본문까지 웨이트 400·500·600만으로 위계를 만든다. 큰 글자는 자간을 강하게 조이고(-0.042em) 본문은 풀어 둔다. 모노스페이스는 "이건 계측값이다"라는 신호로만 등장한다.

### Hierarchy
- **Display** (600, clamp(38px, 9vw, 86px), 0.93): 히어로 이름. 잉크 블록 안에 인라인으로 앉는다. 일본어는 0.8em.
- **Headline** (600, 30px 챕터 제목 / 34px 모달 제목, 1.2): 챕터·모달 제목. 자간 -0.03em.
- **Title** (600, 22px, 1.25): 프로젝트 카드 제목. 모달 섹션 소제목은 20px.
- **Lead** (400, 24px, 1.5): 히어로 첫 문장. `text-wrap: pretty`.
- **Body** (400, 16px, 1.7~1.75): 경력 불릿·모달 본문. 색은 `body`. 항목 한 문장, 90자 이내.
- **Stat** (600, 30px, 1.0): 수치 카드 값. 자간 -0.035em.
- **Label** (400, 14px, 자간 0.1em, 모노): 아이브로우, 챕터 번호, 스택 라벨, 카드 상단 `회사 · 기간`. 영어는 대문자.
- **Card Stat** (600, 21px 일반 / 26px featured, 1.1, tabular-nums): 프로젝트 카드 위의 수치. 모달 수치 카드보다 한 단계 작다.
- **Micro** (11.5~13.5px, 모노): pill 챕터 번호(11.5px, 0.06em), PDF 버튼(12px), 타임라인 날짜(12.5px), 푸터 메타(12px), 카드 이미지 자리 캡션(11px).

### Named Rules
**The Mono Means Data Rule.** JetBrains Mono는 날짜, 번호, 라벨, 스택 태그, 연락처 값에만 쓴다. 문장에는 쓰지 않는다. 수치 카드 라벨은 영어일 때만 모노고 한글·일본어는 본문 서체다.

**The Language Owns Line Breaks Rule.** `word-break: keep-all`은 `html[lang="ko"] body` 한 곳에만 있다. 컴포넌트에 직접 쓰면 일본어 문장이 한 덩어리가 되어 넘친다. 안전망은 `body { overflow-wrap: break-word }`.

**The One Bold Rule.** 항목 하나에 잉크 칩(`**…**`)은 최대 하나. 전부 칠하면 강조가 사라진다.

## Layout

한 칼럼 페이지, 최대 폭 1100px, 좌우 여백 `clamp(18px, 4vw, 32px)`, 바닥 여백 96px. 히어로 아래 첫 챕터(경력)는 104px, 이후 챕터는 80px 위 여백으로 나뉜다. 챕터 머리는 `번호(모노) · 제목` 뒤에 1px 헤어라인(`[data-chaprule]`)이 끝까지 이어진다.

- **상단 바**: sticky(`top: -16px`라 붙으면 위 여백만 30 → 14px), 종이색. 왼쪽 이름, 오른쪽에 **플로팅 pill 하나**(`.ctl`: 챕터 5 · 구분선 · 언어 3 · 구분선 · 테마 · PDF). 챕터 칸은 40px 원형이고 활성 칸만 이름 폭만큼 늘어나 잉크가 채운다. 진행률 표시는 없다. 스크롤 위치는 활성 챕터 하나로만 보인다.
- **경력**: 실제 근무 기간 비율의 타임라인 바(`<ol>`, `flex: 0 0 calc(65.6% - 4px)` 등 인라인 예외 3개) 아래 회사 2열 그리드(gap 40px).
- **스택**: `repeat(auto-fit, minmax(240px, 1fr))` 그리드, 군마다 라벨 + 칩 랩.
- **프로젝트 벤토**: 4열 그리드(gap 16px). 카드는 `PROJECTS[].span / minH / imgW`가 `--span / --minh / --imgw`로 넘긴 값대로 2칸 또는 4칸, 최소 높이 170~250px. 카드 안은 `텍스트 | 이미지 칸` 2열이고 이미지 칸(190~400px)은 `img`가 없으면 빗금 + 캡션. 크기가 곧 중요도다(ezZip만 `featured`).
- **모달**: 폭 `min(720px, 100vw - 32px)`, 높이 `min(90vh, 1100px)`, 페이지 위에 종이색 불투명 오버레이. 헤더 왼쪽에 페이저(‹ `n / 6` ›).

**모바일(≤720px)**은 시트 하단의 `@media (max-width: 720px)` 블록 하나에서만 재정의한다. 상단 바가 사라지고(이름은 히어로가 대신, 챕터 내비 없음) 컨트롤 pill만 우하단 `position: fixed`(언어 3 · 테마 · PDF, 탭 타깃 44px, 그림자 2겹)로 남는다. 스크롤바는 숨기지 않는다(유일한 위치 표시). 경력·프로젝트·학력이 1열, 벤토 카드는 `텍스트 → 하단 전폭 이미지 스트립(88 / 112px)`으로 접히고, 스택은 `라벨 / 2열 항목` 스펙 표, 모달은 `92dvh` 바텀시트(헤더 컨트롤 36px)가 된다. 연락처·푸터 링크는 44px.

리듬은 8 · 12 · 16 · 24 · 36 · 44 · 56 · 80px. 형제 간격은 `gap`으로 잡고 요소별 마진을 쌓지 않는다.

## Elevation & Depth

평면이 기본이다. 깊이는 **종이 → 카드 → 카드 위 면** 세 단의 톤 레이어링과 헤어라인 테두리로만 낸다. 프로젝트 카드는 종이색 위에 헤어라인만 두르고 호버에 `card`로 한 단계 내려앉을 뿐 들어 올리지 않는다. 상단 pill도 종이색 + 헤어라인이라 페이지에 붙어 있다.

### Shadow Vocabulary
- **접지 그림자** (`0 4px 10px light-dark(rgba(0,0,0,.10), rgba(0,0,0,.62))`): 모달 카드의 모서리를 만드는 좁고 진한 층.
- **환경 그림자** (`0 24px 60px light-dark(rgba(0,0,0,.35), rgba(0,0,0,.44))`): 같은 모달의 넓고 옅은 층. 두 겹은 항상 함께 쓴다.

### Named Rules
**The Floating-Only Shadow Rule.** 그림자는 페이지 위로 **뜨는** 것에만 있다: 열린 모달, 그리고 모바일에서 본문 위를 떠다니는 우하단 컨트롤 pill. 둘 다 접지 + 환경 두 겹이다. 카드·버튼·칩은 호버에도 그림자를 얻지 않는다. 한 겹짜리 넓은 블러는 다크에서 얼룩으로 보이므로 쓰지 않는다.

## Shapes

부드럽고 촉감 있는 종이 단추. 모서리는 역할별로 나뉜다: 강조 칩 3px, 컨트롤(시트 세그먼트·아이콘 버튼·필·타임라인 세그먼트) 10px, 카드 위 수치 박스 12px, 프로젝트 카드 14px(벤토라 22px보다 낮춰 칸이 붙는다), 모달·푸터 20~24px, 그리고 상단 pill과 그 안의 챕터 칸·언어 원은 완전한 알약(999px / 50%). 지원 브라우저에서는 `corner-shape: squircle`이 10~24px 모서리에 걸려 원호가 아니라 스쿼클이 된다.

테두리는 1px 헤어라인이다. 프로젝트 카드·pill은 `hairline`, 시트·수치 카드는 `hairline-soft`, 컨트롤은 `control-border`. 잉크 반전 블록은 테두리가 없다. 빗금(`repeating-linear-gradient(135deg …)`)은 "여기 아직 없다"의 기호다: 타임라인 공백(3px 간격)과 비어 있는 카드 이미지 칸(8px 간격) 두 곳.

## Components

### Buttons
- **pill 컨트롤** (상단 바의 테마·PDF): 28px, 테두리·바탕 없음, 호버에 `card`. 테마는 16px SVG, PDF는 12px 모노 글자.
- **아이콘 버튼** (시트의 테마·닫기): 32×32px, 컨트롤 테두리 1px, 카드 위 면 바탕, 10px 스쿼클. 닫기 호버는 잉크 반전. 안의 SVG는 14~16px, 스트로크 1.4~1.8px.
- **페이저 버튼** (모달 ‹ ›): 아이콘 버튼과 같은 크기지만 **테두리와 바탕이 없다.** 호버에 `card-item`이 깔리고, 끝에 닿아 비활성이면 `control-border` 색으로 남는다.
- **복사 버튼** (연락처 옆): 22px 박스에 14px 글리프, 테두리 없음, 색 `muted-2`. 누르면 1.4초 체크 아이콘으로 바뀌고 `aria-live`가 읽는다.
- **텍스트 버튼** (로고): 배경 없음, `text` 색, 호버에 불투명도 .62. 모바일에서는 숨긴다.
- **포커스**: 전역 `:focus-visible { outline: 2px solid ink; outline-offset: 3px }`. 프로젝트 카드는 안의 제목 버튼이 포커스될 때 카드 테두리에 그린다.

### Chips
- **강조 칩** (`.kw`, `strong`): 잉크 반전, 3px 모서리, 패딩 `.08em .28em .12em`, 마진 0, 웨이트 600. 줄 넘김에서 `box-decoration-break: clone`.
- **스택 필** (`.pill`): 모노 13px, 패딩 5px 11px, 10px 스쿼클. 핵심 군은 잉크 반전(`pill-core`), 나머지는 컨트롤 테두리만. 모바일에서 일반 필은 테두리 없는 텍스트가 되지만 핵심 군의 반전은 남는다.
- **모달 태그** (`.tag`): 필과 같되 14px, 9px 모서리, 글자 `text`.

### Cards / Containers
- **프로젝트 카드(벤토)**: 바탕 `paper`, 테두리 `hairline` 1px, 14px 모서리. 안은 `텍스트 | 이미지 칸` 2열. 텍스트는 `아이브로우 / 제목(버튼) / 요약 / 수치 2~3개`, 패딩 24/24/22. 일반 카드의 수치는 값 21px + 라벨 13.5px의 평면 열이고, `featured`(ezZip)만 수치가 `card` 바탕 12px 박스 3장이다. 이미지 칸은 `img`가 있으면 `object-fit: cover`, 없으면 빗금 위에 `이미지 준비 중` 캡슐(11px 모노). 호버·포커스 안은 `card`, 모바일 누름은 `scale(.986)`.
- **수치 카드(모달)**: 바탕 `card-item`, 14px 스쿼클, 패딩 18/20/16, 값 30px 600 위에 라벨. 그리드 `repeat(auto-fit, minmax(160px, 1fr))`이라 2장·3장 모두 빈 칸 없이 찬다.
- **모달 시트**: 720px, 24px 스쿼클, 바탕 `card`, 두 겹 그림자, 패딩 22/44/40. 헤더에 페이저(테두리 없는 ‹ › + `n / 6`, 화살표 라벨에 이전·다음 프로젝트 이름) · 언어 세그먼트 · 테마 · 닫기. 좌우 화살표 키로도 넘긴다. 모바일은 바텀시트(위 모서리만 24px, 드래그 핸들, 아래로 90px 스와이프하면 닫힘, 아래 120px 페이드).
- **푸터**: 잉크 반전 블록, 20px 스쿼클, 패딩 48/44/26. 이름 · 역할 · 링크 / 연락처 2열.

### Inputs / Fields
없음. 폼이 없는 페이지다.

### Navigation (pill)
- **데스크톱**: 종이색 + 헤어라인의 알약 하나에 챕터 5 · 언어 3 · 테마 · PDF. 챕터는 30px 높이의 트랙 위에 `absolute`로 놓인 칸들이고, 활성 칸만 `번호 + 이름`으로 늘어나며(`COL 40 + 글자 수 × 13 + 14`) 잉크 알약이 그 칸을 채운다. 활성이 바뀌는 프레임에는 잉크가 두 칸의 합집합으로 늘었다가 200ms 뒤 목표 칸으로 수축한다(`cubic-bezier(.4, 0, .2, 1)`, `prefers-reduced-motion`이면 전환 없음). 비활성 칸은 `muted` 번호만, 호버에 `text`. 트랙 폭이 바뀌면 오른쪽 컨트롤이 함께 밀린다.
- **모바일**: 챕터 칸과 이름을 없애고 pill만 우하단에 고정한다(44px 타깃, 두 겹 그림자). 위치 표시는 브라우저 스크롤바가 맡는다.

### Language Control
- **pill 안(상단)**: 28px 원 세 개(`ㅎ / A / あ`), 켜진 것만 `card` 바탕 + 600 웨이트 + `ink` 글자. 테두리 없음.
- **시트 헤더**: 컨트롤 테두리 1px 안의 세그먼트. 켜진 버튼은 잉크 반전, 꺼진 버튼은 투명 바탕에 `muted`. 32px 높이(모바일 36px).
- 둘 다 `role="group"` + `aria-pressed`, 색은 `is-on` 클래스로만 정해진다.

### Timeline Bar (signature)
근무 기간 비율의 잉크 세그먼트 두 개와 3.1% 빗금 공백을 담은 `<ol aria-label="근무 기간">`. 세그먼트 안에 회사명(15px 500)과 모노 기간(12.5px, `ink-text-soft`). 10px 스쿼클, 높이 58px(모바일 44px, 날짜 숨김).

### Theme Toggle (signature)
누른 버튼 중심에서 원형으로 퍼지는 View Transition(340ms linear, `clip-path: circle()`). 다음 누름은 같은 지점으로 되감긴다. `prefers-reduced-motion`이면 즉시 전환. 전환 중 재클릭은 무시한다.

## Do's and Don'ts

### Do:
- **Do** 강조가 필요하면 잉크로 반전한다. 항목당 칩 하나.
- **Do** 새 색은 `:root` 토큰으로 먼저 만들고 `light-dark()` 한 줄에 두 테마를 담는다. `@supports not` 폴백 블록의 라이트 값도 같이 맞춘다.
- **Do** 글자 대비는 카드 위에서 4.5:1, 테두리는 3:1로 잰다.
- **Do** 정적 스타일은 시트에, 모바일 재정의는 하단 `@media (max-width: 720px)` 블록 하나에.
- **Do** 계측값(날짜·번호·태그·연락처)만 모노스페이스로.
- **Do** 뜨는 것(모달, 모바일 pill)에만 그림자를, 그것도 접지 + 환경 두 겹으로.
- **Do** 보이지 않는 라벨(`aria-label`, 라이브 리전)도 `T` 상수로 3개 국어.
- **Do** 레이아웃을 건드렸으면 3개 언어 × 모바일 × 인쇄 미리보기까지 본다.

### Don't:
- **Don't** 그라디언트·네온·두 번째 액센트 색을 넣지 않는다. `ai-blue`는 AI 섹션 이름표일 뿐이다.
- **Don't** 카드·버튼·칩에 그림자를 주지 않는다. 그림자는 모달 두 겹뿐이다.
- **Don't** 이모지나 장식 아이콘, 아이콘+제목+설명 카드 그리드를 만들지 않는다.
- **Don't** `!important`, 인라인 정적 `style=`, `:first-of-type` 같은 구조 의존 셀렉터를 쓰지 않는다.
- **Don't** `word-break: keep-all`을 컴포넌트에 직접 쓰지 않는다. 언어 셀렉터에만.
- **Don't** 반전 블록 안 보조 글자를 `opacity`로 만들지 않는다. `ink-text-soft`를 쓴다.
- **Don't** 카드의 이미지 칸을 텍스트로 메우지 않는다. `img`가 올 때까지 빗금 + 캡션이다.
- **Don't** 벤토의 칸 수·높이를 CSS에 박지 않는다. `PROJECTS[].span / minH / imgW`가 정하고 시트는 `--span / --minh / --imgw`를 소비만 한다.
