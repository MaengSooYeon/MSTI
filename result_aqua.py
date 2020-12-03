#결과 화면 - 테스트 결과로 나온 나의 타입을 보여주는 화면
#        - 나의 타입 설명과 같이 향수 추천 
#        - 버튼1을 눌러 추천 향수 더 보러가기
#        - 버튼2을 눌러 전체(다른)타입 결과보기

import sys
import main

from moreResult import moreResultWindow
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ResultWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # window setting
        self.setStyleSheet('background-color: #B6F1FF')
        self.setWindowTitle('MSTI')
        self.setWindowIcon(QIcon('image/icon.png'))
        self.setFixedSize(1000, 600)
        self.center()

        # creating widget - type name, content
        self.typeImg = QLabel('', self)
        self.typeImg.setPixmap(QPixmap('image/type/icon/aqua.png'))
        self.typeImg.resize(240, 220)
        self.typeImg.move(95, 60)
        self.typeImg.setAlignment(Qt.AlignCenter)
        self.typeImg.setScaledContents(1)  # 이미지 크기에 맞게 조정

        self.typeName = QLabel('', self)
        self.typeName.setPixmap(QPixmap('image/type/type_aqua.png'))
        self.typeName.resize(250, 50)
        self.typeName.move(100, 280)
        self.typeName.setAlignment(Qt.AlignCenter)
        self.typeName.setScaledContents(1)  # 이미지 크기에 맞게 조정

        self.typeHT = QLabel('', self)
        self.typeHT.setPixmap(QPixmap('image/type/hashtag/HT_aqua.png'))
        self.typeHT.resize(220, 30)
        self.typeHT.move(115, 355)
        self.typeHT.setAlignment(Qt.AlignCenter)
        self.typeHT.setScaledContents(1)  # 이미지 크기에 맞게 조정


        # perfume type content txt file
        with open('file/contents/contents_aqua.txt', 'r', encoding='utf8') as file:
            content = file.read()
            self.content = QLabel(content, self)
            self.content.resize(710, 130)
            self.content.move(340, 100)
            self.content.setAlignment(Qt.AlignCenter)
            self.content.setScaledContents(1)
            self.content.setFont(QFont("한컴산뜻돋움", 13))
            print(content)
            file.close()


        # perfume recommendation
        self.product1 = QLabel('', self)
        self.product1.setPixmap(QPixmap('image/products/aqua/img1.png'))
        self.product1.resize(220, 220)
        self.product1.move(480, 270)
        self.product1.setAlignment(Qt.AlignCenter)
        self.product1.setScaledContents(1)  # 이미지 크기에 맞게 조정

        self.product2 = QLabel('', self)
        self.product2.setPixmap(QPixmap('image/products/aqua/img2.png'))
        self.product2.resize(220, 220)
        self.product2.move(700, 270)
        self.product2.setAlignment(Qt.AlignCenter)
        self.product2.setScaledContents(1)  # 이미지 크기에 맞게 조정


        # creating widget - button
        self.more_result_btn = QLabel('', self)
        self.more_result_btn.setPixmap(QPixmap('image/more_result_btn.png'))
        self.more_result_btn.resize(180, 50)
        self.more_result_btn.move(50, 520)
        self.more_result_btn.setAlignment(Qt.AlignCenter)
        self.more_result_btn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.more_result_btn).connect(self.moreResult)

        self.more_recommend_btn = QLabel('', self)
        self.more_recommend_btn.setPixmap(QPixmap('image/more_recommend_btn.png'))
        self.more_recommend_btn.resize(180, 50)
        self.more_recommend_btn.move(770, 520)
        self.more_recommend_btn.setAlignment(Qt.AlignCenter)
        self.more_recommend_btn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.more_recommend_btn).connect(self.moreProduct)


    # button event function
    def moreProduct(self):
        from product_aqua import ProductWindow
        self.more_product = ProductWindow()
        self.more_product.show()
        self.hide()

    def moreResult(self):
        self.more_result = moreResultWindow()
        self.more_result.show()
        self.hide()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    resultWindow = ResultWindow()
    resultWindow.show()
    sys.exit(app.exec_())