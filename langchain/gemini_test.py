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

# 입력설정
prompt = input("메시지 입력 :")

# 응답 생성
response = model.generate_content(prompt)

print(response.text)