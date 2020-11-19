## Ex 3-1. 창 띄우기.
#시작화면 - 디자인 위주, 시작 버튼, 간단한 스토리/플레이 방법 설명 버튼
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MSTI')
        self.setWindowIcon(QIcon('image/horse.jpg'))
        self.setGeometry(300, 300, 300, 200)

        self.move(300, 300)
        self.resize(1000, 600)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())