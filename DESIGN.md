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
  stat: "14px"
  card: "22px"
  sheet: "24px"
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
    backgroundColor: "{colors.card}"
    textColor: "{colors.text}"
    rounded: "{rounded.card}"
    padding: "24px 24px 0"
  project-card-hover:
    backgroundColor: "{colors.card-hover}"
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

이 페이지에는 액센트 색이 없다. 이름, 강조 키워드, 경력 타임라인, 푸터, 켜진 세그먼트가 전부 **같은 잉크의 반전 블록**이다. 잉크 하나가 "무엇이 중요한가"를 찍고, 나머지는 종이색 위의 회색 단계로 물러난다. 라이트와 다크는 이 잉크의 방향만 뒤집은 것이라 두 테마가 한 벌의 토큰(`light-dark()`)으로 성립한다.

어조는 에디토리얼하고 자신감 있고 조용하다. 86px 이름 블록과 넓은 여백이 잡지 편집 같은 첫인상을 만들지만, 그 아래는 근무 기간 비율로 그려진 타임라인 바, 챕터 높이로 폭을 나누는 내비 게이지, `metrics` 문장에서만 뽑은 수치 카드처럼 **장식이 아니라 계측이 형태를 정한다.** 1차 독자는 비개발자 인사담당자이고 2차 독자는 기술 면접관이라, 표면은 쉽고 세부는 정확해야 한다.

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
- **잉크 (ink)**: 반전 블록의 바탕. 이름(`.hero-name`), 강조 칩(`.kw`, `strong`), 타임라인 세그먼트, 푸터, 켜진 세그먼트·핵심 스택 필. 라이트에선 거의 검정, 다크에선 밝은 회백색이라 "잉크"는 색이 아니라 **역할**이다.
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

**The Chrome Exception.** 상단 바 크롬(내비 라벨 색, 언어 세그먼트, 모바일 로고 채움)은 JS가 인라인으로 칠하므로 `light-dark()`를 못 쓰고 `dark ? '#…' : '#…'` 쌍으로 있다. 팔레트를 바꾸면 시트와 그 쌍을 함께 고친다.

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
- **Micro** (12~13.5px, 모노): 내비 번호(11.5px, 0.08em), 타임라인 날짜(12.5px), 푸터 메타(12px).

### Named Rules
**The Mono Means Data Rule.** JetBrains Mono는 날짜, 번호, 라벨, 스택 태그, 연락처 값에만 쓴다. 문장에는 쓰지 않는다. 수치 카드 라벨은 영어일 때만 모노고 한글·일본어는 본문 서체다.

**The Language Owns Line Breaks Rule.** `word-break: keep-all`은 `html[lang="ko"] body` 한 곳에만 있다. 컴포넌트에 직접 쓰면 일본어 문장이 한 덩어리가 되어 넘친다. 안전망은 `body { overflow-wrap: break-word }`.

**The One Bold Rule.** 항목 하나에 잉크 칩(`**…**`)은 최대 하나. 전부 칠하면 강조가 사라진다.

## Layout

한 칼럼 페이지, 최대 폭 1100px, 좌우 여백 `clamp(18px, 4vw, 32px)`, 바닥 여백 96px. 챕터는 위쪽 80px 여백으로 나뉘고 구분선은 없다. 챕터 머리는 `번호(모노) · 제목` 한 줄이고 그 옆 `[data-chaprule]`은 데스크톱에서 투명하다.

- **상단 바**: sticky, 종이색. 로고 · 내비(챕터 실측 높이 비례로 폭을 나눈 게이지 5개) · 언어 세그먼트 · 테마 · PDF. 게이지 채움이 읽기 진행률이다.
- **경력**: 실제 근무 기간 비율의 타임라인 바(`flex: 0 0 calc(65.6% - 4px)` 등, 인라인 예외 3개) 아래 회사 2열 그리드(gap 40px).
- **스택**: `repeat(auto-fit, minmax(240px, 1fr))` 그리드, 군마다 라벨 + 칩 랩.
- **프로젝트**: 3열 카드 그리드(gap 16px), 카드 비율 3:4. 카드 아랫면은 이미지 자리라 비워 둔다.
- **모달**: 폭 `min(720px, 100vw - 32px)`, 높이 `min(90vh, 1100px)`, 페이지 위에 종이색 불투명 오버레이.

**모바일(≤720px)**은 시트 하단의 `@media (max-width: 720px)` 블록 하나에서만 재정의한다. 내비는 바의 둘째 줄 스트립이 되고(바 약 100px), 챕터 제목 옆에 헤어라인이 켜지며(사용자 결정), 경력·프로젝트·학력이 1열, 스택이 `라벨 / 2열 항목` 스펙 표가 되고, 모달은 `92dvh` 바텀시트가 된다. 손가락 타깃은 연락처·푸터 링크 44px, 상단 바·시트 헤더 컨트롤 36px.

리듬은 8 · 12 · 16 · 24 · 36 · 44 · 56 · 80px. 형제 간격은 `gap`으로 잡고 요소별 마진을 쌓지 않는다.

## Elevation & Depth

평면이 기본이다. 깊이는 **종이 → 카드 → 카드 위 면** 세 단의 톤 레이어링과 헤어라인 테두리로만 낸다. 호버는 면 색을 한 단계 바꿀 뿐(`card` → `card-hover`) 들어 올리지 않는다.

### Shadow Vocabulary
- **접지 그림자** (`0 4px 10px light-dark(rgba(0,0,0,.10), rgba(0,0,0,.62))`): 모달 카드의 모서리를 만드는 좁고 진한 층.
- **환경 그림자** (`0 24px 60px light-dark(rgba(0,0,0,.35), rgba(0,0,0,.44))`): 같은 모달의 넓고 옅은 층. 두 겹은 항상 함께 쓴다.

### Named Rules
**The Modal-Only Shadow Rule.** 그림자는 페이지 위로 뜨는 모달 하나에만 있다. 카드·버튼·칩은 호버에도 그림자를 얻지 않는다. 한 겹짜리 넓은 블러는 다크에서 얼룩으로 보이므로 쓰지 않는다.

## Shapes

부드럽고 촉감 있는 종이 단추. 모서리는 역할별 다섯 단계다: 강조 칩 3px, 컨트롤(세그먼트·아이콘 버튼·필·타임라인 세그먼트) 10px, 수치 카드 14px, 프로젝트 카드 22px, 모달·푸터 20~24px. 지원 브라우저에서는 `corner-shape: squircle`이 모든 컨트롤과 카드에 걸려 원호가 아니라 스쿼클이 된다.

테두리는 1px 헤어라인이다. 카드는 `hairline-soft`, 컨트롤은 `control-border`. 잉크 반전 블록은 테두리가 없다. 타임라인 공백은 `repeating-linear-gradient(135deg …)` 3px 빗금으로 "여기 아무것도 없었다"를 정직하게 그린다.

## Components

### Buttons
- **아이콘 버튼** (테마·PDF·닫기): 32×32px, 컨트롤 테두리 1px, 투명 바탕, 10px 스쿼클. 호버·닫기 호버는 잉크 반전(바탕 `ink`, 글자 `ink-text`, 테두리 투명). 안의 SVG는 16px, 스트로크 1.4~1.8px.
- **페이저 버튼** (모달 ‹ ›): 아이콘 버튼과 같은 크기지만 **테두리와 바탕이 없다.** 호버에 `card-item`이 깔리고, 끝에 닿아 비활성이면 `control-border` 색으로 남는다.
- **복사 버튼** (연락처 옆): 22px 박스에 14px 글리프, 테두리 없음, 색 `muted-2`. 누르면 1.4초 체크 아이콘으로 바뀌고 `aria-live`가 읽는다.
- **텍스트 버튼** (내비·로고): 배경 없음. 내비는 `번호 + 라벨` 위에 2px 게이지 레일.
- **포커스**: 전역 `:focus-visible { outline: 2px solid ink; outline-offset: 3px }`. 프로젝트 카드는 안의 제목 버튼이 포커스될 때 카드 테두리에 그린다.

### Chips
- **강조 칩** (`.kw`, `strong`): 잉크 반전, 3px 모서리, 패딩 `.08em .28em .12em`, 마진 0, 웨이트 600. 줄 넘김에서 `box-decoration-break: clone`.
- **스택 필** (`.pill`): 모노 13px, 패딩 5px 11px, 10px 스쿼클. 핵심 군은 잉크 반전(`pill-core`), 나머지는 컨트롤 테두리만. 모바일에서 일반 필은 테두리 없는 텍스트가 되지만 핵심 군의 반전은 남는다.
- **모달 태그** (`.tag`): 필과 같되 14px, 9px 모서리, 글자 `text`.

### Cards / Containers
- **프로젝트 카드**: 3:4 비율, 22px 스쿼클, 바탕 `card`, 테두리 `hairline-soft` 1px. 위쪽에 `아이브로우 / 제목 / 요약`이 절대 배치되고 아랫면은 이미지 자리. 호버·포커스 안은 `card-hover`, 모바일 누름은 `scale(.986)`.
- **수치 카드**: 바탕 `card-item`, 14px 스쿼클, 패딩 18/20/16, 값 30px 600 위에 라벨. 그리드 `repeat(auto-fit, minmax(160px, 1fr))`이라 2장·3장 모두 빈 칸 없이 찬다.
- **모달 시트**: 720px, 24px 스쿼클, 바탕 `card`, 두 겹 그림자, 패딩 22/44/40. 헤더에 페이저 · 언어 세그먼트 · 테마 · 닫기. 모바일은 바텀시트(위 모서리만 24px, 드래그 핸들, 아래 120px 페이드).
- **푸터**: 잉크 반전 블록, 20px 스쿼클, 패딩 48/44/26. 이름 · 역할 · 링크 / 연락처 2열.

### Inputs / Fields
없음. 폼이 없는 페이지다.

### Navigation
- **데스크톱**: 챕터 5개, 각 버튼은 `모노 번호 + 라벨` 위에 2px 레일. 폭은 챕터 실측 높이의 0.55제곱 비례, 채움은 현재 챕터의 읽기 진행률. 활성 라벨 600, 나머지 400.
- **모바일**: 같은 컴포넌트가 바의 둘째 줄 스트립으로 내려온다. 로고 글자 자체가 `background-clip: text` 그라디언트로 페이지 진행률을 채운다(유일한 그라디언트, 잉크 두 단계 사이).

### Segmented Control (언어)
`ㅎ / A / あ` 세 버튼이 컨트롤 테두리 1px 안에 있다. 켜진 버튼은 잉크 반전, 꺼진 버튼은 투명 바탕에 `muted` 글자. 32px 높이(모바일 36px). `role="group"` + `aria-pressed`.

### Timeline Bar (signature)
근무 기간 비율의 잉크 세그먼트 두 개와 3.1% 빗금 공백. 세그먼트 안에 회사명(15px 500)과 모노 기간(12.5px, `ink-text-soft`). 10px 스쿼클, 높이 58px(모바일 44px, 날짜 숨김).

### Theme Toggle (signature)
누른 버튼 중심에서 원형으로 퍼지는 View Transition(340ms linear, `clip-path: circle()`). 다음 누름은 같은 지점으로 되감긴다. `prefers-reduced-motion`이면 즉시 전환. 전환 중 재클릭은 무시한다.

## Do's and Don'ts

### Do:
- **Do** 강조가 필요하면 잉크로 반전한다. 항목당 칩 하나.
- **Do** 새 색은 `:root` 토큰으로 먼저 만들고 `light-dark()` 한 줄에 두 테마를 담는다. `@supports not` 폴백 블록의 라이트 값도 같이 맞춘다.
- **Do** 글자 대비는 카드 위에서 4.5:1, 테두리는 3:1로 잰다.
- **Do** 정적 스타일은 시트에, 모바일 재정의는 하단 `@media (max-width: 720px)` 블록 하나에.
- **Do** 계측값(날짜·번호·태그·연락처)만 모노스페이스로.
- **Do** 보이지 않는 라벨(`aria-label`, 라이브 리전)도 `T` 상수로 3개 국어.
- **Do** 레이아웃을 건드렸으면 3개 언어 × 모바일 × 인쇄 미리보기까지 본다.

### Don't:
- **Don't** 그라디언트·네온·두 번째 액센트 색을 넣지 않는다. `ai-blue`는 AI 섹션 이름표일 뿐이다.
- **Don't** 카드·버튼·칩에 그림자를 주지 않는다. 그림자는 모달 두 겹뿐이다.
- **Don't** 이모지나 장식 아이콘, 아이콘+제목+설명 카드 그리드를 만들지 않는다.
- **Don't** `!important`, 인라인 정적 `style=`, `:first-of-type` 같은 구조 의존 셀렉터를 쓰지 않는다.
- **Don't** `word-break: keep-all`을 컴포넌트에 직접 쓰지 않는다. 언어 셀렉터에만.
- **Don't** 반전 블록 안 보조 글자를 `opacity`로 만들지 않는다. `ink-text-soft`를 쓴다.
- **Don't** 프로젝트 카드 아랫면을 텍스트로 메우지 않는다. 이미지 자리다.
