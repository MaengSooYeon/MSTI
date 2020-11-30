# 다른 결과 보기 버튼을 눌렀을 시 보여주는 페이지
# 돌아가기 버튼, 가로 또는 세로 스크롤 바
# 타입 이름을 누르면 해당 타입 결과 페이지로 이동
import sys
import main
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class moreResultWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # window setting
        self.setStyleSheet('background-color: #2C0F59')
        self.setWindowTitle('MSTI')
        #https://wikidocs.net/21853 아이콘넣기
        self.setWindowIcon(QIcon('image/horse.jpg'))
        self.setFixedSize(1000, 600)
        self.center()

        # scroll = QScrollArea()
        # self.addWidget(scroll)

        # creating a label widget
        self.title = QLabel('', self)
        self.title.setPixmap(QPixmap('image/msti_types.png'))
        self.title.resize(320, 70)
        self.title.move(50, 20)
        self.title.setScaledContents(1)  # 이미지 크기에 맞게 조정
        self.title.setAlignment(Qt.AlignCenter)

        self.floral = QLabel('', self)
        self.floral.setPixmap(QPixmap('image/type/more_result/more_result_floral.png'))
        self.floral.resize(400, 140)
        self.floral.move(30, 110)
        self.floral.setAlignment(Qt.AlignCenter)
        self.floral.setScaledContents(1)  # 이미지 크기에 맞게 조정
        # main.clickable(self.floral).connect(self.moreProduct)

        self.musk = QLabel('', self)
        self.musk.setPixmap(QPixmap('image/type/more_result/more_result_musk.png'))
        self.musk.resize(400, 140)
        self.musk.move(440, 110)
        self.musk.setAlignment(Qt.AlignCenter)
        self.musk.setScaledContents(1)  # 이미지 크기에 맞게 조정
        # main.clickable(self.musk).connect(self.moreProduct)

        self.woody = QLabel('', self)
        self.woody.setPixmap(QPixmap('image/type/more_result/more_result_woody.png'))
        self.woody.resize(400, 140)
        self.woody.move(30, 270)
        self.woody.setAlignment(Qt.AlignCenter)
        self.woody.setScaledContents(1)  # 이미지 크기에 맞게 조정
        # main.clickable(self.woody).connect(self.moreProduct)

        self.fruity = QLabel('', self)
        self.fruity.setPixmap(QPixmap('image/type/more_result/more_result_fruity.png'))
        self.fruity.resize(400, 140)
        self.fruity.move(440, 270)
        self.fruity.setAlignment(Qt.AlignCenter)
        self.fruity.setScaledContents(1)  # 이미지 크기에 맞게 조정
        # main.clickable(self.fruity).connect(self.moreProduct)


        self.green = QLabel('', self)
        self.green.setPixmap(QPixmap('image/type/more_result/more_result_green.png'))
        self.green.resize(400, 140)
        self.green.move(30, 430)
        self.green.setAlignment(Qt.AlignCenter)
        self.green.setScaledContents(1)  # 이미지 크기에 맞게 조정
        # main.clickable(self.green).connect(self.moreProduct)

        self.aqua = QLabel('', self)
        self.aqua.setPixmap(QPixmap('image/type/more_result/more_result_aqua.png'))
        self.aqua.resize(400, 140)
        self.aqua.move(440, 430)
        self.aqua.setAlignment(Qt.AlignCenter)
        self.aqua.setScaledContents(1)  # 이미지 크기에 맞게 조정
        # main.clickable(self.aqua).connect(self.moreProduct)

        #나머지 6개 추가하기


        # creating a button widget
        self.gotoMainbtn = QLabel('', self)
        self.gotoMainbtn.setPixmap(QPixmap('image/gotoMainBtn.png'))
        self.gotoMainbtn.resize(180, 50)
        self.gotoMainbtn.move(800, 25)
        self.gotoMainbtn.setAlignment(Qt.AlignCenter)
        self.gotoMainbtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.gotoMainbtn).connect(self.moreProduct)

    # button event function
    def moreProduct(self):
        QMessageBox.about(self, "message", "clicked")
        # 관련된 향수 정보 창으로 바꾸기

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
if __name__ == '__main__':
    app = QApplication(sys.argv)
    more_result_window = moreResultWindow()
    more_result_window.show()
    sys.exit(app.exec_())