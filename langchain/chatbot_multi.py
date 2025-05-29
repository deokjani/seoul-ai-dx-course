# 라이브러리 불러오기
import os
import google.generativeai as genai

# 키값 입력
GOOGLE_API_KEY = ""

# API 키 설정
genai.configure(api_key=GOOGLE_API_KEY)

# 모델 선택하기
model = genai.GenerativeModel(
    "gemini-2.0-flash"
)

# 멀티톤
chat_session =model.start_chat(history=[])
user_query = []

while True:
    prompt = input("메시지[q:종료] :")
    if prompt.lower() in ["exit", "quit", "q"]:
        print("채팅을 종료합니다.")
        exit()
    
    # 인공지능 메시지 처리(멀티톤)
    user_query.append(prompt)

    response = chat_session.send_message(prompt)
    print(f"AI : {response.text}")
