# CV Updates - December 2025

## 변경사항 요약

### 1. Last Updated Date - Git 기반 자동 업데이트

**변경 전:**
- `\today` 사용 (현재 빌드 날짜)

**변경 후:**
- 최근 git commit 날짜 사용
- `update_date.py` 스크립트가 자동으로 `git_date.tex` 파일 생성
- CV 빌드 시 자동으로 반영

**파일 변경:**
- `cv-taewon.tex` (86번 줄): `\today` → `\input{git_date.tex}`
- **신규**: `update_date.py` - Git 날짜 추출 스크립트
- **신규**: `git_date.tex` - 생성된 날짜 파일 (gitignore 추가 권장)

---

### 2. 주저자/교신저자 표시 - 이름 뒤 별표(*) 추가

**변경 전:**
- 이름만 **볼드** 처리

**변경 후:**
- 이름 **볼드** + **별표(*)** 추가
- 예: **Taewon Song***

**파일 변경:**
- `settings.sty` (131번 줄): `\textbf{#1}` → `\textbf{#1}$^{*}$`

**작동 방식:**
- `cv-taewon.tex`에 정의된 `\mynames` 리스트 사용:
  ```latex
  \mynames{
    Song/Tae-Won,
    Song/Taewon,
    Song*/Tae-Won,    % 교신저자 표시용
    Song*/Taewon,     % 교신저자 표시용
  }
  ```
- Bibliography에서 자동으로 매칭하여 강조

---

## 빌드 방법

### 자동 빌드 (권장)

```bash
./build_cv.sh
```

이 스크립트는 자동으로:
1. Git 커밋 날짜 업데이트 (`update_date.py` 실행)
2. LaTeX 빌드 (`latexmk -pdf`)

### 수동 빌드

```bash
# Step 1: Update git date
python3 update_date.py

# Step 2: Build PDF
latexmk -pdf cv-taewon.tex
```

---

## 추가 파일

### 새로 생성된 파일

1. **`update_date.py`** - Git 날짜 추출 스크립트
   - 최근 커밋 날짜를 YYYY-MM-DD 형식으로 추출
   - `git_date.tex` 파일 생성
   - 실패 시 현재 날짜로 fallback

2. **`build_cv.sh`** - 자동 빌드 스크립트
   - Git 날짜 업데이트 + LaTeX 빌드 자동화
   - 실행 가능 (chmod +x)

3. **`git_date.tex`** - 생성된 날짜 파일
   - Git에서 자동 생성되므로 **`.gitignore`에 추가 권장**

---

## .gitignore 권장 추가

```gitignore
# Generated files
git_date.tex
```

---

## 검증 방법

### 1. Last Updated 확인

```bash
# 현재 git 날짜 확인
git log -1 --format=%cd --date=format:'%Y-%m-%d'

# CV PDF 빌드
./build_cv.sh

# PDF 열어서 우측 상단 "Date of revision" 확인
```

### 2. 주저자/교신저자 별표 확인

PDF의 "Research Publications" 섹션에서:
- 본인 이름(Taewon Song)이 **볼드**로 표시
- 주저자 또는 교신저자인 경우 이름 뒤에 ***가 추가됨

---

## 문제 해결

### Git 날짜가 업데이트되지 않을 때

```bash
# 수동으로 날짜 파일 생성
python3 update_date.py

# 날짜 파일 확인
cat git_date.tex

# 출력 예시: 2025-10-06
```

### 별표가 표시되지 않을 때

`own-bib.bib` 파일에서 저자 이름이 정확한지 확인:
- ✅ 올바른 예: `author = {Song*, Taewon and ...}`
- ❌ 잘못된 예: `author = {Song, Taewon* and ...}` (별표 위치 잘못)

`cv-taewon.tex`의 `\mynames` 리스트에 `Song*/Taewon` 포함되어 있는지 확인.

---

## 향후 개선 사항 (Optional)

### 1. GitHub Actions 통합

`.github/workflows/build-cv.yml`:
```yaml
- name: Update git date
  run: python3 update_date.py

- name: Build PDF
  run: latexmk -pdf cv-taewon.tex
```

### 2. Pre-commit Hook

`.git/hooks/pre-commit`:
```bash
#!/bin/bash
python3 update_date.py
git add git_date.tex
```

---

## 변경 내역

| 날짜 | 변경 내용 | 파일 |
|------|-----------|------|
| 2025-12-02 | Git 기반 날짜 자동 업데이트 구현 | cv-taewon.tex, update_date.py |
| 2025-12-02 | 주저자/교신저자 별표 표시 추가 | settings.sty |
| 2025-12-02 | 자동 빌드 스크립트 추가 | build_cv.sh |

---

**작성자**: Claude
**마지막 업데이트**: 2025-12-02
