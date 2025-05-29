# 라이브러리 불러오기
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import Chroma

api_key = ''
os.environ["GOOGLE_API_KEY"] = api_key

# pdf 파일 불러오기
try:
    loader = PyPDFLoader("./source/rain.pdf")
except:
    print("PDF 파일이 존재하지 않습니다.")
    exit()

document = loader.load()
# print(document)
print()
print("="*30 + " PDF Loader " + "="*30)
print(f"문서의 길이 : {len(document)} 페이지")
print(f"미리 보기 : {document[0].page_content[:100]}...")

# 문서의 데이터를 분활(Split)
print()
print("="*30 + " CharacterTextSplitter " + "="*30)

text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=100
)
sp_texts = text_splitter.split_documents(document)
print(f"분할문서 길이 : {len(sp_texts)} 개")
print(f"분할문서 보기 : {sp_texts[0].page_content[:100]}...")
print(f"분할문서 보기 : {sp_texts[1].page_content[:100]}...")

# LangChain의 VectorDB 생성
# 임베딩
embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-exp-03-07"
)
# ChromaDB 생성
db = Chroma.from_documents(
    documents=sp_texts,
    embedding=embeddings,
    persist_directory="./vectordb/rain",
    collection_name="rain_collection"
)

# 임베딩 데이터를 확인
db.get()