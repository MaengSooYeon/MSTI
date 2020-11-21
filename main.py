## Ex 3-1. 창 띄우기.
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
        # window settings
        self.setStyleSheet('background-color: white;')
        self.setWindowTitle('MSTI')
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

        # QDialog 설정
        self.dialog = QDialog()

    # 버튼 이벤트 함수
    def showChoose(self):
        QMessageBox.about(self, "message", "clicked")
        #choose Gui창으로 넘어가게 바꾸기

    # 버튼 이벤트 함수
    def dialog_open(self):
        # creating a label widget
        self.labelDialog = QLabel("설명~", self.dialog)
        self.labelDialog.setAlignment(Qt.AlignCenter)
        self.fontDialog = self.labelDialog.font()
        self.fontDialog.setFamily('Times New Roman')    #폰트 바꾸기
        self.fontDialog.setBold(True)
        self.fontDialog.setPointSize(30)

        self.labelDialog.setFont(self.fontDialog)
        self.labelDialog.move(120, 100)

        self.closeBtn = QLabel('', self.dialog)
        self.closeBtn.setPixmap(QPixmap('image/CloseBtn.png'))
        self.closeBtn.resize(80, 50)
        self.closeBtn.move(480, 320)
        self.closeBtn.setScaledContents(1)    #이미지 크기에 맞게 조정
        clickable(self.closeBtn).connect(self.dialog_close)

        # QDialog 세팅
        self.dialog.setStyleSheet('background-color: white;')
        self.dialog.setWindowTitle('MSTI')
        self.dialog.setWindowIcon(QIcon('image/horse.jpg'))
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.resize(600, 400)
        self.dialog.show()

    # Dialog 닫기 이벤트
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


