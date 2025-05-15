# OpenAI 채팅 함수 불러오기
from openai_chat import ChatMessage

# 채팅하기
while True:
    msg = input("질문[q:종료]:")
    if msg == "q":
        exit()
    rst = ChatMessage(msg)
    print(rst)