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
        self.label.setPixmap(QPixmap('image/choice/question/feel.png'))
        self.label.resize(750, 100)
        self.label.move(160, 45)
        self.label.setAlignment(Qt.AlignCenter)

        # creating a button widget
        self.calmtBtn = QLabel('', self)
        self.calmtBtn.setPixmap(QPixmap('image/choice/answer/차분함.png'))
        self.calmtBtn.resize(150, 100)
        self.calmtBtn.move(270, 380)
        self.calmtBtn.setAlignment(Qt.AlignCenter)
        self.calmtBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정


        self.livelyBtn = QLabel('', self)
        self.livelyBtn.setPixmap(QPixmap('image/choice/answer/생동감.png'))
        self.livelyBtn.resize(150, 100)
        self.livelyBtn.move(600, 380)
        self.livelyBtn.setAlignment(Qt.AlignCenter)
        self.livelyBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정


    def check4(self):
        from choose4 import i
        if self.btn1:
            i.append(1)
        elif self.btn1:
            i.append(2)

        if i == [1,1,1,2,1] or [1,2,1,2,1] or [1,3,1,2,1] or [1,1,1,1,2] or [1,2,1,1,2] or [1,3,1,1,2] or [1,1,2,2,2] or [1,2,2,2,2] or [1,3,2,2,2] or [1,1,2,1,2] or [1,2,2,1,2] or [1,3,2,1,2] :
             main.clickable(self.calmtBtn).connect(self.showFloral)
             main.clickable(self.livelyBtn).connect(self.showFloral)
        elif i == [1,1,1,1,1] or [2,1,1,1,1] or [3,1,1,1,1] or [1,1,1,1,2] or [2,1,1,1,2] or [3,1,1,1,2] or [1,1,2,1,2] or [2,1,2,1,2] or [3,1,2,1,2] or [1,1,2,2,2] or [2,1,2,2,2] or [3,1,2,2,2]:
            main.clickable(self.calmtBtn).connect(self.showFloral)
            main.clickable(self.livelyBtn).connect(self.showFloral)
        elif i == [2,1,1,1,1] or [2,2,1,1,1] or [2,3,1,1,1] or [2,1,1,2,1] or [2,2,1,2,1] or [2,3,1,2,1] or [2,1,1,2,2] or [2,2,1,2,2] or [2,3,1,2,2] or [2,1,2,2,1] or [2,2,2,2,1] or [2,3,2,2,1] :
            main.clickable(self.calmtBtn).connect(self.showFloral)
            main.clickable(self.livelyBtn).connect(self.showFloral)
        elif i == [2,1,2,1,1] or [2,2,2,1,1] or [2,3,2,1,1] or [2,1,1,1,2] or [2,2,1,1,2] or [2,3,1,1,2] or [2,1,2,1,2] or [2,2,2,1,2] or [2,3,2,1,2] or [2,1,2,2,2] or [2,2,2,2,2] or [2,3,2,2,2] :
            main.clickable(self.calmtBtn).connect(self.showFloral)
            main.clickable(self.livelyBtn).connect(self.showFloral)
        elif i == [3,1,1,1,1] or [3,2,1,1,1] or [3,3,1,1,1] or [3,1,1,2,1] or [3,2,1,2,1] or [3,3,1,2,1] or [3,1,2,1,2] or [3,2,2,1,2] or [3,3,2,1,2] or [3,1,2,2,2] or [3,2,2,2,2] or [3,3,2,2,2] :
            main.clickable(self.calmtBtn).connect(self.showFloral)
            main.clickable(self.livelyBtn).connect(self.showFloral)
        elif i == [3,1,2,1,1] or [3,2,2,1,1] or [3,3,2,1,1] or [3,1,2,2,1] or [3,2,2,2,1] or [3,3,2,2,1] or [3,1,1,1,2] or [3,2,1,1,2] or [3,3,1,1,2] or [3,1,1,2,2] or [3,2,1,2,2] or [3,3,1,2,2] :
            main.clickable(self.calmtBtn).connect(self.showFloral)
            main.clickable(self.livelyBtn).connect(self.showFloral)
        elif i == [4,1,2,2,1] or [4,2,2,2,1] or [4,3,2,2,1] or [4,1,2,2,2] or [4,2,2,2,2] or [4,3,2,2,2] or [4,1,1,2,2] or [4,2,1,2,2] or [4,3,1,2,2] or [4,1,1,2,1] or [4,2,1,2,1] or [4,3,1,2,1] :
            main.clickable(self.calmtBtn).connect(self.showFloral)
            main.clickable(self.livelyBtn).connect(self.showFloral)
        elif i == [4,1,1,1,1] or [4,2,1,1,1] or [4,3,1,1,1] or [4,1,2,1,1] or [4,2,2,1,1] or [4,3,2,1,1] or [4,1,1,1,2] or [4,2,1,1,2] or [4,3,1,1,2] or [4,1,2,1,2] or [4,2,2,1,2] or [4,3,2,1,2] :
            main.clickable(self.calmtBtn).connect(self.showFloral)
            main.clickable(self.livelyBtn).connect(self.showFloral)


    def showFloral(self):
        from result_floral import ResultWindow
        self.show_floral = ResultWindow()
        self.show_floral.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chooseWindow = ChooseWindow()
    chooseWindow.show()
    sys.exit(app.exec_())