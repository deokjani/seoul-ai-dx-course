# 라이브러리 불러오기
import streamlit as st

# 인공지능 벡터디비 불러오기
# if not vectordb_load('rain'):
#     st.error("벡터DB 불러오기에 실패하였습니다.")
#     st.stop()

# 타이틀
st.title("랭체인 소나기소설 대화용 챗봇")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for content in st.session_state.chat_history:
    with st.chat_message(content["role"]):
        st.markdown(content["message"])

# 입력창
if prompt := st.chat_input("메시지를 입력하세요."):
    with st.chat_message("user"):
        st.markdown(prompt)
        st.session_state.chat_history.append({"role":"user", "message": prompt})

    with st.chat_message("ai"):
        response = f'{prompt} 내용이 입력되었습니다.'
        st.markdown(response)
        st.session_state.chat_history.append({"role":"ai", "message": response})
