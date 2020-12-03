#선택지 화면 - 질문 n개 질문 안에 선택지 n개를 보여주는 페이지
import sys
import main

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ChooseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.choose1UI()
        self.result =[]

    def choose1UI(self):
        self.setStyleSheet('background-color: #efebf3')
        self.setWindowTitle('CHOOSE')
        self.setWindowIcon(QIcon('image/icon.png'))
        self.setFixedSize(1000, 600)

        # creating questions widget
        self.label = QLabel('', self)
        self.label.setPixmap(QPixmap('image/choice/question/season.png'))
        self.label.resize(750, 100)
        self.label.move(140, 45)
        self.label.setAlignment(Qt.AlignCenter)

        # creating a button widget
        self.springBtn = QLabel('', self)
        self.springBtn.setPixmap(QPixmap('image/choice/answer/봄.png'))
        self.springBtn.resize(150, 100)
        self.springBtn.move(100, 380)
        self.springBtn.setAlignment(Qt.AlignCenter)
        self.springBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.springBtn).connect(self.Click1)


        self.summerBtn = QLabel('', self)
        self.summerBtn.setPixmap(QPixmap('image/choice/answer/여름.png'))
        self.summerBtn.resize(150, 100)
        self.summerBtn.move(300, 380)
        self.summerBtn.setAlignment(Qt.AlignCenter)
        self.summerBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.summerBtn).connect(self.Click2)

        self.falltBtn = QLabel('', self)
        self.falltBtn.setPixmap(QPixmap('image/choice/answer/가을.png'))
        self.falltBtn.resize(150, 100)
        self.falltBtn.move(500, 380)
        self.falltBtn.setAlignment(Qt.AlignCenter)
        self.falltBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.falltBtn).connect(self.Click4)

        self.wintertBtn = QLabel('', self)
        self.wintertBtn.setPixmap(QPixmap('image/choice/answer/겨울.png'))
        self.wintertBtn.resize(150, 100)
        self.wintertBtn.move(700, 380)
        self.wintertBtn.setAlignment(Qt.AlignCenter)
        self.wintertBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.wintertBtn).connect(self.Click4)

        self.product2 = QLabel('', self)
        self.product2.setPixmap(QPixmap('image/line.png'))
        self.product2.resize(200, 15)
        self.label.move(140, 45)
        self.product2.setAlignment(Qt.AlignCenter)
        self.product2.setScaledContents(1)  # 이미지 크기에 맞게 조정



    def Click1(self):
        self.result.append(1)
        main.clickable(self.springBtn).connect(self.showChoose2)

    def Click2(self):
        self.result.append(2)
        main.clickable(self.summerBtn).connect(self.showChoose2)
    def Click3(self):
        self.result.append(3)
        main.clickable(self.falltBtn).connect(self.showChoose2)
    def Click4(self):
        self.result.append(4)
        main.clickable(self.wintertBtn).connect(self.showChoose2)

    def showChoose2(self):
        from choose2 import ChooseWindow
        self.show_choose2 = ChooseWindow()
        self.show_choose2.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    choose = ChooseWindow()
    choose.show()
    sys.exit(app.exec_())