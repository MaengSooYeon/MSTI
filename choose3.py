#선택지 화면 - 질문 n개 질문 안에 선택지 n개를 보여주는 페이지
import sys

import main

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ChooseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #FFFFFF')
        self.setWindowTitle('CHOOSE')
        self.setWindowIcon(QIcon('image/icon.png'))
        self.setFixedSize(1000, 600)

        # creating questions widget
        self.label = QLabel('', self)
        self.label.setPixmap(QPixmap('image/choice/question/style.png'))
        self.label.resize(750, 100)
        self.label.move(140, 45)
        self.label.setAlignment(Qt.AlignCenter)

        # creating a button widget
        self.naturalBtn = QLabel('', self)
        self.naturalBtn.setPixmap(QPixmap('image/choice/answer/내추럴.png'))
        self.naturalBtn.resize(150, 100)
        self.naturalBtn.move(270, 380)
        self.naturalBtn.setAlignment(Qt.AlignCenter)
        self.naturalBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        self.btn1 = main.clickable(self.naturalBtn).connect(self.showChoose4)

        self.trendyBtn = QLabel('', self)
        self.trendyBtn.setPixmap(QPixmap('image/choice/answer/트렌디.png'))
        self.trendyBtn.resize(150, 100)
        self.trendyBtn.move(600, 380)
        self.trendyBtn.setAlignment(Qt.AlignCenter)
        self.trendyBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        self.btn2 = main.clickable(self.trendyBtn).connect(self.showChoose4)

    def check3(self):
        from choose1 import i

        if self.btn1:
            i.append(1)
            print(i)
        elif self.btn1:
            i.append(2)

    def showChoose4(self):
        from choose4 import ChooseWindow
        self.show_choose4 = ChooseWindow()
        self.show_choose4.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chooseWindow = ChooseWindow()
    chooseWindow.show()
    sys.exit(app.exec_())