---
name: 장민규 이력서
description: 흰 카드와 파란 액센트 한 장으로 챕터를 벤토처럼 짜는 3개 국어 개발자 포트폴리오
colors:
  canvas: "light-dark(#ecebe6,#121214)"
  surface: "light-dark(#ffffff,#1d1d21)"
  surface-inset: "light-dark(#ecebe6,#2a2a2f)"
  media: "light-dark(#d9d7cf,#2f2f35)"
  hairline: "light-dark(#dcdad3,#2f2f35)"
  glass: "color-mix(in srgb, surface 72%, transparent)"
  text: "light-dark(#17171a,#ecebe6)"
  body: "light-dark(#3a3a3e,#c4c4c8)"
  muted: "light-dark(#5b5a55,#9a9a9f)"
  ink: "light-dark(#17171a,#f1f0ec)"
  ink-text: "light-dark(#ffffff,#17171a)"
  ink-text-soft: "light-dark(#b3b2ab,#5b5a55)"
  ink-inset: "light-dark(#2c2c30,#d9d8d2)"
  accent: "light-dark(#2a45c7,#b3242b)"
  accent-text: "#ffffff"
  accent-line: "light-dark(#2a45c7,#f05a5f)"
typography:
  display:
    fontFamily: "'Noto Sans KR', 'Noto Sans JP', system-ui, sans-serif"
    fontSize: "68px"
    fontWeight: 900
    lineHeight: 1.1
    letterSpacing: "-0.03em"
  display-detail:
    fontFamily: "'Noto Sans KR', 'Noto Sans JP', system-ui, sans-serif"
    fontSize: "60px"
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: "-0.03em"
  headline:
    fontFamily: "'Noto Sans KR', 'Noto Sans JP', system-ui, sans-serif"
    fontSize: "48px"
    fontWeight: 900
    lineHeight: 1.2
    letterSpacing: "-0.02em"
  lead:
    fontFamily: "'Noto Sans KR', 'Noto Sans JP', system-ui, sans-serif"
    fontSize: "26px"
    fontWeight: 700
    lineHeight: 1.45
    letterSpacing: "-0.01em"
  title-lg:
    fontFamily: "'Noto Sans KR', 'Noto Sans JP', system-ui, sans-serif"
    fontSize: "32px"
    fontWeight: 900
    lineHeight: 1.25
    letterSpacing: "-0.02em"
  title:
    fontFamily: "'Noto Sans KR', 'Noto Sans JP', system-ui, sans-serif"
    fontSize: "28px"
    fontWeight: 700
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  title-sm:
    fontFamily: "'Noto Sans KR', 'Noto Sans JP', system-ui, sans-serif"
    fontSize: "24px"
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: "-0.01em"
  body:
    fontFamily: "'Noto Sans KR', 'Noto Sans JP', system-ui, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.7
    letterSpacing: "normal"
  stat:
    fontFamily: "'Space Grotesk', system-ui, sans-serif"
    fontSize: "88px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.02em"
  stat-detail:
    fontFamily: "'Space Grotesk', 'Noto Sans KR', system-ui, sans-serif"
    fontSize: "64px"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "-0.02em"
  mail:
    fontFamily: "'Space Grotesk', system-ui, sans-serif"
    fontSize: "34px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "-0.01em"
  label:
    fontFamily: "'Noto Sans KR', 'Noto Sans JP', system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "normal"
rounded:
  media: "18px"
  card: "28px"
  card-mobile: "22px"
  pill: "999px"
spacing:
  xs: "6px"
  sm: "10px"
  md: "16px"
  lg: "24px"
  xl: "32px"
  xxl: "48px"
  section-gap: "64px"
components:
  nav-bar:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    padding: "12px 12px 12px 28px"
  nav-pill-mobile:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "26px"
    padding: "6px"
  nav-item-on:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-text}"
    rounded: "{rounded.pill}"
    height: "44px"
    padding: "0 20px"
  nav-item-off:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    rounded: "{rounded.pill}"
    height: "44px"
    padding: "0 20px"
  icon-button:
    backgroundColor: "transparent"
    textColor: "{colors.text}"
    rounded: "{rounded.pill}"
    size: "40px"
  icon-button-hover:
    backgroundColor: "{colors.surface-inset}"
  icon-button-on:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-text}"
  hero-card:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-text}"
    rounded: "{rounded.card}"
    padding: "48px"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.card}"
    padding: "32px"
  ink-card:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-text}"
    rounded: "{rounded.card}"
    padding: "32px"
  media-card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.card}"
    padding: "16px"
  media:
    backgroundColor: "{colors.media}"
    textColor: "{colors.muted}"
    rounded: "{rounded.media}"
  stack-chip:
    backgroundColor: "{colors.surface-inset}"
    textColor: "{colors.text}"
    rounded: "{rounded.pill}"
    padding: "4px 12px"
  tag:
    backgroundColor: "{colors.surface-inset}"
    textColor: "{colors.text}"
    rounded: "{rounded.pill}"
    padding: "6px 12px"
  tag-on-ink:
    backgroundColor: "{colors.ink-inset}"
    textColor: "{colors.ink-text}"
    rounded: "{rounded.pill}"
    padding: "6px 12px"
  status-badge:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-text}"
    rounded: "{rounded.pill}"
    padding: "6px 12px"
  ink-pill:
    backgroundColor: "{colors.ink-inset}"
    textColor: "{colors.ink-text}"
    rounded: "{rounded.pill}"
    height: "44px"
    padding: "0 20px"
  copy-button:
    backgroundColor: "transparent"
    textColor: "{colors.ink-text-soft}"
    rounded: "{rounded.pill}"
    size: "44px"
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-text}"
    rounded: "{rounded.card}"
    padding: "48px"
  back-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.pill}"
    height: "44px"
    padding: "0 22px 0 18px"
  pager-button:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.pill}"
    size: "44px"
  detail-hero:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.accent-text}"
    rounded: "{rounded.card}"
    padding: "48px"
  detail-stat:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text}"
    rounded: "{rounded.card}"
    padding: "32px"
    typography: "{typography.stat-detail}"
---

# Design System: 장민규 이력서

> **2026-09-25 전면 개정.** 디자인 시안 C(벤토 그리드)와 C-4(프로젝트 상세 페이지)가 기준이다. 이전 명세 "한 가지 잉크(One Ink)"는 git 기록에만 남아 있다.
> 토큰 값의 원본은 `index.html`의 `:root`이고, CSS 변수 이름은 위 `colors` 키와 1:1이다(`--surface-inset`, `--hairline` …). 이 파일을 고치면 `/impeccable document`로 `.impeccable/design.json`을 다시 만든다.

## Overview

**Creative North Star: "한 판의 벤토 (One Tray)"**

페이지는 따뜻한 회색 쟁반(`canvas`) 위에 크기가 다른 흰 카드를 16px 간격으로 채운 한 판의 도시락이다. 카드 한 칸에는 정보가 한 종류만 들어간다. 이름, 총 경력, 연락처, 기술 스택이 각자 칸을 차지하므로 인사담당자는 칸만 훑어도 요점을 읽는다. 기술 면접관은 프로젝트 카드를 눌러 상세 페이지에서 세부를 확인한다.

색은 세 겹이다. 대부분은 **흰 카드**가 차지한다. 각 섹션의 리듬은 **잉크 카드**(반전된 검정 카드) 하나가 끊는다. 가장 중요한 한 곳에만 **파란 액센트**를 칠한다. 한 화면에서 카드 크기의 파란 면은 히어로 하나뿐이다.

어조는 친근하지만 정돈되어 있다. 모서리는 28px로 크게 둥글고 글자는 900 웨이트로 굵다. 그림자·그라디언트·장식 아이콘은 없다. 깊이는 쟁반과 카드의 톤 차이로만 만든다.

거부한 것: 그라디언트 워시, 네온, 글래스모피즘(반투명 카드·바 — 바 뒤 점진 흐림 하나만 예외), 카드마다 아이콘을 얹은 기능 소개 그리드, 이모지, 왼쪽 컬러 테두리 카드, 떠 있는 모달.

**Key Characteristics:**
- 4열 벤토 그리드, gap 16px, 최대 폭 1344px. 카드의 칸 수(1·2·3·4칸, 2행)가 정보의 무게를 나타낸다.
- 카드 세 종류: 흰 카드(기본), 잉크 카드(섹션당 하나, 프로젝트만 강조용 최대 둘), 액센트 카드(한 화면에 하나).
- 본문은 Noto Sans KR 400/500/700/900, 숫자·날짜·라벨·기술 이름은 Space Grotesk 500/700.
- 라이트와 다크는 `light-dark()` 한 벌의 토큰으로 정의한다. 다크에서는 쟁반이 흑연색이 되고 잉크 카드는 밝은 회백색으로 반전된다.
- 메인과 프로젝트 상세는 같은 문서의 두 뷰다. `#/p/<id>` 해시가 상세를 연다.
- 3개 국어가 같은 DOM 안에 있고 `html[lang]`으로만 전환된다.

## Colors

거의 무채색이고 유채색은 액센트 하나뿐이다. 라이트는 따뜻한 종이와 회색, 다크는 차가운 흑연 계열이다.

### Primary
- **액센트 (accent)**: 라이트는 코발트 블루, 다크는 일본 칠기 벤또 도시락의 옻칠 빨강(사용자 결정, 2026-09-25 — 연보라·코랄은 기각). 면(카드·배지)에만 칠한다. 쓰는 곳은 다섯 곳뿐이다: ① 메인 히어로 카드 바탕 ② "재직 중" 배지 ③ 상세 페이지 히어로 카드 바탕 ④ 상세 05 AI 섹션 제목(번호와 "AI 활용") ⑤ 키보드 포커스 링.
- **액센트 글자 (accent-text)**: 액센트 면 위의 글자. 두 테마 모두 흰색이다(라이트 7.5:1, 다크 6.6:1).
- **액센트 선 (accent-line)**: 글자·선으로 쓰는 액센트 — 상세 05 AI 제목과 키보드 포커스 링. 라이트는 액센트와 같고, 다크는 옻칠 빨강이 어두운 바탕 위에서 2.6:1밖에 안 나와 같은 계열을 밝힌 빨강을 쓴다(카드 위 5.1:1). 액센트 면 위의 포커스 링도 이 색이다.

### Secondary
- **잉크 (ink)** / **잉크 글자 (ink-text)**: 반전 카드(연락처, 강조 프로젝트, 푸터, 상세의 결과물)와 켜진 내비 항목·언어 버튼에 쓴다. 다크에서는 밝은 회백색이 되므로 "잉크"는 색 이름이 아니라 **역할**이다.
- **잉크 보조 글자 (ink-text-soft)**: 잉크 카드 안의 라벨·기간·역할·전화번호와 복사 버튼 아이콘. 불투명도로 흐리게 만들지 않고 이 토큰을 쓴다.
- **잉크 위 면 (ink-inset)**: 잉크 카드 안의 태그와 알약 링크(GitHub·LinkedIn·결과물 링크) 바탕.

### Neutral
- **쟁반 (canvas)**: 페이지 배경. 카드 사이 16px 틈과 섹션 머리, 푸터 아래 작은 줄이 이 위에 놓인다.
- **카드 (surface)**: 모든 기본 카드와 내비 바, 상세의 "메인으로"·페이저 버튼.
- **카드 위 면 (surface-inset)**: 흰 카드 안의 핵심 스택 알약과 태그 바탕, 버튼 호버. 쟁반과 같은 값이라 "카드에 뚫린 구멍"처럼 보인다.
- **미디어 (media)**: 프로젝트 이미지 자리. 이미지가 없으면 이 면과 캡션만 남긴다.
- **헤어라인 (hairline)**: 비활성 아이콘 글리프와 인쇄에서 흰 카드의 테두리에만 쓴다. 화면의 카드는 테두리 없이 톤 차이로 구분한다.
- **글자 (text)** / **본문 (body)** / **뮤트 (muted)**: 제목 / 설명 문단 / 라벨·기간·보조 정보. 뮤트는 가장 어두운 바탕인 `media` 위에서도 4.7:1이다(라이트 카드 위 6.9:1).

### Named Rules
**The One Accent Rule.** 파란색은 위의 다섯 곳에만 쓴다. 강조가 더 필요하면 새 색을 만들지 말고 잉크 카드나 900 웨이트를 쓴다. 카드 크기의 파란 면은 한 화면에 히어로 하나뿐이다.

**The One Ink Card Rule.** 잉크 카드는 섹션(그리드 한 판)당 최대 하나다: 프로필은 연락처, 상세 히어로는 결과물 카드 하나. 예외는 프로젝트 섹션이다 — 강조 프로젝트(`ink: true`)는 최대 둘이고 **서로 붙이지 않는다**(1번 아래에 2번을 한 열로 쌓는다). 푸터는 섹션 밖이다. 잉크 카드는 리듬을 끊는 쉼표 역할이라, 둘이 붙으면 체크무늬가 된다.

**The Surface Contrast Rule.** 글자 대비는 글자가 실제로 놓이는 면(카드·잉크·액센트·media)을 기준으로 4.5:1 이상, 24px 이상 글자는 3:1 이상이어야 한다. 토큰 값을 바꾸면 그 면들 위에서 모두 다시 잰다.

**The No-JS-Color Rule.** 색은 스타일시트에서만 정한다. 켜진 내비·언어 상태는 `is-on` 클래스로 CSS가 칠하고, JS는 클래스 이름만 바꾼다.

## Typography

**Body / Display Font:** Noto Sans KR (일본어 화면은 Noto Sans JP 우선)
**Data Font:** Space Grotesk

**Character:** 굵은 산세리프 하나가 68px 이름부터 16px 본문까지 400·500·700·900 웨이트로 위계를 만든다. Space Grotesk는 숫자와 라틴 라벨에 기하학적인 인상을 더하는 데이터 전용 서체다.

### Hierarchy
- **Display** (900, 68px, 1.1, -0.03em): 메인 히어로 카드의 이름. 모바일 44px.
- **Display Detail** (900, 60px, 1.2): 상세 히어로의 프로젝트 제목(`mtitle`). 중간 폭 48px, 모바일 36px.
- **Headline** (900, 48px, 1.2, -0.02em): 섹션 제목(경력·프로젝트·학력). 모바일 32px.
- **Lead** (700, 26px, 1.45): 히어로 카드의 한 줄 소개. `text-wrap: pretty`.
- **Title L** (900, 32px): 대표 프로젝트 제목.
- **Title** (700, 28px): 경력 카드의 회사명, 학력의 학교명, 상세의 "결과물 보기".
- **Title S** (700, 24px): 일반 프로젝트 제목. 자격증·병역 이름은 22px, 상세 본문 카드 제목도 22px.
- **Body** (400, 16~18px, 1.7): 설명 문단(자기소개 17px, 상세 blurb 18px). 색은 `body`.
- **Stat** (Space Grotesk 700, 88px, 1.0): 총 경력 숫자. 단위("년차")는 본문 서체 700, 28px. 모바일 64px.
- **Stat Detail** (Space Grotesk 700, 64px): 상세의 수치 카드.
- **Mail** (Space Grotesk 700, 34px): 푸터 이메일. 모바일 20px.
- **Label** (500, 15px, `muted`): 카드 상단 라벨("총 경력", "연락처")은 본문 서체다. 기간·`PROJECT nn`처럼 숫자가 주인공인 라벨만 Space Grotesk로 쓴다.
- **Stack** (Space Grotesk 500): 메인 기술 스택 15px(핵심 스택만 알약), 상세 기술 스택 17px 글자(알약 없음). 카드 안 태그는 13px 500.

### Named Rules
**The Grotesk Means Data Rule.** Space Grotesk는 숫자, 날짜, 기술 이름, 연락처 값에만 쓴다. 문장에는 쓰지 않는다.

**The 900 Is Rare Rule.** 900 웨이트는 이름(히어로·내비·푸터), 섹션 제목, 대표 프로젝트 제목, 상세 히어로 제목에만 쓴다. 카드 제목까지 900이 되면 위계가 무너진다.

**The One Bold Rule.** 문장 안 강조(`**…**` → `<strong>`)는 항목 하나에 최대 하나, 배경 없는 600 웨이트다. 액센트 면 위에서는 둘레 굵기를 따라간다.

**The Balanced Heading Rule.** 여러 줄로 접히는 제목(이름·섹션·회사·프로젝트·학교·자격증·상세 제목)은 `text-wrap: balance`로 줄 길이를 고르게 한다. 본문은 `text-wrap: pretty`. 큰 한글 제목은 받침이 닿지 않도록 행간 1.2 이상.

**The Language Owns Line Breaks Rule.** `word-break: keep-all`은 `html[lang="ko"] body` 한 곳에만 둔다. 안전망으로 `body { overflow-wrap: break-word }`를 건다.

## Layout

페이지 최대 폭 1344px(1440 뷰포트 기준 좌우 48px), 위 여백 32px, 아래 여백 26px(푸터 위·아래 간격이 같아지게). 모든 형제 간격은 `gap`으로 잡는다.

**배율**: 이 문서의 px 값은 100% 기준이다. 1001px 이상 데스크톱 화면에서는 `.page{zoom:.9}`로 전체를 0.9배로 그린다(브라우저 90%가 적정 밀도라는 사용자 결정, 2026-09-25). 중간 폭·모바일·인쇄는 원래 크기다. 값을 바꿀 때는 토큰을 줄이지 말고 이 배율 한 곳만 조정한다.

- **내비 바**: sticky(`top: 16px`). 데스크톱·중간 폭에서는 흰 알약 바탕을 없애고 안쪽 여백(12px 12px 12px 28px)만 남겨, 이름과 버튼 자리는 알약이 있던 때와 같다(사용자 결정, 2026-09-26). 맨 위에서는 지금 모습 그대로이고, 스크롤하면(4px 이상) 화면 위쪽 약 180px(모바일 200px)이 **바 뒤 점진 흐림**으로 덮인다: 1·3·6px 흐림 세 겹을 아래로 갈수록 마스크로 서서히 지우고, 쟁반색 덮개를 얹는다(다크 60% → 35% → 0, 라이트는 흰 카드 위에서 회색 띠로 도드라져 25% → 12% → 0). 흰 바는 불투명한 채 그 위에 떠 있다(사용자 결정, 2026-09-25 — 띠·테·그림자·헤어라인·반전·숨김·반투명 바는 기각). 왼쪽에 이름만(900, 20px) 둔다. `.dev`나 액센트 점은 붙이지 않는다. 오른쪽에 챕터 4개(프로필 · 경력 · 프로젝트 · 학력·자격증)와 언어·테마·PDF 아이콘 버튼. 켜진 챕터는 잉크 알약이다. 메인에서는 바 아랫변 기준으로 스크롤에 따라, 상세에서는 항상 "프로젝트"가 켜진다.
- **섹션 머리**: 카드 밖에서 쟁반 위에 Headline 제목만 둔다. 패딩 64px 16px 8px. `02 / CAREER` 같은 번호 라벨은 의미가 없어 뺐다(사용자 결정, 2026-09-25).
- **01 프로필 (벤토)**: 4열 × 3행.
  - 히어로 카드: 3열 × 2행, 액센트, 패딩 48px, 최소 높이 520px. 라벨 없이 이름 → 한 줄 소개 → 자기소개 문단을 카드 아래에 붙인다(`flex-end`).
  - 총 경력: 오른쪽 열 위, 흰 카드. "N년차"로 표시하고, N은 `CO[].period`의 근무 개월 합에서 채운 햇수 + 1로 계산한다(하드코딩하지 않는다).
  - 연락처: 오른쪽 열 아래, 잉크 카드(이 섹션의 쉼표). 이메일·전화는 링크가 아닌 텍스트 + 복사 버튼, 그 아래 GitHub·LinkedIn 링크.
  - 기술 스택: 아랫줄 4열 전체 폭, 흰 카드. 카드 라벨("기술 스택")은 화면에 두지 않는다 — 첫 묶음 "핵심 스택"이 라벨 역할을 하고, 라벨은 스크린리더용으로만 남긴다. 묶음 제목은 다른 카드 라벨(총 경력 등)과 같은 15px `muted`다(사용자 결정, 2026-09-26). `STACK`의 네 묶음을 4열로 둔다. 핵심 스택(첫 묶음)만 `surface-inset` 알약으로 강조하고, 나머지 묶음은 알약 없는 15px 글자(`body`)로 흘린다.
  - 프로필 사진 칸과 구직 상태 카드는 두지 않는다.
- **02 경력**: 회사별 흰 카드(최소 높이 300px, 패딩 36px), `repeat(auto-fit, minmax(360px, 1fr))`. 회사가 2곳이면 2장만 두고 빈 칸을 만들지 않는다. 최신 경력이 먼저. 기간(Space Grotesk, `muted`)·배지 → 회사명 → 직무 → 설명(회사 소개 + 업무 불릿, `margin-top: auto`로 바닥에 붙인다). 근무 기간 타임라인 막대는 없다.
- **03 프로젝트**: 4열.
  - 대표(`rows: 2`): 2열 × 2행 미디어 카드(16px 안쪽 여백, 이미지 420px, 18px 모서리), 제목 Title L.
  - 보조(`span: 1`): 1열, 이미지 없음, 최소 높이 340px.
  - 잉크 카드(`ink: true`)는 **강조하고 싶은 프로젝트**에만, 최대 둘. 흰 카드 사이에서는 크기보다 색이 먼저 읽히므로 1번 프로젝트(ezZip)는 크기와 색을 둘 다 받고, 2번(Ez-Spool)은 색만 받는다. Ez-Spool은 ezZip 바로 아래에 둔다(사용자 결정, 2026-09-25 — 하나만 칠하면 그 카드가 1번으로 읽혔다). 잉크 카드 안의 이미지 칸은 `ink-inset`, 캡션은 `ink-text-soft`.
  - 카드 순서는 `CARD_ORDER`가 정한다(ezZip · 아이센드 · PC3D / Ez-Spool · 자재관리 ERP · MakeTApp). 왼쪽 두 칸 열에 ezZip(2×2)과 Ez-Spool이 위아래로, 오른쪽에 가로형 아이센드·PC3D, 맨 아래 줄 오른쪽에 1칸 자재관리 ERP·MakeTApp이 나란히 놓인다(사용자 결정, 2026-09-25). 상세 페이지의 번호와 이전·다음은 `PROJECTS` 순서를 따른다.
  - 가로형(`span: 2`): 2열 미디어 카드, 왼쪽에 220px 이미지.
  - 칸 수는 `PROJECTS[].span / rows`가 정하고 CSS는 `--span / --rows`만 읽는다. 대표(2×2) 옆 두 줄은 높이를 반씩 나눈다(`grid-template-rows: 1fr 1fr`, 사용자 결정, 2026-09-25).
  - 카드는 기간 → 제목 ↗ → 한 줄 요약(`summary`, 30~40자) → 태그. 긴 개요(`intro`)는 상세 01에만 둔다. 성과는 노출하지 않는다. 누르면 상세 페이지가 열린다.
- **04 학력 · 자격 · 병역**: 4열. 학교마다 2열 카드("학력" 라벨 → 학교명 → 전공·학위 → 기간), 자격증은 1열씩("자격증" 라벨 → 이름 → 발급기관·취득일), 병역은 2열(같은 형식). 아이콘 타일은 쓰지 않는다.
- **푸터**: 전체 폭 잉크 카드 하나, 섹션과 64px, 패딩 48px. 왼쪽에 이름(900, 40px) / "C# / .NET 개발자 · N년차"(`ink-text-soft`, N은 총 경력에서 계산) / GitHub ↗ · LinkedIn ↗ 잉크 알약. 오른쪽(오른쪽 정렬)에 "연락처" 라벨 / 이메일(Mail) + 복사 버튼 / 전화번호(18px, `ink-text-soft`) + 복사 버튼. 카드 아래 쟁반 위 오른쪽에 Space Grotesk 13px `muted`로 "최종 수정 YYYY.MM.DD"만 둔다. 저작권 표기(© 연도 이름)는 뺐다(사용자 결정, 2026-09-25). 행동 유도(CTA) 문구는 쓰지 않는다.

**프로젝트 상세 페이지**는 메인 콘텐츠를 대체한다(내비 바는 그대로). 순서: "← 메인으로" + 페이저 줄(중간 폭만) → 히어로 벤토 → 대표 이미지 → 수치 카드 줄 → 본문 카드(01~05) → 메인과 같은 푸터. 세부는 Components의 Project Detail Page에 있다.

**중간 폭(721~1000px)**: 그리드를 2열로 줄인다. 메인·상세 히어로는 2열 × 1행, 스택은 2열(묶음도 2열), 대표 프로젝트는 2열 × 1행, 상세 본문 카드는 모두 2열. 내비의 이름은 숨기고 챕터가 왼쪽으로 붙는다.

**모바일(≤720px)**은 시트 하단의 `@media (max-width: 720px)` 블록 한 곳에서만 재정의한다. 벤토는 **반반 섞기**다(사용자 결정, 2026-09-26): 2열 그리드에서 글이 긴 카드(히어로·기술 스택·2칸 프로젝트·학교·병역·상세 히어로·결과물)는 전체 폭, 짧은 카드(총 경력·연락처·1칸 프로젝트·자격증·상세 기간·기술 스택)만 반씩 나란히 놓는다. 경력 카드는 1열. 프로젝트는 강조(잉크) 카드 ezZip·Ez-Spool을 맨 위로, 흰 카드를 그 아래로 모은다(CSS `order`, 데스크톱의 왼쪽 열과 같은 순서). 글자 크기는 줄이지 않는다. 반 칸 연락처는 값·글자 대신 44px 동그라미 아이콘 넷이다: 메일·전화(누르면 복사), GitHub·LinkedIn(링크). 페이지 좌우 16px, 카드 gap 12px, 카드 모서리 22px, 카드 패딩 24px. 글자는 데스크톱보다 한 단계씩 작다(사용자 결정, 2026-09-26): 히어로 이름 36px, 섹션 제목 26px, 총 경력 숫자 48px, 회사명 20px, 프로젝트 제목 22/18px, 학교 18px·자격증 17px, 푸터 이름 28px·이메일 17px, 상세 제목 30px·부제 15px·소제목 17px, 본문·항목 14px(더 내리지 않는다). 상세 성과 수치는 반 칸 2열 카드(숫자 32px), 수가 홀수면 마지막 카드만 전체 폭(`is-wide`). 히어로 카드는 모바일에서도 안쪽 여백 40px 32px, 한 줄 소개 18px, 자기소개 14px. 한 줄 소개의 두 번째 문장(인라이플·ezZip)은 숨기고(`.lead-more`), 그 자리(390px 기준 한·영 3줄, 일 2줄)를 이름 아래 간격(20px + 3lh / 일본어 2lh)으로 돌려 카드 크기는 원래대로 둔 채 글을 아래로 내린다. 내비는 **화면 위 전체 폭의 얇은 바**다(쟁반색, 버튼 줄은 화면 위와 히어로에서 20px, 가로 가운데, 바 전체 `zoom: .9`): 이름 없이 언어 3 · 테마 · 메뉴 버튼(34px × .9 ≈ 31px, 글리프 14px)을 가운데 정렬로 둔다(하단 알약과 같은 순서, 사용자 결정 2026-09-26). 메뉴를 누르면 맨 위에서도 알약으로 바뀌어, 알약이 아래로 늘어난 카드에 16px 챕터 목록(44px 행, 켜진 챕터 모서리 17px = 알약 27 − 여백 10)과 PDF 저장이 펼쳐진다(전체 폭 판은 쓰지 않는다). 바깥·챕터·Esc로 닫힌다. 맨 위에서는 알약 바탕이 없는 이 바이고, 스크롤하면(4px 이상) 가운데 위 흰 알약(위 11px, 가로 가운데, 안쪽 여백 10px, 모서리 27px)으로 바뀐다. 알약은 반투명 유리(`glass` = surface 72%, 뒤 흐림 16px)에 헤어라인 한 줄(안쪽 box-shadow)을 두른다. 알약 위치를 버튼 줄에 맞춰, 바뀔 때 버튼 좌표는 그대로이고 바탕만 바뀐다(애니메이션 없이 즉시 — 서서히 바꾸면 뒤가 번쩍인다). 모바일에는 바 뒤 점진 흐림이 없다 — iOS Safari 26이 화면 끝에 붙은 전체 폭 고정 층을 보고 주소창 자리를 단색 띠로 칠하기 때문이다. 페이지 위 여백 71px(20 + 버튼 31 + 20). iOS Safari 주소창이 아래에 있어 겹쳐 쌓이지 않게 내비를 위로 올렸다(사용자 결정, 2026-09-26 — 시안 E, 하단 알약 대체). 프로젝트 이미지는 대표 카드(ezZip)만 위에 크게 두고, 가로형은 제목 왼쪽 썸네일(폭 120px, 모서리 14px)을 날짜~설명 높이만큼 늘리고, 기술 태그 줄은 그 아래 카드 전체 폭으로 내린다. 썸네일에는 "이미지 준비 중" 글자를 넣지 않는다. 모바일 프로젝트 카드 제목 끝의 ↗는 숨긴다. 푸터는 한 열로 쌓고 왼쪽 정렬하며(아래 "최종 수정"은 데스크톱처럼 오른쪽 정렬), 위 콘텐츠와는 데스크톱처럼 띄운다(60px = 여백 48 + 카드 간격 12).

**인쇄**는 1급 기능이다. 메인은 1열로 흐르고, 상세가 열려 있으면 그 프로젝트만 나온다(메인은 `display:none`). 내비·페이저 줄은 `data-noprint`, 이미지는 숨긴다. 흰 카드는 종이에서 사라지므로 `hairline` 테두리를 두르고, 잉크·액센트 카드는 `print-color-adjust: exact`로 바탕을 강제한다. 카드는 페이지 사이에서 쪼개지지 않는다.

리듬은 6 · 10 · 16 · 24 · 32 · 48 · 64px이다.

## Elevation & Depth

평면이 기본이다. 깊이는 **쟁반 → 카드 → 카드 위 면** 세 단의 톤 차이로만 표현한다. 화면의 카드에는 테두리도 그림자도 없다(인쇄의 헤어라인은 예외). 그림자 토큰은 없다. 스크롤 중 상단 바는 그림자 대신 바 뒤 점진 흐림으로 떠 보인다.

### Named Rules
**The Flat Tray Rule.** 카드·내비·버튼·칩은 호버해도 그림자를 얻지 않는다. 스크롤 중의 상단 바도 그림자 대신 바 뒤 점진 흐림이다. 프로젝트 카드의 호버는 제목 밑줄이다(카드를 `surface-inset`으로 가라앉히면 같은 색의 태그가 사라진다). 내비 항목·아이콘 버튼·"메인으로"·페이저는 `surface-inset` 바탕으로 호버한다.

## Shapes

크고 부드러운 모서리가 인상의 절반을 만든다. 카드·푸터 28px(모바일 22px), 카드 안 이미지 18px, 내비·버튼·칩·태그·배지·알약 링크는 완전한 알약(999px), 아이콘·복사·페이저 버튼은 원이다. 지원 브라우저에서는 `corner-shape: squircle`을 18px 이상 모서리에 건다.

규칙: **안쪽 모서리 = 바깥 모서리 − 안쪽 여백.** 16px 여백의 미디어 카드(28px) 안 이미지가 18px인 이유다(28 − 16 = 12에 시각 보정 +6).

## Components

### Buttons
- **아이콘 버튼**(언어·테마·PDF): 40px 원, 테두리 없음, 호버 시 `surface-inset`, 켜진 언어는 잉크. SVG 16px, 스트로크 1.6px. 모바일 타깃 44px.
- **복사 버튼**: 44px 원, 배경 투명(카드 바탕과 같다), 아이콘 `ink-text-soft` → 호버 `ink-text`. 누르면 1.4초 체크 아이콘으로 바뀌고 `aria-live`가 3개 국어로 읽는다.
- **잉크 알약 링크**: 44px 높이, `ink-inset` 바탕. 푸터 GitHub·LinkedIn, 상세의 결과물 링크.
- **내비 항목**: 알약, 44px 높이, 좌우 20px, 15px 500. 켜진 항목만 잉크.
- **포커스**: 전역 `:focus-visible { outline: 2px solid var(--accent); outline-offset: 3px }`, 액센트 면 안에서는 `accent-text`. 프로젝트 카드는 안의 제목 버튼이 포커스될 때 카드에 그린다.

### Chips
- **메인 기술 스택**: 핵심 스택만 `surface-inset` 알약(Space Grotesk 15px 500, 패딩 4px 12px, 간격 6px). 나머지는 같은 크기의 글자, 간격 4px 14px. 묶음 라벨은 14px `muted`.
- **태그**: 13px 500 알약, 패딩 6px 12px. 흰 카드에서는 `surface-inset`, 잉크 카드에서는 `ink-inset`. 프로젝트 카드 바닥.
- **상태 배지**: 액센트 알약, 13px 500. "재직 중"에만 쓴다.

### Cards
- **히어로 카드**: 액센트, 패딩 48px. 위에 Label(`accent-text` 그대로), 아래에 Display 이름 → Lead → Body.
- **총 경력 카드**: 흰 카드, 위 라벨, 아래 Stat 숫자와 단위. 값은 근무 기간에서 계산한다. 지어낸 숫자를 쓰지 않는다.
- **경력 카드**: 흰 카드, 패딩 36px, 기간·배지 행 → Title 회사 → 뮤트 직무 → 바닥에 소개와 불릿.
- **프로젝트 카드**: 카드 전체가 클릭 면이지만 접근성 컨트롤은 `h3` 안의 버튼 하나다. 카드 자체를 `<a>`나 `role=button`으로 만들지 않는다 — 제목이 버튼 이름에 묻혀 헤딩 탐색에서 사라진다.
- **학력·자격증·병역 카드**: 흰 카드, 라벨 → 이름 → 보조 정보의 같은 형식.
- **빈 이미지**: `media` 면에 14px 뮤트 캡션만 둔다. 본문으로 채우지 않는다.

### Project Detail Page
카드를 누르면 `#/p/<id>`로 이동하고 상세 뷰가 메인 콘텐츠를 대체한다. 새로고침·뒤로가기·해시 직접 진입 모두 이 해시 하나로 동작한다.

- **데스크톱(1001px 이상)**: 상단 바의 챕터는 메인과 똑같이 두고, 켜진 "프로젝트" 잉크 칩이 오른쪽으로 늘어나 번호(`ink-text-soft`, 13px)와 이전·다음 32px 동그라미(모바일 알약의 메뉴 버튼과 같은 `surface-inset` 바탕, 끝에서 35% 불투명)를 품는다. "← 메인으로" 줄은 없고 이름("장민규")을 누르면 보던 카드로 돌아간다(사용자 결정, 2026-09-26 — 시안 v3 B).
- **모바일(≤720px)**: 본문 위 줄이 없다. 위 바(알약) 맨 앞에 ← 버튼(바탕 없음, 다른 버튼과 6px 떼어 둠)이 붙어 보던 카드로 돌아간다. 모바일에는 이전·다음 넘기기가 없다(메인으로 돌아가 다른 카드를 고른다). (사용자 결정, 2026-09-26).
- **상단 줄** (중간 폭 721~1000px, `data-noprint`): 왼쪽 "← 메인으로" 흰 알약(44px), 오른쪽 이전 · `01 / 06` · 다음(44px 흰 원). 화살표 라벨에는 이전·다음 프로젝트 이름이 붙는다. 페이저와 좌우 화살표 키는 끝에서 멈춘다.
- **히어로 벤토** (4열): 액센트 카드 2열 × 2행(`프로젝트 nn · 회사` — "프로젝트"는 언어별로 프로젝트 / PROJECT / プロジェクト, Display Detail 제목, blurb). 오른쪽 위에 정보 카드(기간, 인원·형태는 데이터에 있을 때만)와 기술 스택 카드가 1열씩. 기술 스택은 알약 없이 Space Grotesk 17px 500 글자를 기간처럼 카드 바닥에 붙인다(사용자 결정, 2026-09-25). 오른쪽 아래에 잉크 카드 "결과물 보기" + 링크 알약(줄 높이 160px로 낮게, 남는 높이는 위 줄이 받는다 — 사용자 결정, 2026-09-25) — 링크가 없어도 잉크 칸은 내용 없이 남기고, 모든 폭에서 링크가 있을 때와 같은 높이를 지킨다(중간 폭 108px, 모바일은 옆 기간 카드와 같은 줄 높이, 2026-09-26). 모바일에서는 기간 · 결과물 보기가 정사각형 반 칸씩 한 줄, 기술 스택이 그 아래 전체 폭 한 줄이다(결과물 링크 알약은 14px, 영어 13px로 한 줄 유지)(정보·스택 카드를 길게 늘이면 어색했다 — 사용자 결정, 2026-09-25). 인쇄에서는 빈 칸을 뺀다.
- **대표 이미지**: 전체 폭 흰 카드(안쪽 여백 16px), 이미지 480px(모바일 220px). 없으면 `media` 면과 캡션.
- **수치 카드**: 흰 카드, Stat Detail 값 + 라벨, `repeat(auto-fit, minmax(240px, 1fr))`. `stats`가 없으면 줄을 숨긴다. 값은 `metrics` 문장에 이미 있는 수치만.
- **본문 카드**: AGENTS §2의 01~05 순서와 번호. 모든 섹션이 전체 폭 카드 하나씩이고 위에서 아래로 한 줄씩 쌓인다(사용자 결정, 2026-09-25). ai는 제목 줄(번호와 "AI 활용")을 `accent-line`으로 칠한다(사용자 결정, 2026-09-25). 빈 섹션은 빼되 번호는 당기지 않는다.
- **푸터**: 본문 카드 아래에 메인과 같은 푸터(잉크 카드 + 최종 수정 줄)를 둔다. 하단 "다음 프로젝트" 카드는 두지 않는다(사용자 결정, 2026-09-25) — 다음 프로젝트로는 상단 페이저와 화살표 키로 넘긴다.
- **포커스와 스크롤**: 열면 맨 위로 올리고 `h1`에 포커스(페이저·화살표로 넘길 때는 누른 버튼에 포커스를 둔다). 닫으면(메인으로·Esc·뒤로가기) 떠나기 전 스크롤 위치로 돌아가 마지막으로 본 프로젝트의 카드 버튼에 포커스한다. 해시로 바로 들어왔다면 프로젝트 섹션으로 돌아간다.

### Navigation / Controls
- 언어(`ㅎ / A / あ`)·테마·PDF는 내비 바 오른쪽 끝에 아이콘 버튼으로 둔다. 켜진 언어는 잉크 원이다.
- `role="group"` + `aria-pressed`를 쓰고, 색은 `is-on` 클래스로만 정한다.
- 상세 뷰에서 챕터를 누르면 메인으로 돌아가 그 섹션으로 간다. 이름을 누르면 "← 메인으로"와 같이 보던 카드로 돌아간다.
- 테마 전환은 누른 버튼 중심에서 원형으로 퍼지는 View Transition(340ms)으로 한다. `prefers-reduced-motion`이면 즉시 전환한다.

### Favicon

- 여백의 해(사용자 결정, 2026-09-27): 모서리를 거의 각지게(3/64) 둔 네모에서 원(반지름 15/64)을 오른쪽 위로 비켜 두고, 아래에 수평선 한 줄(44×4). 라이트는 화지(和紙)색 #f4f1ea 바탕 + 파란 원(`accent` #2a45c7) + 먹선(`ink` #17171a), 다크는 쟁반 #121214 바탕 + 옻칠 빨간 원(`accent` #b3242b) + 밝은 선(#ecebe6). 원은 사이트 강조색을 따른다. 사이트 테마 버튼을 따라 두 SVG를 바꿔 끼운다.

## Do's and Don'ts

### Do:
- **Do** 정보 한 종류당 카드 한 칸. 중요도는 칸 수로 표현한다.
- **Do** 새 색은 `:root`에 `light-dark()` 토큰으로 먼저 만든다.
- **Do** 글자 대비는 실제로 놓이는 면(카드·잉크·액센트·media) 기준으로 잰다.
- **Do** 숫자·날짜·라벨·기술 이름·연락처 값만 Space Grotesk로 쓴다.
- **Do** 모바일 재정의는 하단 `@media (max-width: 720px)` 블록 하나에 모은다.
- **Do** 보이지 않는 라벨(`aria-label`, 라이브 리전)도 3개 국어로 준비한다.
- **Do** 레이아웃을 바꾸면 3개 언어 × 1440·900·390px × 라이트·다크 × 인쇄, 그리고 카드 → 상세 → 이전·다음·화살표·Esc → 카드 포커스 복귀와 해시 직접 진입을 모두 확인한다.

### Don't:
- **Don't** 액센트를 다섯 자리 밖에 쓰지 않는다. 두 번째 유채색을 만들지 않는다.
- **Don't** 한 섹션에 잉크 카드를 두 장 이상 두지 않는다. 프로젝트의 강조 카드만 최대 둘이다.
- **Don't** 화면의 카드에 테두리·그림자·그라디언트를 주지 않는다(인쇄의 헤어라인만 예외).
- **Don't** 이모지, 장식 아이콘, 아이콘 타일, "아이콘 + 제목 + 설명" 기능 카드 그리드를 만들지 않는다. 글리프는 `↗`과 화살표만 쓴다.
- **Don't** 900 웨이트를 대표 프로젝트 외의 카드 제목에 쓰지 않는다.
- **Don't** 이메일·전화에 `mailto:`/`tel:` 링크를 걸지 않는다. 텍스트 + 복사 버튼이다.
- **Don't** 프로필 사진 칸, 구직 상태 카드, 행동 유도 문구, 로고의 `.dev`·액센트 점을 되살리지 않는다.
- **Don't** 모달·바텀시트를 다시 만들지 않는다. 프로젝트 상세는 해시로 여는 페이지 뷰다.
- **Don't** 잉크·액센트 카드 안의 보조 글자를 `opacity`로 흐리게 만들지 않는다. 토큰을 쓴다.
- **Don't** 벤토의 칸 수·높이를 CSS에 직접 쓰지 않는다. 데이터가 정하고 CSS는 변수만 읽는다.
- **Don't** `!important`, 인라인 정적 `style=`, 구조에 의존하는 셀렉터(`:first-of-type` 등)를 쓰지 않는다.
