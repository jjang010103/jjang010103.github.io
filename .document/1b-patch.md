# 1b 「번호 레일」 → index.html 반영 패치

AGENTS.md 규칙에 맞춤: 정적 스타일은 `<style>`에만, 모바일은 하단 `@media (max-width:720px)` 블록 한 곳, `!important`·구조 셀렉터 없음, 색은 토큰.
수치는 기존 `PROJECTS[].metrics` 문장에 있는 값만 옮겼다(§4). 없는 프로젝트(pc3d, mobile)는 `stats`를 두지 않는다 — `sc-if`가 카드 줄을 숨긴다.

---

## 1. `:root` — 토큰 1개 추가

```css
--ai:light-dark(#4f46e5,#818cf8);            /* AI 협업 섹션 강조 */
```

## 2. `<style>` — `/* ── project modal ── */` 안의 `.m-flow*` 규칙 전부를 아래로 교체

```css
.m-flow{display:flex;flex-direction:column}
.m-flow-sec{display:grid;grid-template-columns:44px 1fr;gap:0 18px}
.m-flow-rail{display:flex;flex-direction:column;align-items:center;gap:10px}
.m-flow-num{font-size:12px;font-weight:500;letter-spacing:.08em;line-height:22px;color:var(--muted)}
.m-flow-line{flex:1;width:1px;background:var(--line-ui)}
[data-flowlast] .m-flow-line{display:none}
.m-flow-body{display:flex;flex-direction:column;gap:12px;padding-bottom:30px}
[data-flowlast] .m-flow-body{padding-bottom:0}
.m-flow-title{font-size:16px;font-weight:600;letter-spacing:-.02em;line-height:22px;color:light-dark(#151514,#ececed)}
.m-flow-text{margin:0;font-size:15px;line-height:1.75;font-weight:300;color:light-dark(#2b2a27,#dcdcdf);word-break:keep-all}
.m-stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,150px),1fr));gap:10px;margin-bottom:2px}
.m-stat{display:flex;flex-direction:column;gap:5px;padding:14px 16px 13px;background:var(--card-item);border:1px solid var(--line-card);corner-shape:squircle;border-radius:14px}
.m-stat-v{font-size:26px;font-weight:600;letter-spacing:-.03em;line-height:1;color:light-dark(#151514,#ececed)}
.m-stat-k{font-size:11px;letter-spacing:.08em;color:var(--muted)}
.m-flow-list{display:flex;flex-direction:column;gap:8px;list-style:none;padding:0;margin:0}
.m-flow-item{position:relative;padding-left:14px;font-size:14.5px;line-height:1.72;font-weight:300;color:light-dark(#2b2a27,#dcdcdf);word-break:keep-all}
.m-flow-item::before{content:"";position:absolute;left:0;top:10px;width:4px;height:4px;border-radius:50%;background:light-dark(#8c8b85,#76757d)}
.m-flow-item strong{background:var(--ink);color:var(--ink-fg);padding:.08em .32em .12em;margin:0 .04em;border-radius:3px;font-weight:600;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.m-flow-sec--ai .m-flow-num{color:var(--ai)}
.m-flow-sec--ai .m-flow-item::before{background:var(--ai)}
```

> 지운 것: `.m-flow-title::before`(3px 바), `text-transform:uppercase`, `.m-flow-sec--ai .m-flow-title` 색 재정의.
> 모바일 블록 끝의 `[data-contrib-item]`, `[data-contrib-text]` 두 줄은 이미 템플릿에 없는 훅이니 같이 지운다.

## 3. `@media (max-width:720px)` 블록 안 — 모달 부분 끝에 추가

```css
  .m-flow-sec{grid-template-columns:28px 1fr;gap:0 12px}
  .m-flow-body{padding-bottom:24px;gap:10px}
  .m-flow-title{font-size:15.5px}
  .m-flow-text{font-size:14.5px}
  .m-stats{grid-template-columns:1fr 1fr}
  .m-stat{padding:12px 14px 11px}
  .m-stat-v{font-size:22px}
```

## 4. 템플릿 — `<div class="m-flow">…</div>` 전체를 교체

5개의 `sc-if` 블록 → `p.flow` 루프 하나. 번호는 5단계 고정(01~05)이라 AI가 없는 프로젝트는 04에서 끝난다 — 빈 단계를 숨기는 게 아니라 "없음"이 보이도록.

```html
<div class="m-flow">
  <sc-for list="{{ p.flow }}" as="s" hint-placeholder-count="5">
    <div class="m-flow-sec {{ s.cls }}" data-flowlast="{{ s.last }}">
      <div class="m-flow-rail">
        <span class="mono m-flow-num">{{ s.num }}</span>
        <span class="m-flow-line"></span>
      </div>
      <div class="m-flow-body">
        <div class="m-flow-title">{{ s.title }}</div>
        <sc-if value="{{ s.isText }}">
          <p class="m-flow-text">{{ s.text }}</p>
        </sc-if>
        <sc-if value="{{ s.hasStats }}">
          <div class="m-stats">
            <sc-for list="{{ s.stats }}" as="k" hint-placeholder-count="3">
              <div class="m-stat"><span class="m-stat-v">{{ k.v }}</span><span class="mono m-stat-k">{{ k.k }}</span></div>
            </sc-for>
          </div>
        </sc-if>
        <sc-if value="{{ s.isList }}">
          <ul class="m-flow-list">
            <sc-for list="{{ s.items }}" as="c" hint-placeholder-count="2">
              <li class="m-flow-item">{{ c.text }}</li>
            </sc-for>
          </ul>
        </sc-if>
      </div>
    </div>
  </sc-for>
</div>
```

## 5. 스크립트 — `view()` 안의 features/metrics/challenges/ai 계산을 `flow`로 통합

```js
const view = (p) => {
  const T5 = [
    ['intro', null],
    ['features', p.features],
    ['metrics', p.metrics],
    ['challenges', p.challenges],
    ['ai', p.ai]
  ];
  const flow = [];
  T5.forEach(([key, list], i) => {
    if (key !== 'intro' && !(list && list.length)) return;
    const sec = { num: '0' + (i + 1), title: t(T[key]), cls: key === 'ai' ? 'm-flow-sec--ai' : '', last: null };
    if (key === 'intro') { sec.isText = true; sec.text = t(p.intro || p.blurb); }
    else { sec.isList = true; sec.items = list.map(c => ({ text: bold(t(c)) })); }
    if (key === 'metrics') {
      sec.hasStats = !!(p.stats && p.stats.length);
      sec.stats = (p.stats || []).map(k => ({ v: t(k.v), k: t(k.k) }));
    }
    flow.push(sec);
  });
  flow[flow.length - 1].last = true;
  return {
    id: p.id, co: t(p.co), coFull: t(p.coFull), date: p.date, url: p.url,
    title: t(p.title), mtitle: t(p.mtitle), blurb: t(p.blurb), role: t(p.role),
    stack: p.stack, h3cls: p.feature ? 'card-title--feature' : '',
    flow
  };
};
```

`titleIntro / titleFeatures / titleMetrics / titleChallenges / titleAi` 반환값은 더 안 쓰므로 지운다.

## 6. 데이터 — `PROJECTS[]`에 `stats` 추가 (metrics 문장에서 그대로 옮김)

```js
// ezzip
stats: [
  { v: { ko: '6만 명', en: '60K', ja: '6万人' },      k: { ko: 'DAU', en: 'DAU', ja: 'DAU' } },
  { v: { ko: '1,800건', en: '1,800', ja: '1,800件' }, k: { ko: '일 평균 설치', en: 'DAILY INSTALLS', ja: '1日平均インストール' } },
  { v: { ko: '50%+', en: '50%+', ja: '50%+' },        k: { ko: '실행 파일 크기 감축', en: 'SMALLER BINARY', ja: 'バイナリ削減' } }
],
// isend
stats: [
  { v: { ko: '90만+', en: '900K+', ja: '90万+' }, k: { ko: '일 발송 건수', en: 'MESSAGES / DAY', ja: '1日配信件数' } },
  { v: { ko: '30%', en: '30%', ja: '30%' },       k: { ko: '주요 조회 성능 개선', en: 'FASTER KEY QUERIES', ja: '主要照会性能改善' } }
],
// maketapp
stats: [
  { v: { ko: '800개', en: '~800', ja: '800本' },          k: { ko: '자동 빌드 앱', en: 'APPS AUTO-BUILT', ja: '自動ビルド' } },
  { v: { ko: '1일→1시간', en: '1d → 1h', ja: '1日→1時間' }, k: { ko: '제작 소요 시간', en: 'BUILD TIME', ja: '制作時間' } }
],
// ezspool
stats: [
  { v: { ko: '98%', en: '98%', ja: '98%' }, k: { ko: '도면 검색 속도 향상', en: 'FASTER SEARCH', ja: '図面検索速度向上' } },
  { v: { ko: '70%', en: '70%', ja: '70%' }, k: { ko: '수작업 계산 공수 단축', en: 'LESS MANUAL CALC', ja: '手動計算工数削減' } }
],
// pc3d, mobile — stats 없음 (Zero Leak·FCM은 수치가 아님)
```

## 7. 확인 (§8)

- 스크립트 ko/en/ja 개수: `stats` 18개 항목 × 2 = +36씩 동일하게 늘어난다 → 세 숫자가 같아야 한다.
- `grep -c '!important[;}]'` → 0, 모바일 블록 → 1, 구조 셀렉터 → 0 유지.
- 카드 → 모달 → 3개 언어 → 라이트/다크(`--ai` 토큰) → 720px 시트 → 인쇄 미리보기.
