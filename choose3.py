#선택지 화면 - 질문 n개 질문 안에 선택지 n개를 보여주는 페이지
import sys
import choose4

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
        self.label.setPixmap(QPixmap('image/choice/question/image.png'))
        self.label.resize(600, 100)
        self.label.move(210, 45)
        self.label.setAlignment(Qt.AlignCenter)

        # creating a button widget
        self.meekBtn = QLabel('', self)
        self.meekBtn.setPixmap(QPixmap('image/choice/answer/순한.png'))
        self.meekBtn.resize(150, 100)
        self.meekBtn.move(270, 380)
        self.meekBtn.setAlignment(Qt.AlignCenter)
        self.meekBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        choose4.clickable(self.meekBtn).connect(self.showChoose4)

        self.strongBtn = QLabel('', self)
        self.strongBtn.setPixmap(QPixmap('image/choice/answer/강렬한.png'))
        self.strongBtn.resize(150, 100)
        self.strongBtn.move(600, 380)
        self.strongBtn.setAlignment(Qt.AlignCenter)
        self.strongBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정
        choose4.clickable(self.strongBtn).connect(self.showChoose4)

    def showChoose4(self):
        self.show_choose4 = choose4.ChooseWindow()
        self.show_choose4.show()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chooseWindow = ChooseWindow()
    chooseWindow.show()
    sys.exit(app.exec_())