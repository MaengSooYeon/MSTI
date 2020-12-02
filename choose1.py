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
        self.label.setPixmap(QPixmap('image/choice/question/age.png'))
        self.label.resize(600, 100)
        self.label.move(210, 45)
        self.label.setAlignment(Qt.AlignCenter)

        # creating a button widget
        self.tenBtn = QLabel('', self)
        self.tenBtn.setPixmap(QPixmap('image/choice/answer/10대.png'))
        self.tenBtn.resize(150, 100)
        self.tenBtn.move(130, 380)
        self.tenBtn.setAlignment(Qt.AlignCenter)
        self.tenBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.tenBtn).connect(self.showChoose2)

        self.twentyBtn = QLabel('', self)
        self.twentyBtn.setPixmap(QPixmap('image/choice/answer/20대.png'))
        self.twentyBtn.resize(150, 100)
        self.twentyBtn.move(420, 380)
        self.twentyBtn.setAlignment(Qt.AlignCenter)
        self.twentyBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.twentyBtn).connect(self.showChoose2)

        self.thrityBtn = QLabel('', self)
        self.thrityBtn.setPixmap(QPixmap('image/choice/answer/30대.png'))
        self.thrityBtn.resize(150, 100)
        self.thrityBtn.move(700, 380)
        self.thrityBtn.setAlignment(Qt.AlignCenter)
        self.thrityBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.thrityBtn).connect(self.showChoose2)

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