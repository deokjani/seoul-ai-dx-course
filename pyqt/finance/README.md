# 실시간 주식 데이터 조회 GUI - PyQt5 + FinanceDataReader

이 프로젝트는 PyQt5 GUI를 통해 **삼성전자 등 주요 종목의 실시간 주가, 5일 평균, 주가 추세(상승/하락/보합)** 등을 확인할 수 있는 프로그램입니다.  
FinanceDataReader를 통해 주가 데이터를 가져오며, 주기적으로 자동 갱신됩니다.

---

## 주요 기능

- 국내 주요 종목(삼성전자, 삼성물산 등) 주가 조회
- 5일 평균 계산 및 주가 추세 비교
- 실시간 데이터 갱신 (5초 간격)
- 날짜 표시 및 테이블 형태 출력
- 종료 버튼 포함

---

## 실행 화면 예시

> `finance_main.ui` 기반 GUI (Qt Designer)

---

## 폴더 구조

```
.
├── finance_main.py       # 메인 GUI 실행 파일
├── finance_main.ui       # PyQt5 UI 정의 파일
├── finance_test.py       # FinanceDataReader 기능 테스트용
├── date_test.py          # 날짜 출력 테스트용
├── requirements.txt      # 의존성 목록
```

---

## 실행 방법

### 1. 가상환경 생성 및 패키지 설치
```bash
python -m venv venv
source venv/bin/activate  # 윈도우는 venv\Scripts\activate
pip install -r requirements.txt
```

### 2. 실행
```bash
python finance_main.py
```

---

## requirements.txt 내용

- PyQt5
- FinanceDataReader
- pandas

---

## 참고 사항

- `FinanceDataReader`는 주가 데이터를 온라인으로 가져오므로 인터넷 연결이 필요합니다.
- UI 파일(`finance_main.ui`)은 Qt Designer로 수정 가능합니다.
- GUI는 5초 간격으로 주가 데이터를 자동 갱신합니다.

---

## 라이선스

본 프로젝트는 비상업적 학습 목적에 한해 자유롭게 사용 가능합니다.
