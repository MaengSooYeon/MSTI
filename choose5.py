#선택지 화면 - 질문 n개 질문 안에 선택지 n개를 보여주는 페이지
import sys
import main

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ChooseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.choose5UI()

    def choose5UI(self):
        self.setStyleSheet('background-color: #efebf3')
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

        self.product2 = QLabel('', self)
        self.product2.setPixmap(QPixmap('image/line.png'))
        self.product2.resize(1000, 15)
        # self.product2.move(140, 45)
        self.product2.setAlignment(Qt.AlignCenter)
        self.product2.setScaledContents(1)  # 이미지 크기에 맞게 조정

    def Click1(self):
        self.show_choose = ChooseWindow()
        self.show_choose.show()
        self.result.append(1)
        self.hide()

    def Click2(self):
        self.show_choose = ChooseWindow()
        self.show_choose.show()
        self.result.append(2)
        self.hide()

        if i == [1,1,1,2,1] or [1,2,1,2,1] or [1,3,1,2,1] or [1,1,1,1,2] or [1,2,1,1,2] or [1,3,1,1,2] or [1,1,2,2,2] or [1,2,2,2,2] or [1,3,2,2,2] or [1,1,2,1,2] or [1,2,2,1,2] or [1,3,2,1,2] :
             main.clickable(self.calmtBtn).connect(self.showFloral)
             main.clickable(self.livelyBtn).connect(self.showFloral)
        elif i == [1,1,1,1,1] or [2,1,1,1,1] or [3,1,1,1,1] or [1,1,1,1,2] or [2,1,1,1,2] or [3,1,1,1,2] or [1,1,2,1,2] or [2,1,2,1,2] or [3,1,2,1,2] or [1,1,2,2,2] or [2,1,2,2,2] or [3,1,2,2,2]:
            main.clickable(self.calmtBtn).connect(self.showGreen)
            main.clickable(self.livelyBtn).connect(self.showGreen)
        elif i == [2,1,1,1,1] or [2,2,1,1,1] or [2,3,1,1,1] or [2,1,1,2,1] or [2,2,1,2,1] or [2,3,1,2,1] or [2,1,1,2,2] or [2,2,1,2,2] or [2,3,1,2,2] or [2,1,2,2,1] or [2,2,2,2,1] or [2,3,2,2,1] :
            main.clickable(self.calmtBtn).connect(self.showAqua)
            main.clickable(self.livelyBtn).connect(self.showAqua)
        elif i == [2,1,2,1,1] or [2,2,2,1,1] or [2,3,2,1,1] or [2,1,1,1,2] or [2,2,1,1,2] or [2,3,1,1,2] or [2,1,2,1,2] or [2,2,2,1,2] or [2,3,2,1,2] or [2,1,2,2,2] or [2,2,2,2,2] or [2,3,2,2,2] :
            main.clickable(self.calmtBtn).connect(self.showFruity)
            main.clickable(self.livelyBtn).connect(self.showFruity)
        elif i == [3,1,1,1,1] or [3,2,1,1,1] or [3,3,1,1,1] or [3,1,1,2,1] or [3,2,1,2,1] or [3,3,1,2,1] or [3,1,2,1,2] or [3,2,2,1,2] or [3,3,2,1,2] or [3,1,2,2,2] or [3,2,2,2,2] or [3,3,2,2,2] :
            main.clickable(self.calmtBtn).connect(self.showWoody)
            main.clickable(self.livelyBtn).connect(self.showWoody)
        elif i == [3,1,2,1,1] or [3,2,2,1,1] or [3,3,2,1,1] or [3,1,2,2,1] or [3,2,2,2,1] or [3,3,2,2,1] or [3,1,1,1,2] or [3,2,1,1,2] or [3,3,1,1,2] or [3,1,1,2,2] or [3,2,1,2,2] or [3,3,1,2,2] :
            main.clickable(self.calmtBtn).connect(self.showMusk)
            main.clickable(self.livelyBtn).connect(self.showMusk)
        elif i == [4,1,2,2,1] or [4,2,2,2,1] or [4,3,2,2,1] or [4,1,2,2,2] or [4,2,2,2,2] or [4,3,2,2,2] or [4,1,1,2,2] or [4,2,1,2,2] or [4,3,1,2,2] or [4,1,1,2,1] or [4,2,1,2,1] or [4,3,1,2,1] :
            main.clickable(self.calmtBtn).connect(self.showGourmans)
            main.clickable(self.livelyBtn).connect(self.showGourmans)
        elif i == [4,1,1,1,1] or [4,2,1,1,1] or [4,3,1,1,1] or [4,1,2,1,1] or [4,2,2,1,1] or [4,3,2,1,1] or [4,1,1,1,2] or [4,2,1,1,2] or [4,3,1,1,2] or [4,1,2,1,2] or [4,2,2,1,2] or [4,3,2,1,2] :
            main.clickable(self.calmtBtn).connect(self.showTobacco)
            main.clickable(self.livelyBtn).connect(self.showTobacco)

    def showFloral(self):
        from result_floral import ResultWindow
        self.show_floral = ResultWindow()
        self.show_floral.show()
        self.hide()
    def showGreen(self):
        from result_green import ResultWindow
        self.show_green = ResultWindow()
        self.show_green.show()
        self.hide()
    def showAqua(self):
        from result_aqua import ResultWindow
        self.show_aqua = ResultWindow()
        self.show_aqua.show()
        self.hide()
    def showFruity(self):
        from result_fruity import ResultWindow
        self.show_fruity = ResultWindow()
        self.show_fruity.show()
        self.hide()
    def showWoody(self):
        from result_woody import ResultWindow
        self.show_woody = ResultWindow()
        self.show_woody.show()
        self.hide()
    def showMusk(self):
        from result_musk import ResultWindow
        self.show_musk = ResultWindow()
        self.show_musk.show()
        self.hide()
    def showGourmans(self):
        from result_gourmans import ResultWindow
        self.show_gourmans = ResultWindow()
        self.show_gourmans.show()
        self.hide()
    def showTobacco(self):
        from result_tobacco_leather import ResultWindow
        self.show_tobacco = ResultWindow()
        self.show_tobacco.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chooseWindow = ChooseWindow()
    chooseWindow.show()
    sys.exit(app.exec_())