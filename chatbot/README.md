
# AI Chatbot Sample (OpenAI GPT 기반 커스터마이징 챗봇)

## 프로젝트 개요

이 프로젝트는 OpenAI GPT 모델을 기반으로 한 간단한 커맨드라인 챗봇 애플리케이션입니다.  
시스템 역할 프롬프트를 통해 특정 캐릭터(예: 바리스타, AI 전문가)처럼 응답하는 챗봇을 구성할 수 있습니다.

## 파일 구성

| 파일명 | 설명 |
|--------|------|
| `chat_main.py` | 사용자 입력을 받아 챗봇과 대화하는 메인 실행 스크립트 |
| `openai_chat.py` | "AI 기술 설명 챗봇"용 시스템 역할 프롬프트 포함 |
| `openai_chat copy.py` | "커피 바리스타 챗봇"용 시스템 역할 프롬프트 포함 |

## 사용 방법

### 1. 패키지 설치

```bash
pip install openai
```

또는 아래와 같이 `requirements.txt`를 사용:

```bash
pip install -r requirements.txt
```

### 2. OpenAI API Key 설정

`openai_chat.py` 또는 `openai_chat copy.py` 내부의 `OPENAI_KEY` 변수에  
당신의 OpenAI API 키를 입력합니다:

```python
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

보안상 API 키는 외부에 노출되지 않도록 `.env` 또는 설정 파일로 관리하는 것이 권장됩니다.

## 실행 예시

```bash
python chat_main.py
```

이후 다음과 같이 입력을 진행합니다:

```
질문[q:종료]: 오늘 마실만한 커피 추천해줘
답변: 오늘은 에스프레소 마키아토를 추천합니다. ...
```

## 챗봇 모드 변경 방법

### 바리스타 챗봇을 사용하려면:
- `openai_chat copy.py` 내의 `ChatMessage()` 함수를 import 하세요.

```python
from openai_chat import ChatMessage  # → openai_chat copy.py 로 변경
```

### AI 기술 설명 챗봇을 사용하려면:
- 기본 `openai_chat.py` 사용

## 모델 설정

- 현재 모델은 `gpt-4o`로 지정되어 있으며, `gpt-3.5-turbo`도 사용 가능합니다.
- 생성 온도(temperature)는 `0.7`로 설정되어 있어 적당한 창의성을 유지합니다.

## 요구사항

- Python ≥ 3.8
- OpenAI Python SDK
- 인터넷 연결 (API 호출 필수)

## License

MIT License
