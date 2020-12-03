# woody type 향수 제품 설명화면

import sys
import main
import product_floral as p

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from moreResult import moreResultWindow

class ProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # window setting
        self.setStyleSheet('background-color: #ffffff')
        self.setWindowTitle('MSTI')
        self.setWindowIcon(QIcon('image/icon.png'))
        self.setFixedSize(1000, 600)
        self.move(10, 60)

        # creating widget - product img, content
        self.product1 = QLabel('', self)
        self.product1.setPixmap(QPixmap('image/products/woody/img3.png'))
        self.product1.resize(480, 225)
        self.product1.move(15, 100)
        self.product1.setAlignment(Qt.AlignCenter)
        self.product1.setScaledContents(1)  # 이미지 크기에 맞게 조정

        self.product2 = QLabel('', self)
        self.product2.setPixmap(QPixmap('image/products/woody/img4.png'))
        self.product2.resize(480, 225)
        self.product2.move(12, 320)
        self.product2.setAlignment(Qt.AlignCenter)
        self.product2.setScaledContents(1)  # 이미지 크기에 맞게 조정

        self.product3 = QLabel('', self)
        self.product3.setPixmap(QPixmap('image/products/woody/img5.png'))
        self.product3.resize(480, 225)
        self.product3.move(495, 100)
        self.product3.setAlignment(Qt.AlignCenter)
        self.product3.setScaledContents(1)  # 이미지 크기에 맞게 조정

        self.product4 = QLabel('', self)
        self.product4.setPixmap(QPixmap('image/products/woody/img6.png'))
        self.product4.resize(480, 225)
        self.product4.move(490, 320)
        self.product4.setAlignment(Qt.AlignCenter)
        self.product4.setScaledContents(1)  # 이미지 크기에 맞게 조정


        # creating widget - button
        self.more_result_btn = QLabel('', self)
        self.more_result_btn.setPixmap(QPixmap('image/more_result_btn.png'))
        self.more_result_btn.resize(180, 50)
        self.more_result_btn.move(30, 25)
        self.more_result_btn.setAlignment(Qt.AlignCenter)
        self.more_result_btn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.more_result_btn).connect(self.moreResult)

        self.gotoMainbtn = QLabel('', self)
        self.gotoMainbtn.setPixmap(QPixmap('image/gotoMainBtn.png'))
        self.gotoMainbtn.resize(180, 50)
        self.gotoMainbtn.move(800, 25)
        self.gotoMainbtn.setAlignment(Qt.AlignCenter)
        self.gotoMainbtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.gotoMainbtn).connect(self.showMain)

        self.contents = QLabel('', self)
        self.contents.setPixmap(QPixmap('image/products/icon.png'))
        self.contents.resize(50, 50)
        self.contents.move(700, 25)
        self.contents.setAlignment(Qt.AlignCenter)
        self.contents.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.contents).connect(self.showContents)


    # button event function
    def showMain(self):
        self.show_main = main.MainWindow()
        self.show_main.show()
        self.hide()

    def moreResult(self):
        self.more_result = moreResultWindow()
        self.more_result.show()
        self.hide()

    def showContents(self):
        self.show_contents = p.ContentsWindow()
        self.show_contents.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    productWindow = ProductWindow()
    productWindow.show()
    sys.exit(app.exec_())