# 포트폴리오 메인 페이지 리디자인 — 적용 지시서 (최종)

시안 파일: `Project Detail.dc.html` (8a 라이트 / 8b 다크). 이 문서가 그 시안의 단일 반영 스펙이다.
AGENTS.md 규칙 준수: 색은 `:root` 토큰만, `!important` 0, 모바일 블록 1개, 3개 국어 짝 유지(§5), 수치는 기존 문장에서만(§4), 인쇄 1급.
**라이트 값(light-dark 첫 인수)은 이 문서에 명시된 곳만 바꾼다.**

---

## 0. 요약 — 바뀌는 것 6가지

1. 다크 토큰 교체 (3b "면 리프트" + 톤다운 그레이)
2. 타입 스케일 한 단계 상향 (최소 14px)
3. About: 줄글 2문단 → 리드 한 문장 + 불릿 3개
4. 경력: 타임라인 바 유지, 회사 카드 → 패널 없는 플랫 2컬럼
5. 프로젝트 카드: D8 — 3:4 단색 카드, 아이브로우/제목/요약 + 우하단 이미지, 링크 제거
6. 프로젝트 모달: 5단계 번호 레일(1b) + 성과 스탯 카드 + blurb 복원
7. 챕터 헤더 밑줄 없음(현행 유지), 챕터 간격 96 → 80px

---

## 1. `:root` 토큰

```css
:root{
  color-scheme:light dark;
  --bg:light-dark(#fbfbf9,#101011);
  --fg:light-dark(#1c1b19,#d9d9db);
  --ink:light-dark(#151514,#d9d9db);
  --ink-fg:light-dark(#fbfbf9,#101011);
  --card:light-dark(#f1f1f0,#1c1c20);
  --card-hover:light-dark(#eaeae9,#222227);
  --card-item:light-dark(#fbfbf9,#292930);
  --line:light-dark(#dcdbd5,#34343b);
  --line-soft:light-dark(#e3e2dc,#2c2c33);
  --line-card:light-dark(#e3e2dc,#35353d);
  --line-ui:light-dark(#cfcdc6,#4a4a54);
  --muted:light-dark(#5f5f59,#98989d);
  --muted-2:light-dark(#54544e,#a8a8ac);
  --chip-bg:light-dark(#f7f6f3,#24242a);
  --chip-bc:light-dark(#dcdbd5,#4a4a54);
  --chip-fg:light-dark(#3f3f3a,#bebec2);
  --body:light-dark(#2b2a27,#cbcbce);      /* 신규: 본문 */
  --sub:light-dark(#45453f,#adadb1);       /* 신규: 카드 요약·보조 본문 */
  --dot:light-dark(#6f6f68,#9a9aa3);       /* 신규: 불릿 점 */
  --stripe:light-dark(#d3d1ca,#3c3c44);    /* 신규: 타임라인 공백 스트라이프 */
  --ai:light-dark(#4f46e5,#a5b4fc);        /* 신규: 모달 AI 섹션 강조 */
}
```
라이트 변경분(시인성): `--line` #e5e4e0→#dcdbd5, `--line-ui` #dedcd6→#cfcdc6, `--muted` #6f6f68→#5f5f59, `--muted-2` #63635d→#54544e, `--chip-fg` #4a4a45→#3f3f3a.
`theme-color` 메타 스크립트의 다크 값 `#0c0c0d` → `#101011`. 모달 오버레이 `rgba(0,0,0,.76)` → `.7`.

### 시트 안의 다크 리터럴 → 토큰
`light-dark(` 두 번째 인수로 박힌 값은 전부 위 토큰으로 치환한다. 대응: 제목/이름 `#ececed`→`var(--fg)`, 본문 `#dcdcdf`·`#c9c9cf`→`var(--body)`, 요약 `#9a9aa2`·`#a8a8b2`→`var(--sub)`, 라벨 `#858590`→`var(--muted)`, 불릿 `#76757d`→`var(--dot)`, 스트라이프 `#26262b`→`var(--stripe)`. 라이트 인수도 같은 토큰의 첫 값과 일치해야 한다.

---

## 2. 타입 스케일 (전 요소 · 라이트/다크 공통)

| 역할 | 현재 | 변경 |
|---|---|---|
| 모노 라벨·아이브로우·스펙 라벨 (`.eyebrow`, `.speclabel`, `.m-flow-num`, `.m-stat-k`, 필터, 푸터 소문) | 11.5–12.5 | **14** |
| 메타·소제목 (`.tl-co`, `.card-meta`, 연락처 행, 세그 버튼 A/あ, `.spec-date`) | 13–14 | **15** |
| 본문 (`.card-blurb`, `.m-flow-text`, `.m-flow-item`, `.co-item`, `.spec-role`) | 14.5–15 | **16** |
| About 불릿 (`.about-item`) | 16 | **17** |
| 카드 제목 (`.card-title`) | 19–21 | **22** (feature 카드도 22) |
| About 리드 (`.about-lead`), 히어로 서브 | 20 / 19 | **22** / 20 |
| 챕터 h2 | 28 | **30** |
| 모달 제목 | 26 | **28** |
| 스탯 값 (`.m-stat-v`) | 26 | **28** |
| 푸터 이름 / 이메일 | 40 / 25 | **42** / 27 |
| 히어로 h1 | 86 | 유지 |

본문 계열 `font-weight:300` → **400**. 모노 `letter-spacing:.12–.14em` → **.08–.1em**. 불릿 점 4px → **5px**(top 10px).
타임라인 바 높이 52 → **58px**. 모바일 블록에서는 각 값 −1~−2px, 히어로 h1은 기존 규칙 유지.

---

## 3. About

### CSS (`.about-body*` 세 규칙 삭제 후)
```css
.about{padding:38px 0 34px;border-bottom:1px solid var(--line)}
.about-lead{margin:0 0 16px;font-size:22px;line-height:1.5;font-weight:500;letter-spacing:-.014em;color:var(--fg);word-break:keep-all}
.about-list{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
.about-item{position:relative;padding-left:16px;font-size:17px;line-height:1.7;color:var(--body);word-break:keep-all}
.about-item::before{content:"";position:absolute;left:0;top:11px;width:5px;height:5px;border-radius:50%;background:var(--dot)}
.kw{background:var(--ink);color:var(--ink-fg);padding:.08em .32em .12em;margin:0 .04em;border-radius:3px;font-weight:600;box-decoration-break:clone;-webkit-box-decoration-break:clone}
```
`.kw`는 `[data-modalcard] li strong`, `.m-flow-item strong`, `.co-item strong`과 규칙을 공유한다(셀렉터 나열, 중복 정의 제거).

### 템플릿 — `<section class="about">` 전체 교체
```html
<section class="about">
  <p class="about-lead">
    <span data-lb="ko">고등학교 때 개발을 시작해 <strong class="kw">8년차</strong>가 된 C#/.NET 개발자입니다.</span>
    <span data-lb="en">A C#/.NET developer <strong class="kw">8 years</strong> in — started writing software in high school.</span>
    <span data-lb="ja">高校在学中に開発を始め、<strong class="kw">8年目</strong>を迎えたC#/.NETエンジニアです。</span>
  </p>
  <ul class="about-list">
    <li class="about-item"><span data-lb="ko">Windows 데스크톱 · Avalonia 크로스플랫폼이 주력, C++ Native 연동까지 직접</span><span data-lb="en">Windows desktop and Avalonia cross-platform as the core, down to C++ native interop</span><span data-lb="ja">Windowsデスクトップ・Avaloniaクロスプラットフォームが主力、C++ Native連携まで担当</span></li>
    <li class="about-item"><span data-lb="ko">Java / Spring Boot 대용량 분산 환경 백엔드 경험</span><span data-lb="en">Backend experience in high-volume Java / Spring Boot distributed systems</span><span data-lb="ja">Java / Spring Boot 大容量分散環境のバックエンド経験</span></li>
    <li class="about-item"><span data-lb="ko">정량 목표를 먼저 정하고 수치로 결과를 증명하는 방식으로 일함</span><span data-lb="en">Sets a measurable target first, then proves the result with numbers</span><span data-lb="ja">定量目標を先に定め、数値で結果を証明する進め方</span></li>
  </ul>
</section>
```

---

## 4. 경력 — 회사 카드 → 플랫 컬럼

타임라인 바(`.tl-bar` 계열)는 유지, 높이만 58px. `.co-card` 패널(배경·테두리·배지·`.co-desc`·min-height) 전부 삭제.

### CSS
```css
.co-grid{display:grid;grid-template-columns:1fr 1fr;gap:0 40px;margin-top:28px}
.co-col{display:flex;flex-direction:column}
.co-head{display:flex;align-items:baseline;gap:10px;margin-bottom:4px}
.co-name{font-size:18px;font-weight:600;letter-spacing:-.02em;color:var(--fg)}
.co-dept{font-size:14px;color:var(--muted)}
.co-about{font-size:15px;color:var(--muted);margin-bottom:14px}
.co-list{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
.co-item{position:relative;padding-left:16px;font-size:16px;line-height:1.7;color:var(--body);word-break:keep-all}
.co-item::before{content:"";position:absolute;left:0;top:10px;width:5px;height:5px;border-radius:50%;background:var(--dot)}
```
모바일: `.co-grid{grid-template-columns:1fr;gap:28px}`.

### 템플릿 — 각 회사
```html
<div class="co-grid">
  <div class="co-col">
    <div class="co-head"><span class="co-name">…㈜휴엔시스템</span><span class="mono co-dept">…EIS · 주임</span></div>
    <div class="co-about">…플랜트 건설·엔지니어링 특화 솔루션 기업</div>
    <ul class="co-list">
      <li class="co-item">…플랜트 배관 도면 자동화 제품군 <strong class="kw">Windows 클라이언트 전담</strong></li>
      <li class="co-item">…도면 검색 속도 98% 개선, 심볼 좌표 자동 추출로 수작업 계산 70% 절감</li>
      <li class="co-item">…현대엔지니어링 8개+ 현장 · 삼성물산 평택 현장 기술 지원 직접 대응</li>
    </ul>
  </div>
  <div class="co-col">
    <div class="co-head"><span class="co-name">…㈜인라이플</span><span class="mono co-dept">…이지랩사업부 · 주임</span></div>
    <div class="co-about">…국내 1위 리타겟팅 광고 플랫폼과 국내 최초 PC형 앱스토어를 운영하는 데이터 테크 기업</div>
    <ul class="co-list">
      <li class="co-item">…자사 PC 제품군 <strong class="kw">공통 모듈 · 통합 인스톨러 플랫폼</strong> 설계·구축</li>
      <li class="co-item">…첫 제품 ezZip 기획부터 엔진 개발·운영 주도 → DAU 6만 명</li>
      <li class="co-item">…이전: Java/Spring 대용량 메시지 발송 플랫폼 iSend 백엔드</li>
    </ul>
  </div>
</div>
```
`…`는 기존 `data-l`/`data-lb` 3개 국어 span 패턴으로 감싼다. en/ja 문안은 §3과 같은 톤으로 기존 co-desc 문장에서 옮긴다(새 사실 금지).

---

## 5. 프로젝트 카드 — D8

`.proj-card` 규칙과 카드 템플릿 교체. 링크 행(`[data-cardlink]`)은 **삭제**(URL은 모달에만).

### CSS
```css
.proj-card{position:relative;aspect-ratio:3/4;border-radius:22px;overflow:hidden;background:var(--card);border:1px solid var(--line-soft);color:var(--fg);cursor:pointer;transition:background .15s}
.proj-card:hover{background:var(--card-hover)}
.pc-text{position:absolute;left:0;right:0;top:0;padding:24px 24px 0;display:flex;flex-direction:column;gap:12px;pointer-events:none}
.pc-eyebrow{font-size:14px;letter-spacing:.1em;color:var(--muted)}
.pc-title{margin:0;font-size:22px;line-height:1.25;letter-spacing:-.028em;font-weight:600;color:var(--fg)}
.pc-blurb{margin:0;font-size:16px;line-height:1.6;color:var(--sub);word-break:keep-all}
.pc-img{position:absolute;right:-8%;bottom:-6%;width:70%;aspect-ratio:1/1;pointer-events:none}
.pc-img img{width:100%;height:100%;object-fit:contain;object-position:right bottom;display:block}
```
모바일: `.proj-card{aspect-ratio:auto;min-height:0}` `.pc-text{position:static;padding:20px 20px 0}` `.pc-img{position:static;width:60%;margin:16px 0 0 auto;aspect-ratio:1/1}`.
인쇄: `.pc-img{display:none}` 또는 `object-fit:contain` 유지 후 `break-inside:avoid`.

### 템플릿
```html
<article class="proj-card" data-tech="{{ p.techAttr }}" onClick="{{ p.open }}">
  <div class="pc-text">
    <div class="mono pc-eyebrow">{{ p.co }} · {{ p.date }}</div>
    <h3 class="pc-title {{ p.h3cls }}">{{ p.title }}</h3>
    <p class="pc-blurb">{{ p.blurb }}</p>
  </div>
  <div class="pc-img"><img src="{{ p.img }}" alt="" loading="lazy"></div>
</article>
```
### 데이터
`PROJECTS[]`에 `img: 'assets/projects/<id>.png'` 추가. 이미지는 **배경 제거(누끼) PNG**, 정방형 권장, 우하단에 무게중심. 파일: `ezzip.png`, `isend.png`, `maketapp.png`, `ezspool.png`, `pc3d.png`, `bowoon.png`. 없는 항목은 `img` 생략 → `<img>` 렌더 안 함(`sc-if`).

---

## 6. 프로젝트 모달 — 1b 번호 레일

### CSS — `.m-flow*` 전부 교체
```css
.m-flow{display:flex;flex-direction:column}
.m-flow-sec{display:grid;grid-template-columns:44px 1fr;gap:0 18px}
.m-flow-rail{display:flex;flex-direction:column;align-items:center;gap:10px}
.m-flow-num{font-size:14px;font-weight:500;letter-spacing:.08em;line-height:24px;color:var(--muted)}
.m-flow-line{flex:1;width:1px;background:var(--line-ui)}
[data-flowlast] .m-flow-line{display:none}
.m-flow-body{display:flex;flex-direction:column;gap:12px;padding-bottom:30px}
[data-flowlast] .m-flow-body{padding-bottom:0}
.m-flow-title{font-size:18px;font-weight:600;letter-spacing:-.02em;line-height:24px;color:var(--fg)}
.m-flow-text{margin:0;font-size:16px;line-height:1.75;color:var(--body);word-break:keep-all}
.m-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,150px),1fr));gap:10px;margin-bottom:2px}
.m-stat{display:flex;flex-direction:column;gap:5px;padding:14px 16px 13px;background:var(--card-item);border:1px solid var(--line-card);border-radius:14px}
.m-stat-v{font-size:28px;font-weight:600;letter-spacing:-.03em;line-height:1;color:var(--fg)}
.m-stat-k{font-size:14px;letter-spacing:.08em;color:var(--muted)}
.m-flow-list{display:flex;flex-direction:column;gap:8px;list-style:none;padding:0;margin:0}
.m-flow-item{position:relative;padding-left:16px;font-size:16px;line-height:1.72;color:var(--body);word-break:keep-all}
.m-flow-item::before{content:"";position:absolute;left:0;top:11px;width:5px;height:5px;border-radius:50%;background:var(--dot)}
.m-flow-sec--ai .m-flow-num{color:var(--ai)}
.m-flow-sec--ai .m-flow-item::before{background:var(--ai)}
```
지우는 것: `.m-flow-title::before`(3px 바), `text-transform:uppercase`. 모바일: `.m-flow-sec{grid-template-columns:28px 1fr;gap:0 12px}` `.m-stats{grid-template-columns:1fr 1fr}` `.m-stat-v{font-size:24px}`.

### 템플릿 — 모달 본문
`<h3 class="modal-title">` 바로 아래 `<p class="modal-blurb">{{ p.blurb }}</p>` 추가(§2 순서 복원). 이어서:
```html
<div class="m-flow">
  <sc-for list="{{ p.flow }}" as="s" hint-placeholder-count="5">
    <div class="m-flow-sec {{ s.cls }}" data-flowlast="{{ s.last }}">
      <div class="m-flow-rail"><span class="mono m-flow-num">{{ s.num }}</span><span class="m-flow-line"></span></div>
      <div class="m-flow-body">
        <div class="m-flow-title">{{ s.title }}</div>
        <sc-if value="{{ s.isText }}"><p class="m-flow-text">{{ s.text }}</p></sc-if>
        <sc-if value="{{ s.hasStats }}"><div class="m-stats"><sc-for list="{{ s.stats }}" as="k" hint-placeholder-count="3"><div class="m-stat"><span class="m-stat-v">{{ k.v }}</span><span class="mono m-stat-k">{{ k.k }}</span></div></sc-for></div></sc-if>
        <sc-if value="{{ s.isList }}"><ul class="m-flow-list"><sc-for list="{{ s.items }}" as="c" hint-placeholder-count="2"><li class="m-flow-item">{{ c.text }}</li></sc-for></ul></sc-if>
      </div>
    </div>
  </sc-for>
</div>
```

### 스크립트 — `view()`
```js
const T5 = [['intro',null],['features',p.features],['metrics',p.metrics],['challenges',p.challenges],['ai',p.ai]];
const flow = [];
T5.forEach(([key, list], i) => {
  if (key !== 'intro' && !(list && list.length)) return;
  const sec = { num: '0' + (i + 1), title: t(T[key]), cls: key === 'ai' ? 'm-flow-sec--ai' : '', last: null };
  if (key === 'intro') { sec.isText = true; sec.text = t(p.intro || p.blurb); }
  else { sec.isList = true; sec.items = list.map(c => ({ text: bold(t(c)) })); }
  if (key === 'metrics') { sec.hasStats = !!(p.stats && p.stats.length); sec.stats = (p.stats || []).map(k => ({ v: t(k.v), k: t(k.k) })); }
  flow.push(sec);
});
flow[flow.length - 1].last = true;
// return { …기존, flow }  — titleIntro/Features/Metrics/Challenges/Ai 반환값 삭제
```
번호는 5단계 고정(AI 없는 프로젝트는 04에서 끝남).

### 데이터 — `stats` (기존 metrics 문장에서만)
```js
ezzip:    [{v:{ko:'6만 명',en:'60K',ja:'6万人'},k:{ko:'DAU',en:'DAU',ja:'DAU'}},{v:{ko:'1,800건',en:'1,800',ja:'1,800件'},k:{ko:'일 평균 설치',en:'DAILY INSTALLS',ja:'1日平均インストール'}},{v:{ko:'50%+',en:'50%+',ja:'50%+'},k:{ko:'실행 파일 크기 감축',en:'SMALLER BINARY',ja:'バイナリ削減'}}]
isend:    [{v:{ko:'90만+',en:'900K+',ja:'90万+'},k:{ko:'일 발송 건수',en:'MESSAGES / DAY',ja:'1日配信件数'}},{v:{ko:'30%',en:'30%',ja:'30%'},k:{ko:'주요 조회 성능 개선',en:'FASTER KEY QUERIES',ja:'主要照会性能改善'}}]
maketapp: [{v:{ko:'800개',en:'~800',ja:'800本'},k:{ko:'자동 빌드 앱',en:'APPS AUTO-BUILT',ja:'自動ビルド'}},{v:{ko:'75%',en:'75%',ja:'75%'},k:{ko:'웹뷰 로딩 단축',en:'FASTER WEBVIEW LOAD',ja:'WebView読込短縮'}}]
ezspool:  [{v:{ko:'98%',en:'98%',ja:'98%'},k:{ko:'도면 검색 속도 향상',en:'FASTER SEARCH',ja:'図面検索速度向上'}},{v:{ko:'70%',en:'70%',ja:'70%'},k:{ko:'수작업 계산 공수 단축',en:'LESS MANUAL CALC',ja:'手動計算工数削減'}}]
// pc3d, bowoon: stats 없음
```

---

## 7. 기타

- 챕터 헤더: 밑줄 없음(현행). 챕터 `padding-top` 96 → **80px**.
- 히어로 연락처 행 간격 9 → 10px.
- 인쇄: 프로젝트 카드 `.pc-img` 숨김, 모달은 현행(미포함) 유지.

---

## 8. 확인 (AGENTS.md §8)

1. `data-l` / `data-lb` ko·en·ja 개수 3개 언어 동일. 스크립트 `stats` 추가분(9항목 × v,k × 3언어)도 동일.
2. `grep -c '!important[;}]'` → 0 · `@media (max-width:720px)` → 1 · 구조 셀렉터 0 · 다크 리터럴(`light-dark(` 두 번째 인수 중 토큰 아닌 값) → 0.
3. 육안: 라이트/다크 × ko/en/ja × 데스크톱/720px — 히어로, About 리드+불릿, 타임라인 바(58px, 텍스트 안 넘침), 플랫 컬럼, 스택, 프로젝트 카드(이미지 우하단 잘림, 텍스트와 겹침 없음, 6장 높이 동일), 학력, 푸터.
4. 카드 → 모달: blurb → 스펙 → 01~05 레일, 성과 스탯 카드, AI 인디고, 720px 시트.
5. 인쇄 미리보기 라이트/다크.
6. AGENTS.md §8 통과값·날짜 갱신, `.document/History/`에 이 문서 사본 + ADR 1건(카드 링크 삭제·모달 5단계 고정).
