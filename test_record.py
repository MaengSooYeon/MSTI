# 결과로 나온 타입의 이름과 빈도수를 볼 수 있는 화면

import re
# import string
import sys
import main

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# result.txt 파일에 있는 결과 빈도 수 구하는 코드
frequency = {}
document_text = open('file/result.txt', 'r', encoding='utf-8')
text_string = document_text.read()
match_pattern = re.findall(r'\b[가-힣]+\b', text_string)          #한글
# match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)    #영어

#뭐지 result.txt에서 값을 못가져온다..

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

f = open("file/result_cnt.txt", 'w+', encoding='utf-8')
for words in frequency_list:
    data = f'{words} 타입은 {frequency[words]}번의 결과가 나왔습니다.\n\n'
    f.write(data)
    # print(words,'type', frequency[words])
f.close()

class showRecordWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # window setting
        self.setStyleSheet('background-color: #efebf3')
        self.setWindowTitle('MSTI')
        self.setWindowIcon(QIcon('image/icon.png'))
        self.setFixedSize(1000, 600)
        self.center()

        # result count txt file
        with open('file/result_cnt.txt', 'r', encoding='utf8') as file:
            content = file.read()
            self.content = QLabel(content, self)
            self.content.resize(710, 500)
            self.content.move(150, 50)
            self.content.setAlignment(Qt.AlignCenter)
            self.content.setScaledContents(1)
            self.content.setStyleSheet('font: normal 19px 리디바탕')

            if not content:     #파일에 읽어올 txt가 없으면
                self.notTXT = QLabel('아직 테스트 기록이 없습니다.', self)
                self.notTXT.resize(710, 500)
                self.notTXT.move(150, 50)
                self.notTXT.setAlignment(Qt.AlignCenter)
                self.notTXT.setScaledContents(1)
                self.notTXT.setStyleSheet('font: normal 19px 리디바탕')

            print(content.strip('\n'))
            file.close()


        # creating widget - button
        self.gotoMainbtn = QLabel('', self)
        self.gotoMainbtn.setPixmap(QPixmap('image/gotoMainBtn.png'))
        self.gotoMainbtn.resize(180, 50)
        self.gotoMainbtn.move(420, 520)
        self.gotoMainbtn.setAlignment(Qt.AlignCenter)
        self.gotoMainbtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.gotoMainbtn).connect(self.showMain)


    # button event function
    def showMain(self):
        from resultType import Type
        self.show_main = main.MainWindow()
        self.show_main.show()
        Type.result.clear()
        self.hide()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_record = showRecordWindow()
    show_record.show()
    sys.exit(app.exec_())