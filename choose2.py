#선택지 화면 - 질문 n개 질문 안에 선택지 n개를 보여주는 페이지
import sys
import main
import choose3
from resultType import Type

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ChooseWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.choose2UI()

    def choose2UI(self):
        self.setStyleSheet('background-color: #efebf3')
        self.setWindowTitle('CHOOSE')
        self.setWindowIcon(QIcon('image/icon.png'))
        self.setFixedSize(1000, 600)
        self.center()

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
        main.clickable(self.tenBtn).connect(self.click_show1)

        self.twentyBtn = QLabel('', self)
        self.twentyBtn.setPixmap(QPixmap('image/choice/answer/20대.png'))
        self.twentyBtn.resize(150, 100)
        self.twentyBtn.move(420, 380)
        self.twentyBtn.setAlignment(Qt.AlignCenter)
        self.twentyBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.twentyBtn).connect(self.click_show2)

        self.thrityBtn = QLabel('', self)
        self.thrityBtn.setPixmap(QPixmap('image/choice/answer/30대.png'))
        self.thrityBtn.resize(150, 100)
        self.thrityBtn.move(700, 380)
        self.thrityBtn.setAlignment(Qt.AlignCenter)
        self.thrityBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.thrityBtn).connect(self.click_show3)

        self.product2 = QLabel('', self)
        self.product2.setPixmap(QPixmap('image/line.png'))
        self.product2.resize(400, 15)
        # self.product2.move(140, 45)
        self.product2.setAlignment(Qt.AlignCenter)
        self.product2.setScaledContents(1)  # 이미지 크기에 맞게 조정

    def click_show1(self):
        self.show_choose = choose3.ChooseWindow()
        self.show_choose.show()
        Type.append(1)
        self.hide()

    def click_show2(self):
        self.show_choose = choose3.ChooseWindow()
        self.show_choose.show()
        Type.append(2)
        self.hide()

    def click_show3(self):
        self.show_choose = choose3.ChooseWindow()
        self.show_choose.show()
        Type.append(3)
        self.hide()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chooseWindow = ChooseWindow()
    chooseWindow.show()
    sys.exit(app.exec_())