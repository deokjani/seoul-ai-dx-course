# 1. 라이브러리 가져오기
import openai

# 2. 환경설정
OPENAI_KEY = "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"
openai.api_key = OPENAI_KEY

# 3. 인공지능 모델 선택
MODEL = "gpt-4o"  # gpt-3.5-turbo, gpt-4

# 4. ChatTing 모듈
def ChatMessage(msg):
    response = openai.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role":"system",
                "content":"""
인공지능에 대한 질문을 받는 챗봇입니다.
질문에 대한 내용을 설명을 해줄때, 전문적인 용어로 기술적인 내용위주로 설명해줘.

**예시**
질문 : Tensorflow란 무엇인가요?
답변 : Tensorflow는 구글에서 개발한 오픈소스 머신러닝 라이브러리로, 데이터 플로우 그래프를 사용하여 수치 계산을 수행합니다. 주로 딥러닝 모델을 구축하고 훈련하는 데 사용되며, 다양한 플랫폼에서 실행할 수 있는 유연성과 확장성을 제공합니다.
"""
            },
            {
                "role":"assistant",
                "content":"인공지능에대한 질문이 있으면 전문적인 용어로 기술적인 내용위주로 설명해줘."
            },
            {
                "role":"user",
                "content":msg
            }
        ],
        temperature=0.7,
    )

    # print(response)

    return response.choices[0].message.content