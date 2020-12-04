#시작화면

import sys
import test_record

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#클릭이벤트 함수
def clickable(widget):
    class Filter(QObject):
        # pyside2 사용자는 pyqtSignal() -> Signal()로 변경
        clicked = pyqtSignal()

        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()     #객체를 가져오기 위해 .emit() 사용
                        return True
            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # window setting
        self.setStyleSheet('background-color: #FFFFFF')
        self.setWindowTitle('MSTI')
        self.setWindowIcon(QIcon('image/icon.png'))
        self.setFixedSize(1000, 600)
        self.center()

        # creating widget - title
        self.label = QLabel('', self)
        self.label.setPixmap(QPixmap('image/Title.png'))
        self.label.resize(540, 120)
        self.label.move(210, 120)
        self.label.setAlignment(Qt.AlignCenter)

        # creating widget - button
        self.startBtn = QLabel('', self)
        self.startBtn.setPixmap(QPixmap('image/testStart_btn.png'))
        self.startBtn.resize(200, 75)
        self.startBtn.move(530, 380)
        self.startBtn.setAlignment(Qt.AlignCenter)
        self.startBtn.setScaledContents(1)    #이미지 크기에 맞게 조정
        clickable(self.startBtn).connect(self.showChoose)

        self.contentsBtn = QLabel('', self)
        self.contentsBtn.setPixmap(QPixmap('image/contents_btn.png'))
        self.contentsBtn.resize(200, 75)
        self.contentsBtn.move(240, 380)
        self.contentsBtn.setAlignment(Qt.AlignCenter)
        self.contentsBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        clickable(self.contentsBtn).connect(self.dialogOpen)

        self.recordBtn = QLabel('', self)
        self.recordBtn.setPixmap(QPixmap('image/test_record.png'))
        self.recordBtn.resize(180, 50)
        self.recordBtn.move(780, 25)
        self.recordBtn.setAlignment(Qt.AlignCenter)
        self.recordBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        clickable(self.recordBtn).connect(self.showRecord)

        # QDialog setting
        self.dialog = QDialog()


    # button event function
    def showChoose(self):
        from choose1 import ChooseWindow
        self.show_choose = ChooseWindow()
        self.show_choose.show()
        self.hide()

    def showRecord(self):
        self.show_record = test_record.showRecordWindow()
        self.show_record.show()
        self.hide()

    def dialogOpen(self):
        # creating widget - content
        self.contents = QLabel('', self.dialog)
        self.contents.setPixmap(QPixmap('image/contents.png'))
        self.contents.resize(530, 230)
        self.contents.move(0, 40)
        self.contents.setAlignment(Qt.AlignCenter)
        self.contents.setScaledContents(1)  # 이미지 크기에 맞게 조정

        # QDialog setting
        self.dialog.setStyleSheet('background-color: white;')
        self.dialog.setWindowTitle('MSTI')
        self.dialog.setWindowIcon(QIcon('image/icon.png'))
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(520, 300)
        self.dialog.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
