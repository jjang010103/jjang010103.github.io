# 포트폴리오 리디자인 — 최종 반영 지시서

시안: `Project Detail.dc.html` (메인 라이트/다크 · 프로젝트 상세 라이트/다크 · 모바일 메인/상세). 이 문서가 단일 스펙이며 이전 patch 문서는 전부 폐기.
AGENTS.md 준수: 색은 `:root` 토큰만 · `!important` 0 · 모바일 미디어 블록 1개 · 3개 국어 짝 유지(§5) · 수치는 기존 문장에서만(§4) · 인쇄 1급.
**라이트 값은 §1에 명시된 것만 변경.**

---

## 0. 요약

1. 다크 토큰 교체 (3b 면 리프트 + 톤다운 중성 그레이)
2. 타입 스케일 상향 — 최소 14px
3. 히어로: 라벨·연락처 그리드 → 이름 + 문장 2개 (About 섹션 폐기, 흡수)
4. 경력: 타임라인 바 유지, 회사 카드 → 패널 없는 플랫 2컬럼
5. 프로젝트 카드: D8 (3:4 단색 카드 + 우하단 누끼 이미지), 필터·링크·챕터 메타 제거
6. 프로젝트 모달: 단일 컬럼 재구성, 구분선 없음, 03에 스탯 카드
7. 학력 배지 제거, 챕터 헤더 밑줄 없음(현행), 챕터 간격 80px

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
  --muted-2:light-dark(#8a8983,#7d7d82);
  --chip-bg:light-dark(#f7f6f3,#24242a);
  --chip-bc:light-dark(#dcdbd5,#4a4a54);
  --chip-fg:light-dark(#3f3f3a,#bebec2);
  --body:light-dark(#2b2a27,#cbcbce);
  --sub:light-dark(#45453f,#adadb1);
  --dot:light-dark(#6f6f68,#9a9aa3);
  --stripe:light-dark(#d3d1ca,#3c3c44);
  --slot:light-dark(#e6e5df,#26262c);
  --ai:light-dark(#4f46e5,#a5b4fc);
  --scrim:light-dark(rgba(20,20,19,.55),rgba(0,0,0,.7));
}
```
라이트 변경분: `--line` #e5e4e0→#dcdbd5 · `--line-ui` #dedcd6→#cfcdc6 · `--muted` #6f6f68→#5f5f59 · `--muted-2` → #8a8983(아이브로우/보조용, 기존보다 밝음) · `--chip-fg` #4a4a45→#3f3f3a.
`theme-color` 다크 `#0c0c0d`→`#101011`. 시트 안 `light-dark(` 리터럴은 전부 위 토큰으로 치환(다크 두 번째 인수에 토큰 외 값 0개).

---

## 2. 타입 스케일 (공통)

| 역할 | 값 |
|---|---|
| 모노 라벨·아이브로우·스펙 라벨·필터·푸터 소문 | **14** |
| 메타·소제목·세그 A/あ·연락처 | **15** |
| 본문·불릿·카드 요약·모달 본문 | **16** |
| 히어로 보조 문장 | **17** |
| 회사명(`.co-name`)·모달 섹션 제목 | **18 / 20** |
| 카드 제목 | **22** |
| 히어로 문장 | **24** |
| 챕터 h2 | **30** |
| 모달 제목 / 스탯 값 | **34 / 30** |
| 푸터 이름 / 이메일 | **42 / 27** |
| 히어로 h1 | 86 (유지) |

본문 `font-weight:300`→**400**. 모노 `letter-spacing` .12–.14em→**.08–.1em**. 불릿 점 4→**5px**(top 10–11px). 타임라인 바 52→**58px**.

---

## 3. 상단 바
현행 유지(로고·번호 내비·진행바·세그·아이콘). 폰트만 §2.

## 4. 히어로 (About 섹션 삭제 후 흡수)

```css
.hero{padding:64px 0 56px;border-bottom:1px solid var(--line)}
.hero-lead{margin:30px 0 0;font-size:24px;line-height:1.5;letter-spacing:-.018em;color:var(--fg);max-width:820px;text-wrap:pretty;word-break:keep-all}
.hero-lead a{color:var(--fg);text-decoration:underline;text-decoration-color:var(--line);text-underline-offset:4px;text-decoration-thickness:1px}
.hero-sub{margin:16px 0 0;font-size:17px;line-height:1.7;color:var(--muted);max-width:720px;word-break:keep-all}
.kw{background:var(--ink);color:var(--ink-fg);padding:.08em .32em .12em;margin:0 .04em;border-radius:3px;font-weight:600;box-decoration-break:clone;-webkit-box-decoration-break:clone}
```
```html
<header class="hero">
  <h1 class="hero-name">장민규</h1>  <!-- 기존 잉크 블록 그대로 -->
  <p class="hero-lead">
    <span data-lb="ko">고등학교 때 개발을 시작해 <strong class="kw">8년차</strong>가 된 C#/.NET 개발자. <a href="https://www.enliple.com" target="_blank" rel="noopener">인라이플</a>에서 압축 프로그램 <a href="https://ezlab.im/ko/tool/ezzip" target="_blank" rel="noopener">ezZip</a>과 자사 PC 제품군의 공통 플랫폼을 만들고 있습니다.</span>
    <span data-lb="en">A C#/.NET developer <strong class="kw">8 years</strong> in, since high school. At <a …>Enliple</a> I build <a …>ezZip</a> and the shared platform behind our PC products.</span>
    <span data-lb="ja">高校在学中に開発を始め、<strong class="kw">8年目</strong>のC#/.NETエンジニア。<a …>Enliple</a>で圧縮ソフト<a …>ezZip</a>と自社PC製品群の共通基盤を開発中。</span>
  </p>
  <p class="hero-sub">
    <span data-lb="ko">Windows 데스크톱 · Avalonia 크로스플랫폼이 주력, C++ Native 연동부터 Java / Spring Boot 대용량 백엔드까지 직접. 정량 목표를 먼저 정하고 수치로 결과를 증명합니다.</span>
    <span data-lb="en">Windows desktop and Avalonia cross-platform first; hands-on from C++ native interop to high-volume Java / Spring Boot backends. Set a measurable target, prove it with numbers.</span>
    <span data-lb="ja">Windowsデスクトップ・Avaloniaクロスプラットフォームが主力。C++ Native連携からJava / Spring Boot大容量バックエンドまで担当。定量目標を先に定め、数値で結果を証明。</span>
  </p>
</header>
```
삭제: 히어로 라벨 2줄, 연락처 4행 그리드, `<section class="about">` 전체 및 `.about-*` CSS. 연락처는 푸터에만.

## 5. 경력

타임라인 바 유지(58px). `.co-card` 패널(배경·테두리·배지·`.co-desc`·min-height) 삭제. 챕터 메타(`2018.09 → NOW`) 삭제.
```css
.co-grid{display:grid;grid-template-columns:1fr 1fr;gap:0 40px;margin-top:28px}
.co-head{display:flex;align-items:baseline;gap:10px;margin-bottom:4px}
.co-name{font-size:18px;font-weight:600;letter-spacing:-.02em;color:var(--fg)}
.co-dept{font-size:14px;color:var(--muted)}
.co-about{font-size:15px;color:var(--muted);margin-bottom:14px}
.co-list{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
.co-item{position:relative;padding-left:16px;font-size:16px;line-height:1.7;color:var(--body);word-break:keep-all}
.co-item::before{content:"";position:absolute;left:0;top:10px;width:5px;height:5px;border-radius:50%;background:var(--dot)}
```
불릿(ko, en/ja는 co-desc 문장에서 옮김 · 새 사실 금지):
- 휴엔시스템: `플랜트 배관 도면 자동화 제품군 <kw>Windows 클라이언트 전담</kw>` / `도면 검색 속도 98% 개선, 심볼 좌표 자동 추출로 수작업 계산 70% 절감` / `현대엔지니어링 8개+ 현장 · 삼성물산 평택 현장 기술 지원 직접 대응`
- 인라이플: `자사 PC 제품군 <kw>공통 모듈 · 통합 인스톨러 플랫폼</kw> 설계·구축` / `첫 제품 ezZip 기획부터 엔진 개발·운영 주도 → DAU 6만 명` / `이전: Java/Spring 대용량 메시지 발송 플랫폼 iSend 백엔드`

## 6. 기술 스택
현행(4열 카테고리 + 알약, 핵심만 잉크) 유지. 폰트 §2(라벨 14, 알약 15).

## 7. 프로젝트 카드 — D8

필터 칩 행·`6/6` 메타·`[data-cardlink]` 링크 행 **삭제**(URL은 모달로).
```css
.proj-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.proj-card{position:relative;aspect-ratio:3/4;border-radius:22px;overflow:hidden;background:var(--card);border:1px solid var(--line-soft);color:var(--fg);cursor:pointer;transition:background .15s}
.proj-card:hover{background:var(--card-hover)}
.pc-text{position:absolute;inset:0 0 auto 0;padding:24px 24px 0;display:flex;flex-direction:column;gap:12px;pointer-events:none}
.pc-eyebrow{font-size:14px;letter-spacing:.1em;color:var(--muted)}
.pc-title{margin:0;font-size:22px;line-height:1.25;letter-spacing:-.028em;font-weight:600}
.pc-blurb{margin:0;font-size:16px;line-height:1.6;color:var(--sub);word-break:keep-all}
.pc-img{position:absolute;right:-8%;bottom:-6%;width:70%;aspect-ratio:1/1;pointer-events:none}
.pc-img img{width:100%;height:100%;object-fit:contain;object-position:right bottom;display:block}
```
```html
<article class="proj-card" onClick="{{ p.open }}">
  <div class="pc-text"><div class="mono pc-eyebrow">{{ p.co }} · {{ p.date }}</div><h3 class="pc-title">{{ p.title }}</h3><p class="pc-blurb">{{ p.blurb }}</p></div>
  <sc-if value="{{ p.img }}"><div class="pc-img"><img src="{{ p.img }}" alt="" loading="lazy"></div></sc-if>
</article>
```
데이터: `PROJECTS[].img = 'assets/projects/<id>.png'` — 배경 제거(누끼) PNG, 정방형, 우하단 무게중심. `ezzip / isend / maketapp / ezspool / pc3d / bowoon`.

## 8. 학력 · 자격 · 병역
배지(`.edu-badge`) 삭제. 항목명 15/500, 메타 모노 14 muted. 3열 유지.

## 9. 프로젝트 모달 — 단일 컬럼

구분선 없음, 간격으로만. 폭 900px, 패딩 `22px 44px 40px`.
```css
.modal-card{width:min(900px,calc(100vw - 32px));background:var(--card);border:1px solid var(--line-soft);border-radius:24px;padding:22px 44px 40px}
.m-eyebrow{font-size:14px;letter-spacing:.1em;color:var(--muted)}
.modal-title{margin:10px 0 0;font-size:34px;font-weight:600;line-height:1.2;letter-spacing:-.03em}
.modal-blurb{margin:14px 0 0;font-size:18px;line-height:1.6;color:var(--sub);max-width:720px;text-wrap:pretty}
.m-link{margin-top:18px;font-size:15px}
.m-link a{color:var(--fg);text-decoration:underline;text-decoration-color:var(--line);text-underline-offset:5px;text-decoration-thickness:1px}
.m-stack{display:flex;flex-wrap:wrap;gap:6px;margin:36px 0 56px}
.m-stack .tag{font-size:14px;padding:5px 10px;border-radius:9px;border:1px solid var(--line-ui);color:var(--fg)}
.m-sec{display:flex;flex-direction:column;gap:12px;padding-bottom:44px}
.m-sec:last-child{padding-bottom:0}
.m-sec-h{display:flex;align-items:baseline;gap:12px}
.m-num{font-size:14px;letter-spacing:.1em;color:var(--muted-2)}
.m-sec--ai .m-num{color:var(--ai)}
.m-sec-t{font-size:20px;font-weight:600;letter-spacing:-.022em}
.m-text{margin:0;font-size:16px;line-height:1.75;color:var(--body)}
.m-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.m-stat{background:var(--card-item);border:1px solid var(--line-soft);border-radius:14px;padding:18px 20px 16px;display:flex;flex-direction:column;gap:6px}
.m-stat-v{font-size:30px;font-weight:600;letter-spacing:-.035em;line-height:1}
.m-stat-k{font-size:14px;letter-spacing:.08em;color:var(--muted)}
.m-list{display:flex;flex-direction:column;gap:8px;list-style:none;padding:0;margin:0}
.m-item{position:relative;padding-left:16px;font-size:16px;line-height:1.72;color:var(--body)}
.m-item::before{content:"";position:absolute;left:0;top:11px;width:5px;height:5px;border-radius:50%;background:var(--dot)}
.m-sec--ai .m-item::before{background:var(--ai)}
.m-foot{display:flex;justify-content:space-between;align-items:baseline;gap:24px;flex-wrap:wrap;margin-top:72px;font-size:14px;color:var(--muted-2)}
.m-foot a{color:var(--muted);text-decoration:none}
```
순서: 컨트롤 행(세그·테마·닫기, 현행) → `.m-eyebrow` `{{p.co}} · {{p.date}}` → `.modal-title` → `.modal-blurb` → `.m-link` 공식 웹사이트 ↗ → `.m-stack` → 섹션 01~05 → `.m-foot`(`장민규 · C#/.NET 개발자 · 8년차` | 이메일 · GitHub ↗ · LinkedIn ↗).
섹션 03은 제목 아래 `.m-stats` 먼저, 그다음 불릿. 번호 레일·3px 바·uppercase·역할(ROLE)·스펙 그리드·하단 서명 블록 **삭제**.

### `view()`
```js
const T5=[['intro',null],['features',p.features],['metrics',p.metrics],['challenges',p.challenges],['ai',p.ai]];
const flow=[];
T5.forEach(([key,list],i)=>{
  if(key!=='intro'&&!(list&&list.length))return;
  const s={num:'0'+(i+1),title:t(T[key]),cls:key==='ai'?'m-sec--ai':''};
  if(key==='intro'){s.isText=true;s.text=t(p.intro||p.blurb);}else{s.isList=true;s.items=list.map(c=>({text:bold(t(c))}));}
  if(key==='metrics'){s.hasStats=!!(p.stats&&p.stats.length);s.stats=(p.stats||[]).map(k=>({v:t(k.v),k:t(k.k)}));}
  flow.push(s);
});
// return {…, flow}; titleIntro/Features/Metrics/Challenges/Ai 삭제
```
### `stats` 데이터 (기존 metrics 문장에서만)
```js
ezzip:[{v:{ko:'6만 명',en:'60K',ja:'6万人'},k:{ko:'DAU',en:'DAU',ja:'DAU'}},{v:{ko:'1,800건',en:'1,800',ja:'1,800件'},k:{ko:'일 평균 설치',en:'DAILY INSTALLS',ja:'1日平均インストール'}},{v:{ko:'50%+',en:'50%+',ja:'50%+'},k:{ko:'실행 파일 크기 감축',en:'SMALLER BINARY',ja:'バイナリ削減'}}]
isend:[{v:{ko:'90만+',en:'900K+',ja:'90万+'},k:{ko:'일 발송 건수',en:'MESSAGES / DAY',ja:'1日配信件数'}},{v:{ko:'30%',en:'30%',ja:'30%'},k:{ko:'주요 조회 성능 개선',en:'FASTER KEY QUERIES',ja:'主要照会性能改善'}}]
maketapp:[{v:{ko:'800개',en:'~800',ja:'800本'},k:{ko:'자동 빌드 앱',en:'APPS AUTO-BUILT',ja:'自動ビルド'}},{v:{ko:'75%',en:'75%',ja:'75%'},k:{ko:'웹뷰 로딩 단축',en:'FASTER WEBVIEW LOAD',ja:'WebView読込短縮'}}]
ezspool:[{v:{ko:'98%',en:'98%',ja:'98%'},k:{ko:'도면 검색 속도 향상',en:'FASTER SEARCH',ja:'図面検索速度向上'}},{v:{ko:'70%',en:'70%',ja:'70%'},k:{ko:'수작업 계산 공수 단축',en:'LESS MANUAL CALC',ja:'手動計算工数削減'}}]
// pc3d, bowoon: 없음
```

## 10. 모바일 (`@media (max-width:720px)` 블록 안에만)

- 상단 바: 내비 숨김, 로고 20px + 세그·아이콘만
- 히어로: h1 52px, `.hero-lead` 19px, `.hero-sub` 15px, 패딩 `40px 0`
- 타임라인 바: 높이 44px, 회사명만(기간 span 숨김) → 기간은 `.co-col`에 `.co-date`(모노 14, muted-2)로 표시
- `.co-grid{grid-template-columns:1fr;gap:32px}`
- 스택 4열 → 1열, 알약 14px
- `.proj-grid{grid-template-columns:1fr}` `.proj-card{aspect-ratio:4/5}` `.pc-text{padding:20px 20px 0;gap:10px}` `.pc-title{font-size:21px}` `.pc-blurb{font-size:15px}` `.pc-img{width:62%}`
- 학력 3열 → 1열
- 푸터: 1열 스택, 이름 30px, 이메일 18px `word-break:break-all`
- 모달: 하단 시트 — `width:100%;height:92vh;border-radius:24px 24px 0 0;padding:14px 20px 40px`, 상단 그랩 핸들(36×4, `--line-ui`), 제목 27px, blurb 16px, 본문 15px, `.m-stats{grid-template-columns:1fr 1fr}` `.m-stat-v{font-size:26px}`, 섹션 간격 38px, 시트 하단 페이드(`--card`로 120px)

## 11. 인쇄
`.pc-img` 숨김, 카드 `break-inside:avoid`. 모달은 현행(미포함) 유지.

## 12. 확인 (§8)
1. `data-l`/`data-lb` 3개 국어 개수 동일 · `stats` 추가분(9×2×3) 동일
2. `!important` 0 · 모바일 블록 1 · 구조 셀렉터 0 · 다크 리터럴 0
3. 라이트/다크 × ko/en/ja × 데스크톱/390px: 히어로 문장 줄바꿈, 바 58/44px 안 넘침, 카드 6장 높이 동일·텍스트와 이미지 겹침 없음, 모달 스탯·알약 줄바꿈
4. 카드→모달 순서(아이브로우→제목→blurb→링크→스택→01~05→푸터 줄), 03 스탯 카드
5. 인쇄 미리보기 라이트/다크
6. AGENTS.md §8 통과값·날짜 갱신, `.document/History/`에 사본 + ADR(카드 링크·필터 삭제, About 흡수, 모달 단일 컬럼)
