# ADR History — 과잉 설계 감사 및 정리

- 날짜: 2026-09-02
- 대상: `index.html` (이력서 단일 페이지)
- 계기: 저장소 전체 과잉 설계 감사(ponytail-audit)
- 결과: `index.html` 995 → 983줄, 렌더당 동적 바인딩 87개 → 0개

---

## ADR-001. dc-runtime + React 스택을 유지한다

**상태:** 채택 (변경 없음)

**맥락**
감사에서 가장 큰 절감 항목으로 지목된 것은 `support.js`(69KB, 1911줄)와 그것이 unpkg에서 런타임에 내려받는 React 18 + ReactDOM UMD였다. 렌더링 대상은 하드코딩된 카드 6개, 모달, 언어 토글, 테마 토글이 전부인 정적 페이지다. 순수 HTML + 바닐라 JS 약 60줄이면 동일한 결과를 낼 수 있고, 그 경우 -1911줄, -2 의존성이 가능하다.

**결정**
제거하지 않는다.

**근거**
`support.js` 헤더는 `GENERATED from dc-runtime/src/*.ts — do not edit`이며, `.document/History/` 및 `x-dc` / `<helmet>` / `sc-for` 구조는 이 문서가 캔버스 에디터에서 저작되었음을 뜻한다. 런타임을 걷어내면 줄 수는 줄지만 저작 워크플로 자체가 깨진다. 절감액보다 잃는 것이 크다.

**결과**
- 외부 CDN 의존(React, ReactDOM) 유지. 오프라인/CDN 차단 환경에서는 페이지가 렌더되지 않는다.
- 이후 모든 정리는 런타임 위에서, 런타임과 싸우지 않는 방향으로만 수행한다.

---

## ADR-002. 다국어 표시를 렌더 바인딩에서 정적 속성 + CSS로 옮긴다

**상태:** 채택 (적용 완료)

**맥락**
한/영/일 3개 언어의 모든 문구가 `<span style="display:{{ ki }}">` 형태로 표현되어 있었고, 그 수가 87개였다. `renderVals()`는 이를 위해 `ki·ei·ji·kb·eb·jb` 6개 플래그와 `inl()`/`blk()` 헬퍼를 계산했다.

`scrollY`가 컴포넌트 state이므로 **스크롤 프레임마다** `renderVals()`가 실행되고, 87개 바인딩이 매번 재평가·diff 되고 있었다. 언어는 사용자가 클릭할 때만 바뀌는 값인데 스크롤 비용을 지불하고 있었던 셈이다.

**결정**
표시 여부를 정적 속성 `data-l`(inline) / `data-lb`(block)로 표기하고, CSS 3줄로 전환한다.

```css
[data-l],[data-lb]{display:none}
html[lang="ko"] [data-l="ko"],html[lang="en"] [data-l="en"],html[lang="ja"] [data-l="ja"]{display:inline}
html[lang="ko"] [data-lb="ko"],html[lang="en"] [data-lb="en"],html[lang="ja"] [data-lb="ja"]{display:block}
```

`inline`용과 `block`용 속성을 분리한 이유는, 기존 87개 중 60개가 `inline`, 27개가 `block`이었기 때문이다. 단일 속성으로 합치면 레이아웃이 바뀐다.

**전제 조건**
CSS가 `html[lang]`에 의존하므로 첫 페인트 시점에 `lang`이 이미 있어야 한다. 기존에는 `componentDidMount`에서 설정해 마운트 전까지 모든 언어가 숨는 구간이 있었다. `<head>` 부트스트랩 스크립트에서 localStorage를 읽어 선반영하도록 한 줄 추가했다 — 원래 존재하던 깜빡임도 함께 해소된다.

**결과**
- 렌더당 동적 바인딩 87 → 0. 스크롤 성능에 직접 기여.
- JS가 죽어도 언어 표시가 동작한다 (정적 스냅샷에서 확인).
- 언어별 문구를 추가할 때 템플릿 바인딩이 아니라 `data-l="xx"` 속성만 붙이면 된다.

---

## ADR-003. `<title>`을 `<helmet>` 밖 실제 `<head>`로 옮기고 언어에 연동한다

**상태:** 채택 (적용 완료)

**맥락**
언어 전환 시 브라우저 탭 제목도 해당 언어로 바뀌게 하려 했다. 두 가지 자연스러운 방법이 모두 막혀 있었다.

1. `document.title = ...` 대입 → helmet이 `<title>`을 **live 엘리먼트**로 관리하며 매 렌더마다 템플릿 원본 텍스트로 되돌린다 (`support.js:1487`):
   ```js
   if (el.textContent !== child.textContent) el.textContent = child.textContent;
   ```
   `scrollY`가 state이므로 스크롤 한 번에 즉시 원복된다.
2. `<title>{{ pageTitle }}</title>` → helmet의 compile 함수는 `(_vals, ctx) => ...` 시그니처로 **`_vals`를 사용하지 않는다** (`support.js:1420`). 바인딩을 해석하지 않으므로 중괄호가 그대로 출력된다.

**결정**
`<title>`을 `<helmet>`에서 제거하고 문서의 실제 `<head>`에 둔다. helmet 관리 대상에서 빠지므로 아무것도 덮어쓰지 않는다. 이름 3개국어는 `window.NAMES` 하나로 공유하고, `<head>` 부트스트랩(초기 로드)과 `setLang`(전환 시) 두 곳에서 `document.title`을 설정한다.

**대안으로 검토했다가 버린 것**
helmet이 참조하는 템플릿 원본 노드의 `textContent`를 직접 변형하는 방법. 동작은 하지만 프레임워크 내부 구조에 의존하는 해킹이라 배제했다.

**결과**
- 탭 제목: 장민규 / Min-gyu Jang / チャン・ミンギュ. 새로고침 후에도 유지.
- 스크롤로 인한 리렌더에도 원복되지 않음 (실측 확인).
- `<title>`이 helmet 밖에 있으므로, 캔버스 에디터가 head 메타데이터를 helmet 기준으로 직렬화한다면 이 태그를 인식하지 못할 수 있다. **에디터에서 재저장 시 확인 필요.**
- `og:title`은 `장민규 · C#/.NET 개발자 이력서`로 유지. 공유 카드는 설명이 있는 편이 낫고, 크롤러는 대부분 JS 변경을 반영하지 않는다.

---

## ADR-004. `navState()` / `ResizeObserver` / `geo` 상태를 유지한다

**상태:** 채택 (감사 지적 철회)

**맥락**
감사 1차에서 다음을 과잉으로 지목했다.
- `navState()` 59줄 — 챕터 높이 기반 비례 탭 너비(`Math.pow(span, 0.55)` 스무딩) + 읽기 진행 게이지
- `ResizeObserver(documentElement)` — `resize` 리스너와 중복으로 보임
- `geo` 상태 문자열 — 수제 변경 감지 키

**결정**
셋 다 유지한다. 지적을 철회한다.

**근거**
- `resize`는 뷰포트 크기 변화만 잡는다. 폰트 로드 완료나 리플로우로 **문서 높이**가 바뀌는 경우는 잡지 못하고, `ResizeObserver`는 잡는다. 코드 주석(`nav fills depend on final layout — fonts, images and reflow all land here`)이 정확히 이 의도를 적어두고 있었다. 중복이 아니다.
- `geo`는 그 높이 변화를 state에 반영하기 위한 키다. `ResizeObserver`가 정당하면 `geo`도 정당하다.
- 비례 탭 너비와 진행 게이지는 사고로 생긴 복잡도가 아니라 의도된 디자인이다. 복잡하다는 이유로 기능을 지우는 것은 감사의 권한 밖이다.

**교훈**
"중복으로 보이는 두 리스너"는 관측 대상이 다를 수 있다. 지우기 전에 주석과 관측 대상을 먼저 읽는다.

---

## ADR-005. 모바일 `!important` 오버라이드 리팩터링을 보류한다

**상태:** 보류 (유효한 지적, 미적용)

**맥락**
`@media (max-width:720px)` 블록이 86줄에 `!important` 152개를 담고 있다. 이는 마크업의 인라인 `style=` 속성 255개를 특이도로 이기기 위한 것이다. 근본 원인은 인라인 스타일이고, 반복되는 인라인 블록을 시트 상단에 이미 존재하는 클래스(`.mono .sq .pill .tag .eyebrow`)로 옮기면 `!important`는 전부 불필요해진다.

**결정**
이번 작업 범위에서 제외한다.

**근거**
인라인 스타일 255개를 클래스로 옮기는 전면 리스타일이며, 시각적 회귀를 눈으로 검증하지 않고 진행하면 레이아웃이 깨진다. 자동 검증 수단이 없는 상태에서 감행할 변경이 아니다.

**결과**
별도 작업으로 남긴다. 진행 시 데스크톱/모바일 양쪽 스크린샷 비교가 선행되어야 한다.

---

## 함께 적용한 소규모 정리

| 항목 | 내용 |
|---|---|
| 죽은 CSS 규칙 | `#s-intro,section[data-chapter],[data-kpisec]{scroll-margin-top:64px}` 삭제 — 하단의 `section[id],header[id]{...76px}`가 동일 셀렉터를 전부 덮어쓰고 있었다 |
| 스크롤바 숨김 정리 | IE 전용 `-ms-overflow-style`, `display:none` 옆의 중복 `width/height:0`, 불필요한 `!important` 제거. Safari 대응 `::-webkit-scrollbar`는 유지 |
| `T.site` 삭제 | `T.link`와 바이트 단위로 동일했다. `siteLabel` 바인딩 제거, `linkLabel` 하나로 통합 |
| 빈 파일 삭제 | 저장소 루트의 `공식` (0바이트, 미추적) |
| 타이틀 | `장민규 · C#/.NET 개발자 이력서` → `장민규` (ADR-003으로 다국어 연동) |

## 검토했으나 손대지 않은 것

- **Pretendard 스타일시트 2개** — JP에 한글이 없을 경우를 위한 폴백이 `font-family` 스택에 이미 있다. 의도된 구성.
- **`bold()` (`**` 파서)** — 대체하려면 다국어 문자열 약 50개에 마크업을 심고 `dangerouslySetInnerHTML`을 써야 한다. 현재의 2줄이 더 낫다.
- **`CARD_H3_FEATURE`, 필터 7개, 모달 내 언어/테마 버튼** — 의도된 디자인 및 제품 결정.

## 알려진 이슈 (미수정, 기존 문제)

테마 토글을 view transition(620ms) 도중에 다시 누르면 콘솔에 `InvalidStateError: Transition was aborted because of invalid state`가 발생한다. `toggleTheme`의 `document.startViewTransition` 호출이 겹칠 때 발생하며, 이번 변경과 무관한 기존 동작이다. 화면에는 영향이 없다.

## 검증

로컬 정적 서버 + 브라우저 실측으로 확인:

- 한/영/일 전환 시 본문·탭 제목 모두 해당 언어로 전환, 나머지 언어 비표시
- 새로고침 후 언어·테마 유지 (localStorage)
- 프로젝트 카드 6개 렌더, 모달 개폐(Escape 포함), 기여 항목 4개 및 강조(`<strong>`) 4개 정상
- 테마 토글 및 `theme-color` 메타 갱신 정상
- 미해결 `{{ }}` 바인딩 0개, `<head>` 내 `<title>` 1개
- 스크롤로 리렌더를 유발해도 탭 제목 원복 없음
- JS 미실행 정적 스냅샷에서도 한국어만 표시 (CSS 단독 동작 확인)

백업: `scratchpad/index.html.bak` (감사 전), `index.html.bak2` (타이틀 작업 전)
