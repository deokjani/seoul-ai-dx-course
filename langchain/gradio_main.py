import gradio as gr
import random
import time

# 인공지능 라이브러리 불러오기
from chatbot_gemini_lib import vectordb_load, chat_query

# 벡터DB 불러오기
if vectordb_load('rain') == False:
    print("벡터디비 불러오기 에러...")
    exit()

with gr.Blocks(title="GEMINI 소나기소설 챗봇") as demo:
    gr.Markdown("# GEMINI 소나기소설 챗봇")
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox(label="AI와 대화할 내용을 입력하세요.")
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = chat_query(message)
        # bot_message = random.choice(["How are you?", "Today is a great day", "I'm very hungry"])
        chat_history.append({"role": "user", "content": message})
        chat_history.append({"role": "assistant", "content": bot_message})
        time.sleep(2)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()