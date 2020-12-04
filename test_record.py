import re
# import string
import sys
import main

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class showRecordWindow(QMainWindow):
    def __init__(self):
        self.showTxt()
        super().__init__()
        # window setting
        self.setStyleSheet('background-color: #efebf3')
        self.setWindowTitle('MSTI')
        self.setWindowIcon(QIcon('image/icon.png'))
        self.setFixedSize(1000, 600)
        self.center()

        f2 = open("file/result_cnt.txt",'r', encoding='utf-8')
        text2 = f2.read

        self.content = QLabel('', self)
        self.content.setText(self.showTxt())
        self.content.resize(710, 500)
        self.content.move(150, 50)
        self.content.setAlignment(Qt.AlignCenter)
        self.content.setScaledContents(1)
        self.content.setStyleSheet('font: normal 19px 리디바탕')


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

    def showTxt(self):
        f1 = open('file/result.txt', 'r', encoding='utf-8')
        text = f1.read()
        t = text.split()

        f2 = open("file/result_cnt.txt",'a', encoding='utf-8')

        cnt = {}
        for i in t:
            cnt[i] = cnt.get(i, 0) + 1
            keys = sorted(cnt.keys())
        for i in keys:
            self.txt = (i + " 타입의 " + str(cnt[i]) + "번의 결과가 나왔습니다 \n")
            self.content.setText(self.txt)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_record = showRecordWindow()
    show_record.show()
    sys.exit(app.exec_())