# 3b 「면 리프트」 다크 테마 → index.html 반영 패치

진단: 현재 다크는 배경 #0c0c0d ↔ 카드 #161618 명도차 1.2배(카드 경계 소멸), 헤어라인 #232329 대비 1.4:1, 반전 블록 17:1 눈부심.
3b는 배경은 깊게 두고 카드·아이템·테두리를 뚜렷하게 띄운다. **라이트 값(light-dark 첫 인수)은 건드리지 않는다.**
AGENTS.md 규칙: 색은 `:root` 토큰에서만, `!important` 없음, 모바일 블록 1개 유지.

---

## 1. `:root` — light-dark() 두 번째 값 교체

```css
:root{
  color-scheme:light dark;
  --bg:light-dark(#fbfbf9,#0d0d0e);
  --fg:light-dark(#1c1b19,#f1f1f3);
  --ink:light-dark(#151514,#f1f1f3);
  --ink-fg:light-dark(#fbfbf9,#0d0d0e);
  --card:light-dark(#f1f1f0,#1c1c20);
  --card-hover:light-dark(#eaeae9,#222227);
  --card-item:light-dark(#fbfbf9,#292930);
  --line:light-dark(#e5e4e0,#2a2a30);
  --line-soft:light-dark(#e9e8e4,#232328);
  --line-card:light-dark(#e5e4de,#35353d);
  --line-ui:light-dark(#dedcd6,#41414a);
  --muted:light-dark(#6f6f68,#a9a9b3);
  --muted-2:light-dark(#63635d,#b9b9c2);
  --chip-bg:light-dark(#f7f6f3,#24242a);
  --chip-bc:light-dark(#e5e4e0,#41414a);
  --chip-fg:light-dark(#4a4a45,#c6c6ce);
  --ai:light-dark(#4f46e5,#a5b4fc);
}
```

## 2. 토큰 밖에 박힌 다크 리터럴 교체 (두 번째 인수만)

시트에서 `light-dark(` 를 검색해 아래 값으로 바꾼다. 같은 옛 값은 전부 같은 새 값으로.

| 옛 다크 값 | 새 값 | 쓰이는 곳 |
|---|---|---|
| `#ececed` | `#f6f6f8` | 제목·이름·링크 (.modal-title, .spec-co, .m-flow-title, .m-stat-v, .mfoot-name, [data-cardlink] a, .spec-linkrow a, .mfoot-links a) |
| `#dcdcdf` | `#e6e6ea` | .tag 글자, .spec-date, .m-flow-text, .m-flow-item |
| `#c9c9cf` | `#d9d9de` | .about-body, .spec-role |
| `#a8a8b2` | `#b4b4be` | .modal-blurb |
| `#9a9aa2` | `#a4a4ae` | .card-blurb |
| `#858590` | `#9c9ca6` | .speclabel |
| `#a5a5ad` | `#c6c6ce` | .logo-btn |
| `#a2a2ad` | `#a9a9b3` | .icon-btn--close |
| `#76757d` | `#8d8d97` | .m-flow-item::before (불릿) |
| `#6a6a73` | `#7c7c86` | [data-rowarrow] |
| `#1b1b20` / `#282830` | `#292930` / `#454550` | .tag 배경 / 테두리 |
| `#2a2a30` (icon-btn 테두리) | `#41414a` | .icon-btn |
| `#26262b` | `#33333a` | .tl-gap 스트라이프 |

`.proj-card`, `.co-card`는 `border:1px solid transparent` → `border-color:var(--line-soft)`로 바꿔 다크에서 카드 외곽이 잡히게 한다(라이트에선 #e9e8e4로 거의 안 보이므로 부작용 없음).

## 3. 기타

- `<meta name="theme-color">` 스크립트의 `'#0c0c0d'` → `'#0d0d0e'`
- `[data-modal]` 오버레이 `rgba(0,0,0,.76)` → `rgba(0,0,0,.7)` (카드가 밝아졐으므로 살짝 완화)
- `::selection` 다크 값은 그대로.

## 4. 확인 (§8)

- 라이트 렌더가 픽셀 단위로 변하지 않았는지(첫 인수 미변경) 스크린샷 비교.
- 다크: 메인(바·인트로·타임라인·회사카드·스택·프로젝트 카드·학력·푸터) → 모달(1b 레일·스탯 카드) → 720px 시트 → 3개 언어.
- 대비 확인 목표: 카드/배경 ≥1.6배, 헤어라인/배경 ≥2:1, `--muted`/`--card` ≥ 4.5:1.
- `grep -c '!important[;}]'` 0 · 모바일 블록 1 · 구조 셀렉터 0 유지, AGENTS.md §8 통과값·날짜 갱신.
