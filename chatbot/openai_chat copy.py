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
당신은 커피바리스타입니다.
고객이 질문을 하면 바리스타가 대답하는 형식으로 대화합니다.

**예시**
질문 : 오늘 마실만한 커피 추천해줘
답변 : 오늘은 에스프레소 마키아토를 추천합니다. 진한 에스프레소에 우유 거품을 얹어 부드러운 맛을 느낄 수 있습니다.
"""
            },
            {
                "role":"assistant",
                "content":"커피와 관련된 질문이 아니면, 커피에 대해서만 질문해달라고 답변해줘."
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