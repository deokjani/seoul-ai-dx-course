import sys
import os.path

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

from lib.navercrawl_lib import search_naver_kin
from lib.wordcloud_lib import WordCloud_Create

form_class = uic.loadUiType("./ui/wordcloud_main.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(1600, 1200)
        self.btn_close.clicked.connect(self.close_clicked)
        self.btn_search.clicked.connect(self.search_clicked)
        self.btn_process.clicked.connect(self.process_clicked)

    def process_clicked(self):
        searchFile = self.ed_file.text()

        # ed_file 이 비어 있을 경우      
        if searchFile == "":
            QMessageBox.warning(self, "경고", "파일명을 입력해주세요.")
            return
        
        # ed_file 의 파일이 존재하는지 확인
        if os.path.exists(searchFile) == False:
            QMessageBox.warning(self, "경고", "파일이 존재하지 않습니다.")
            return
        
        # ed_file 의 확장자 확인
        extFile = os.path.splitext(searchFile)[1]
        if extFile != ".csv":
            QMessageBox.warning(self, "경고", "CSV 파일만 가능합니다.")
            return
        
        # 금지어
        stopWord = self.ed_stopword.text()
        
        # wordcloud 생성
        cloud_path = WordCloud_Create(searchFile, stopWord)
        # 이미지 표시하기
        self.qPixmapfileVar = QPixmap()
        self.qPixmapfileVar.load(cloud_path)
        self.qPixmapfileVar = self.qPixmapfileVar.scaled(1024, 768)
        self.lb_word.setPixmap(self.qPixmapfileVar)
        
    def search_clicked(self):
        search = self.ed_search.text()
        if search == "":
            QMessageBox.warning(self, "경고", "검색어를 입력하세요.")
            return
        
        save_file = search_naver_kin(search)
        self.ed_result.setText(save_file)
        self.ed_file.setText(save_file)
        self.ed_stopword.setText(search)

    def close_clicked(self):
        btnResult = QMessageBox.question(self, "종료", "정말 종료하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if btnResult == QMessageBox.Yes:
            self.close()
        else:
            pass

app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()
