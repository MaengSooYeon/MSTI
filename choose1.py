#선택지 화면 - 질문 n개 질문 안에 선택지 n개를 보여주는 페이지
import sys
import main
import choose2
from resultType import Type

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ChooseWindow(QMainWindow):


    def __init__(self):
        super().__init__()
        self.choose1UI()


    def choose1UI(self):
        self.setStyleSheet('background-color: #efebf3')
        self.setWindowTitle('CHOOSE1')
        self.setWindowIcon(QIcon('image/icon.png'))
        self.setFixedSize(1000, 600)
        self.center()

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
        main.clickable(self.springBtn).connect(self.click_show1)

        self.summerBtn = QLabel('', self)
        self.summerBtn.setPixmap(QPixmap('image/choice/answer/여름.png'))
        self.summerBtn.resize(150, 100)
        self.summerBtn.move(300, 380)
        self.summerBtn.setAlignment(Qt.AlignCenter)
        self.summerBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.summerBtn).connect(self.click_show2)

        self.falltBtn = QLabel('', self)
        self.falltBtn.setPixmap(QPixmap('image/choice/answer/가을.png'))
        self.falltBtn.resize(150, 100)
        self.falltBtn.move(500, 380)
        self.falltBtn.setAlignment(Qt.AlignCenter)
        self.falltBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.falltBtn).connect(self.click_show3)

        self.wintertBtn = QLabel('', self)
        self.wintertBtn.setPixmap(QPixmap('image/choice/answer/겨울.png'))
        self.wintertBtn.resize(150, 100)
        self.wintertBtn.move(700, 380)
        self.wintertBtn.setAlignment(Qt.AlignCenter)
        self.wintertBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.wintertBtn).connect(self.click_show4)

        self.product2 = QLabel('', self)
        self.product2.setPixmap(QPixmap('image/line.png'))
        self.product2.resize(200, 15)
        # self.product2.move(140, 45)
        self.product2.setAlignment(Qt.AlignCenter)
        self.product2.setScaledContents(1)  # 이미지 크기에 맞게 조정

    def click_show1(self):
        self.show_choose = choose2.ChooseWindow()
        self.show_choose.show()
        Type.append(1)
        self.hide()

    def click_show2(self):
        self.show_choose = choose2.ChooseWindow()
        self.show_choose.show()
        Type.append(2)
        self.hide()

    def click_show3(self):
        self.show_choose = choose2.ChooseWindow()
        self.show_choose.show()
        Type.append(3)
        self.hide()

    def click_show4(self):
        self.show_choose = choose2.ChooseWindow()
        self.show_choose.show()
        Type.append(4)
        self.hide()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    choose = ChooseWindow()
    choose.show()
    sys.exit(app.exec_())