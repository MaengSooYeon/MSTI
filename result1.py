#결과 화면 - 테스트 결과로 나온 나의 타입을 보여주는 화면
#        - 나의 타입 설명과 같이 향수 추천 
#        - 버튼1을 눌러 추천 향수 더 보러가기
#        - 버튼2을 눌러 전체(다른)타입 결과보기
import sys
import main
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class ResultWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # window setting
        self.setStyleSheet('background-color: #FFE3E3')
        self.setWindowTitle('MSTI')
        # https://wikidocs.net/21853 아이콘넣기
        self.setWindowIcon(QIcon('image/horse.jpg'))
        self.setFixedSize(1000, 600)
        self.center()

        # creating a label widget
        self.typeImg = QLabel('', self)
        self.typeImg.setPixmap(QPixmap('image/type/icon/floral.png'))
        self.typeImg.resize(220, 220)
        self.typeImg.move(110, 60)
        self.typeImg.setAlignment(Qt.AlignCenter)
        self.typeImg.setScaledContents(1)  # 이미지 크기에 맞게 조정

        self.typeName = QLabel('', self)
        self.typeName.setPixmap(QPixmap('image/type/type_floral.png'))
        self.typeName.resize(250, 50)
        self.typeName.move(100, 280)
        self.typeName.setAlignment(Qt.AlignCenter)
        self.typeName.setScaledContents(1)  # 이미지 크기에 맞게 조정

        self.typeHT = QLabel('', self)
        self.typeHT.setPixmap(QPixmap('image/type/hashtag/HT_floral.png'))
        self.typeHT.resize(220, 30)
        self.typeHT.move(115, 355)
        self.typeHT.setAlignment(Qt.AlignCenter)
        self.typeHT.setScaledContents(1)  # 이미지 크기에 맞게 조정

        self.typeHT = QLabel('', self)
        self.typeHT.setPixmap(QPixmap('image/type/contents/contents_floral.png'))
        self.typeHT.resize(590, 150)
        self.typeHT.move(410, 100)
        self.typeHT.setAlignment(Qt.AlignCenter)
        self.typeHT.setScaledContents(1)  # 이미지 크기에 맞게 조정


        # creating a button widget
        self.more_recommend_btn = QLabel('', self)
        self.more_recommend_btn.setPixmap(QPixmap('image/more_recommend_btn.png'))
        self.more_recommend_btn.resize(180, 50)
        self.more_recommend_btn.move(770, 520)
        self.more_recommend_btn.setAlignment(Qt.AlignCenter)
        self.more_recommend_btn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.more_recommend_btn).connect(self.moreProduct)

        self.more_result_btn = QLabel('', self)
        self.more_result_btn.setPixmap(QPixmap('image/more_result_btn.png'))
        self.more_result_btn.resize(180, 50)
        self.more_result_btn.move(50, 520)
        self.more_result_btn.setAlignment(Qt.AlignCenter)
        self.more_result_btn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.more_result_btn).connect(self.moreProduct)

    # button event function
    def moreProduct(self):
        QMessageBox.about(self, "message", "clicked")
        #관련된 향수 정보 창으로 바꾸기

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