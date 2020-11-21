#시작화면 - 디자인 위주, 시작 버튼, 간단한 스토리/플레이 방법 설명 버튼
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

#label로 클릭이벤트를 사용하기 위해서.
#https://wiki.python.org/moin/PyQt/Making%20non-clickable%20widgets%20clickable
def clickable(widget):
    class Filter(QObject):
        clicked = pyqtSignal()  # pyside2 사용자는 pyqtSignal() -> Signal()로 변경

        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
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
        #https://wikidocs.net/21853 아이콘넣기
        self.setWindowIcon(QIcon('image/horse.jpg'))
        self.setFixedSize(1000, 600)
        self.center()

        # creating a label widget
        self.label = QLabel('', self)
        self.label.setPixmap(QPixmap('image/Title.png'))
        self.label.resize(540, 120)
        self.label.move(210, 120)
        self.label.setAlignment(Qt.AlignCenter)

        self.startBtn = QLabel('', self)
        self.startBtn.setPixmap(QPixmap('image/TestStartBtn.png'))
        self.startBtn.resize(200, 75)
        self.startBtn.move(530, 380)
        self.startBtn.setAlignment(Qt.AlignCenter)
        self.startBtn.setScaledContents(1)    #이미지 크기에 맞게 조정
        clickable(self.startBtn).connect(self.showChoose)

        self.howPlayBtn = QLabel('', self)
        self.howPlayBtn.setPixmap(QPixmap('image/HowToPlayBtn.png'))
        self.howPlayBtn.resize(200, 75)
        self.howPlayBtn.move(240, 380)
        self.howPlayBtn.setAlignment(Qt.AlignCenter)
        self.howPlayBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        clickable(self.howPlayBtn).connect(self.dialog_open)

        # QDialog setting
        self.dialog = QDialog()

    # button event function
    def showChoose(self):
        QMessageBox.about(self, "message", "clicked")
        #choose Gui창으로 넘어가게 바꾸기

    # button event function
    def dialog_open(self):
        # creating a label widget
        self.contents = QLabel('', self.dialog)
        self.contents.setPixmap(QPixmap('image/contents.png'))
        self.contents.resize(500, 210)
        self.contents.move(50, 75)
        self.contents.setAlignment(Qt.AlignCenter)
        self.contents.setScaledContents(1)  # 이미지 크기에 맞게 조정

        self.closeBtn = QLabel('', self.dialog)
        self.closeBtn.setPixmap(QPixmap('image/CloseBtn.png'))
        self.closeBtn.resize(80, 50)
        self.closeBtn.move(480, 320)
        self.closeBtn.setScaledContents(1)    #이미지 크기에 맞게 조정
        clickable(self.closeBtn).connect(self.dialog_close)

        # QDialog setting
        self.dialog.setStyleSheet('background-color: white;')
        self.dialog.setWindowTitle('MSTI')
        self.dialog.setWindowIcon(QIcon('image/horse.jpg'))
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(600, 400)
        self.dialog.show()

    # Dialog close event
    def dialog_close(self):
        self.dialog.close()
        self.show()

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


