# 라이브러리 불러오기
import pandas as pd
import re
# wordCloud 라이브러리
from wordcloud import WordCloud
# 그래프 표시
import matplotlib.pyplot as plt

# 특수문자 제거
# 참조 : https://clolee.tistory.com/17
def clean_text(inputString):
    text_rmv = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', ' ', inputString)
    text_rmv = ' '.join(text_rmv.split())
    return text_rmv

def WordCloud_Create(filename, stopWord):
    # 파일 불러오기
    df_crawl = pd.read_csv(filename, encoding="cp949")
    # 특정 데이터를 삭제(drop)
    df = df_crawl.drop(['link'], axis='columns')
    # 리스트로 바꾸기
    list = df['text'].astype(str).tolist()
    # 리스트를 문자열로 변환
    word_str = ' '.join(s for s in list)
    # 특수문자 제거
    word_str_cut = clean_text(word_str)

    # 금지어 지정
    stopWords = []
    split_stopwords = stopWord.split(", ")
    strip_stopwords = [word.strip() for word in split_stopwords]

    wc1 = WordCloud(
        font_path = "c:\windows\fonts\malgun.ttf",
        stopwords = strip_stopwords,
        background_color = 'white',
        width = 1024,
        height = 768,
        random_state=42
    )

    
    wc1.generate(word_str_cut)

    saveWC = filename.replace('.csv', '.png')
    wc1.to_file(saveWC)

    return saveWC