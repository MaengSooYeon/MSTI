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

        # creating a label widget
        self.title = QLabel('', self)
        self.title.setPixmap(QPixmap('image/msti_types.png'))
        self.title.resize(280, 60)
        self.title.move(30, 20)
        self.title.setScaledContents(1)  # 이미지 크기에 맞게 조정
        self.title.setAlignment(Qt.AlignCenter)

        #1열
        self.floral = QLabel('', self)
        self.floral.setPixmap(QPixmap('image/type/more_result/more_result_floral.png'))
        self.floral.resize(310, 110)
        self.floral.move(20, 110)
        self.floral.setAlignment(Qt.AlignCenter)
        self.floral.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.floral).connect(self.showFloral)

        self.fruity = QLabel('', self)
        self.fruity.setPixmap(QPixmap('image/type/more_result/more_result_fruity.png'))
        self.fruity.resize(310, 110)
        self.fruity.move(345, 110)
        self.fruity.setAlignment(Qt.AlignCenter)
        self.fruity.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.fruity).connect(self.showFruity)

        self.musk = QLabel('', self)
        self.musk.setPixmap(QPixmap('image/type/more_result/more_result_musk.png'))
        self.musk.resize(310, 110)
        self.musk.move(670, 110)
        self.musk.setAlignment(Qt.AlignCenter)
        self.musk.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.musk).connect(self.showMusk)


        #2열
        self.minty = QLabel('', self)
        self.minty.setPixmap(QPixmap('image/type/more_result/more_result_minty.png'))
        self.minty.resize(310, 110)
        self.minty.move(20, 228)
        self.minty.setAlignment(Qt.AlignCenter)
        self.minty.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.minty).connect(self.showMinty)

        self.aqua = QLabel('', self)
        self.aqua.setPixmap(QPixmap('image/type/more_result/more_result_aqua.png'))
        self.aqua.resize(310, 110)
        self.aqua.move(345, 228)
        self.aqua.setAlignment(Qt.AlignCenter)
        self.aqua.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.aqua).connect(self.showAqua)

        self.watery = QLabel('', self)
        self.watery.setPixmap(QPixmap('image/type/more_result/more_result_watery.png'))
        self.watery.resize(310, 110)
        self.watery.move(670, 228)
        self.watery.setAlignment(Qt.AlignCenter)
        self.watery.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.watery).connect(self.showWatery)


        #3열
        self.green = QLabel('', self)
        self.green.setPixmap(QPixmap('image/type/more_result/more_result_green.png'))
        self.green.resize(310, 110)
        self.green.move(20, 350)
        self.green.setAlignment(Qt.AlignCenter)
        self.green.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.green).connect(self.showGreen)

        self.woody = QLabel('', self)
        self.woody.setPixmap(QPixmap('image/type/more_result/more_result_woody.png'))
        self.woody.resize(310, 110)
        self.woody.move(345, 350)
        self.woody.setAlignment(Qt.AlignCenter)
        self.woody.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.woody).connect(self.showWoody)

        self.mossy = QLabel('', self)
        self.mossy.setPixmap(QPixmap('image/type/more_result/more_result_mossy.png'))
        self.mossy.resize(310, 110)
        self.mossy.move(670, 350)
        self.mossy.setAlignment(Qt.AlignCenter)
        self.mossy.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.mossy).connect(self.showMossy)


        #4열
        self.tobacco_leather = QLabel('', self)
        self.tobacco_leather.setPixmap(QPixmap('image/type/more_result/more_result_tobacco-leather.png'))
        self.tobacco_leather.resize(310, 110)
        self.tobacco_leather.move(20, 470)
        self.tobacco_leather.setAlignment(Qt.AlignCenter)
        self.tobacco_leather.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.tobacco_leather).connect(self.showTobacco_leather)

        self.gourmans = QLabel('', self)
        self.gourmans.setPixmap(QPixmap('image/type/more_result/more_result_gourmans.png'))
        self.gourmans.resize(310, 110)
        self.gourmans.move(345, 470)
        self.gourmans.setAlignment(Qt.AlignCenter)
        self.gourmans.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.gourmans).connect(self.showGourmans)

        self.dry = QLabel('', self)
        self.dry.setPixmap(QPixmap('image/type/more_result/more_result_dry.png'))
        self.dry.resize(310, 110)
        self.dry.move(670, 470)
        self.dry.setAlignment(Qt.AlignCenter)
        self.dry.setScaledContents(1)  # 이미지 크기에 맞게 조정
        main.clickable(self.dry).connect(self.showDry)




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

    def showFloral(self):
        from result1 import ResultWindow
        self.show_floral = ResultWindow()
        self.show_floral.show()
        self.hide()

    def showMusk(self):
        from result2 import ResultWindow
        self.show_musk = ResultWindow()
        self.show_musk.show()
        self.hide()

    def showWoody(self):
        from result3 import ResultWindow
        self.show_woody = ResultWindow()
        self.show_woody.show()
        self.hide()

    def showFruity(self):
        from result4 import ResultWindow
        self.show_fruity = ResultWindow()
        self.show_fruity.show()
        self.hide()

    def showGreen(self):
        from result5 import ResultWindow
        self.show_green = ResultWindow()
        self.show_green.show()
        self.hide()

    def showAqua(self):
        from result6 import ResultWindow
        self.show_aqua = ResultWindow()
        self.show_aqua.show()
        self.hide()

    def showGourmans(self):
        from result7 import ResultWindow
        self.show_gourmans = ResultWindow()
        self.show_gourmans.show()
        self.hide()

    def showMossy(self):
        from result8 import ResultWindow
        self.show_mossy = ResultWindow()
        self.show_mossy.show()
        self.hide()

    def showTobacco_leather(self):
        from result9 import ResultWindow
        self.show_mossy = ResultWindow()
        self.show_mossy.show()
        self.hide()

    def showDry(self):
        from result10 import ResultWindow
        self.show_dry = ResultWindow()
        self.show_dry.show()
        self.hide()

    def showMinty(self):
        from result11 import ResultWindow
        self.show_minty = ResultWindow()
        self.show_minty.show()
        self.hide()

    def showWatery(self):
        from result12 import ResultWindow
        self.show_watery = ResultWindow()
        self.show_watery.show()
        self.hide()


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