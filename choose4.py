#선택지 화면 - 질문 n개 질문 안에 선택지 n개를 보여주는 페이지
import sys
import main
import choose5
from resultType import Type

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ChooseWindow(QWidget):
    result4 = []

    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #efebf3')
        self.setWindowTitle('CHOOSE')
        self.setWindowIcon(QIcon('image/icon.png'))
        self.setFixedSize(1000, 600)
        self.center()

        # creating questions widget
        self.label = QLabel('', self)
        self.label.setPixmap(QPixmap('image/choice/question/image.png'))
        self.label.resize(600, 100)
        self.label.move(210, 45)
        self.label.setAlignment(Qt.AlignCenter)

        # creating a button widget
        self.meekBtn = QLabel('', self)
        self.meekBtn.setPixmap(QPixmap('image/choice/answer/순함.png'))
        self.meekBtn.resize(150, 100)
        self.meekBtn.move(270, 380)
        self.meekBtn.setAlignment(Qt.AlignCenter)
        self.meekBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.meekBtn).connect(self.click_show10)

        self.strongBtn = QLabel('', self)
        self.strongBtn.setPixmap(QPixmap('image/choice/answer/강렬한.png'))
        self.strongBtn.resize(150, 100)
        self.strongBtn.move(600, 380)
        self.strongBtn.setAlignment(Qt.AlignCenter)
        self.strongBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.strongBtn).connect(self.click_show11)

        self.product2 = QLabel('', self)
        self.product2.setPixmap(QPixmap('image/line.png'))
        self.product2.resize(800, 15)
        # self.product2.move(140, 45)
        self.product2.setAlignment(Qt.AlignCenter)
        self.product2.setScaledContents(1)  # 이미지 크기에 맞게 조정

    def click_show10(self):
        self.show_choose = choose5.ChooseWindow()
        self.show_choose.show()
        Type.append(1)
        self.hide()

    def click_show11(self):
        self.show_choose = choose5.ChooseWindow()
        self.show_choose.show()
        Type.append(2)
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