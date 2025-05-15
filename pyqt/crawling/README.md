# Naver Knowledge iN WordCloud Generator

이 프로젝트는 **네이버 지식인(Naver Knowledge iN)** 에서 특정 키워드로 질문 데이터를 크롤링하고, 이를 기반으로 **워드클라우드 이미지를 생성**하는 Python GUI 응용 프로그램입니다.  
PyQt5 기반 GUI를 제공하며, 금지어 필터링 기능도 포함되어 있습니다.

---

## 실행 화면 예시

![UI](./assets/screenshot.png) <!-- 원하는 이미지 위치에 맞게 변경하세요 -->

---

## 주요 기능

- 네이버 지식인에서 키워드 검색 및 질문 수집
- 질문 제목만 추출 및 CSV 저장
- 금지어 필터링
- 워드클라우드 이미지 생성 및 표시
- PyQt5 GUI 제공

---

## 폴더 구조

```
.
├── ui/
│   └── wordcloud_main.ui       # PyQt5 UI 파일
├── data/                       # 크롤링된 CSV 및 워드클라우드 이미지 저장 폴더
├── lib/
│   ├── navercrawl_lib.py       # 지식인 크롤링 모듈
│   ├── wordcloud_lib.py        # 워드클라우드 생성 모듈
├── wordcloud_main.py           # 메인 GUI 실행 파일
├── test.py                     # 단독 테스트용 코드
└── README.md
```

---

## 실행 방법

### 1. 가상환경 생성 및 패키지 설치 (선택)
```bash
python -m venv venv
source venv/bin/activate  # 윈도우는 venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 의존 라이브러리 수동 설치
```bash
pip install PyQt5 beautifulsoup4 pandas wordcloud matplotlib
```

### 3. `.ui` 파일 → `.py` 변환 (필요시)
```bash
pyuic5 ui/wordcloud_main.ui -o ui_main.py
```

### 4. 실행
```bash
python wordcloud_main.py
```

---

## 주요 파일 설명

| 파일 | 설명 |
|------|------|
| `navercrawl_lib.py` | 네이버 지식인 검색어 기반 크롤러 |
| `wordcloud_lib.py` | 텍스트 전처리 및 워드클라우드 이미지 생성 |
| `wordcloud_main.py` | PyQt5 기반 GUI 실행 |
| `test.py` | CLI 기반 테스트 코드 |
| `ed_stopword.py` | 금지어 처리 테스트 코드 |
| `wordcloud_main.ui` | Qt Designer로 작성한 GUI 정의 파일 |

---

## 주의사항

- 한글 폰트를 `malgun.ttf`로 지정함 (`C:\Windows\Fonts\malgun.ttf`) → macOS는 별도 설정 필요
- 워드클라우드 이미지는 크롤링된 CSV와 동일한 이름의 `.png` 파일로 저장됨
- 네이버 페이지 구조 변경 시 크롤링 실패 가능성 있음

---

## 예시 사용 흐름

1. 키워드 입력 후 "검색"
2. 자동으로 CSV 파일 생성 및 경로 표시
3. 금지어 입력 후 "워드클라우드 생성"
4. 생성된 워드클라우드 이미지 확인

---

## 라이선스

본 프로젝트는 개인 학습 및 비상업적 목적에만 사용 가능합니다.
