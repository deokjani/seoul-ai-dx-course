import csv
import time
import random
from datetime import datetime

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
from urllib.parse import quote_plus

# 날짜로 파일명 만드는 함수
def gen_filename(search):
    current_time = datetime.now()
    date_part = current_time.strftime("%Y%m%d")
    time_part = current_time.strftime("%H%M%S")
    return f"./data/{date_part}_{time_part}_{search}.csv"

def search_naver_kin(search):
    print("검색어: ", search)

    # 저장한 파일 열기 : 파일명
    # 년월일_시분초_검색어.csv
    # 20250508_101010_인공지능.csv
    # 엑셀파일의 경우 encoding은 "cp949"로 저장해야 한글이 깨지지 않음
    save_file = gen_filename(search)
    print("저장할 파일명: ", save_file)
    f = open(save_file, 'w', encoding='cp949', newline='')
    csvWriter = csv.writer(f)
    csvWriter.writerow(["text", "link"])

    for i in range(2):
        # 검색을 위한 qutue_plus 인코딩 작업
        url = f"https://kin.naver.com/search/list.naver?query={quote_plus(search)}&page={i+1}"
        print("url: ", url)

        # 네이버 지식인 정보 가져오기
        html = urlopen(url).read()
        # print("html: ", html)

        # BeautifulSoup 으로 html 파싱
        soup = bs(html, "html.parser")
        total = soup.select('.basic1 > li > dl > dt > a')
        print("total = ", len(total))

        for idx, data in enumerate(total):
            print("#" * 20 + str(idx + 1) + "#" * 20)
            print(data)
            # 제목만 검출
            title = data.text
            print("title: ", title)
            # 링크만 검출
            link = data.attrs['href']
            print("link: ", link)
            # csv 파일에 저장
            csvWriter.writerow([title, link])

        # 딜레이
        delay_time = random.randint(1, 10)
        time.sleep(delay_time)

    f.close()

    return save_file