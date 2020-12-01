#선택지 화면 - 질문 n개 질문 안에 선택지 n개를 보여주는 페이지
import sys
import choose3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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

class ChooseWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet('background-color: #FFFFFF')
        self.setWindowTitle('CHOOSE')
        self.setWindowIcon(QIcon('image/horse.jpg'))
        self.setFixedSize(1000, 600)

        # creating questions widget
        self.label = QLabel('', self)
        self.label.setPixmap(QPixmap('image/choice/question/feel.png'))
        self.label.resize(750, 100)
        self.label.move(160, 45)
        self.label.setAlignment(Qt.AlignCenter)

        # creating a button widget
        self.calmtBtn = QLabel('', self)
        self.calmtBtn.setPixmap(QPixmap('image/choice/answer/차분함.png'))
        self.calmtBtn.resize(150, 100)
        self.calmtBtn.move(270, 380)
        self.calmtBtn.setAlignment(Qt.AlignCenter)
        self.calmtBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        choose3.clickable(self.calmtBtn).connect(self.showChoose3)

        self.livelyBtn = QLabel('', self)
        self.livelyBtn.setPixmap(QPixmap('image/choice/answer/생동감.png'))
        self.livelyBtn.resize(150, 100)
        self.livelyBtn.move(600, 380)
        self.livelyBtn.setAlignment(Qt.AlignCenter)
        self.livelyBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        choose3.clickable(self.livelyBtn).connect(self.showChoose3)

    def showChoose3(self):
        self.show_choose3 = choose3.ChooseWindow()
        self.show_choose3.show()
        self.hide()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    chooseWindow = ChooseWindow()
    chooseWindow.show()
    sys.exit(app.exec_())