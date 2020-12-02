import sys
import main
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ProductWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # window setting
        self.setStyleSheet('background-color: #ffffff')
        self.setWindowTitle('MSTI')
        # https://wikidocs.net/21853 아이콘넣기
        self.setWindowIcon(QIcon('image/horse.jpg'))
        self.setFixedSize(1000, 600)
        self.center()

        # creating a label widget
        self.product1 = QLabel('', self)
        self.product1.setPixmap(QPixmap('image/products/tobacco_leather/img3.png'))
        self.product1.resize(480, 225)
        self.product1.move(15, 100)
        self.product1.setAlignment(Qt.AlignCenter)
        self.product1.setScaledContents(1)  # 이미지 크기에 맞게 조정

        self.product2 = QLabel('', self)
        self.product2.setPixmap(QPixmap('image/products/tobacco_leather/img4.png'))
        self.product2.resize(480, 225)
        self.product2.move(8, 320)
        self.product2.setAlignment(Qt.AlignCenter)
        self.product2.setScaledContents(1)  # 이미지 크기에 맞게 조정

        self.product3 = QLabel('', self)
        self.product3.setPixmap(QPixmap('image/products/tobacco_leather/img5.png'))
        self.product3.resize(480, 225)
        self.product3.move(500, 100)
        self.product3.setAlignment(Qt.AlignCenter)
        self.product3.setScaledContents(1)  # 이미지 크기에 맞게 조정

        self.product4 = QLabel('', self)
        self.product4.setPixmap(QPixmap('image/products/tobacco_leather/img6.png'))
        self.product4.resize(480, 225)
        self.product4.move(495, 320)
        self.product4.setAlignment(Qt.AlignCenter)
        self.product4.setScaledContents(1)  # 이미지 크기에 맞게 조정

        # creating a button widget
        self.gotoMainbtn = QLabel('', self)
        self.gotoMainbtn.setPixmap(QPixmap('image/gotoMainBtn.png'))
        self.gotoMainbtn.resize(180, 50)
        self.gotoMainbtn.move(800, 25)
        self.gotoMainbtn.setAlignment(Qt.AlignCenter)
        self.gotoMainbtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.gotoMainbtn).connect(self.showMain)


    # button event function
    def showMain(self):
        self.show_main = main.MainWindow()
        self.show_main.show()
        self.hide()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    productWindow = ProductWindow()
    productWindow.show()
    sys.exit(app.exec_())