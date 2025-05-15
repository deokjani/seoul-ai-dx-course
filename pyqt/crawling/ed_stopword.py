stopwords = "고양이, 고양이가, 고양이는"
print(stopwords)

# 문자열 분리
split_stopwords = stopwords.split(", ")
print(type(split_stopwords))

# strip_stopwords = []
# for word in split_stopwords:
#     strip_stopwords.append(word.strip())

strip_stopwords = [word.strip() for word in split_stopwords]
print(strip_stopwords)

# 정리
split_stopwords = stopwords.split(", ")
strip_stopwords = [word.strip() for word in split_stopwords]