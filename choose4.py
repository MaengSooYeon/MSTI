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
        self.setWindowIcon(QIcon('image/horse.jpg'))
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
        main.clickable(self.springBtn).connect(self.showChoose5)

        self.summerBtn = QLabel('', self)
        self.summerBtn.setPixmap(QPixmap('image/choice/answer/여름.png'))
        self.summerBtn.resize(150, 100)
        self.summerBtn.move(300, 380)
        self.summerBtn.setAlignment(Qt.AlignCenter)
        self.summerBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.summerBtn).connect(self.showChoose5)

        self.falltBtn = QLabel('', self)
        self.falltBtn.setPixmap(QPixmap('image/choice/answer/가을.png'))
        self.falltBtn.resize(150, 100)
        self.falltBtn.move(500, 380)
        self.falltBtn.setAlignment(Qt.AlignCenter)
        self.falltBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.falltBtn).connect(self.showChoose5)

        self.wintertBtn = QLabel('', self)
        self.wintertBtn.setPixmap(QPixmap('image/choice/answer/겨울.png'))
        self.wintertBtn.resize(150, 100)
        self.wintertBtn.move(700, 380)
        self.wintertBtn.setAlignment(Qt.AlignCenter)
        self.wintertBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.wintertBtn).connect(self.showChoose5)

    def showChoose5(self):
        from choose5 import ChooseWindow
        self.show_choose5 = ChooseWindow()
        self.show_choose5.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chooseWindow = ChooseWindow()
    chooseWindow.show()
    sys.exit(app.exec_())