#선택지 화면 - 질문 n개 질문 안에 선택지 n개를 보여주는 페이지
import sys
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
        self.label.setPixmap(QPixmap('image/choice/question/age.png'))
        self.label.resize(600, 100)
        self.label.move(210, 45)
        self.label.setAlignment(Qt.AlignCenter)

        # creating a button widget
        self.startBtn = QLabel('', self)
        self.startBtn.setPixmap(QPixmap('image/choice/answer/10대.png'))
        self.startBtn.resize(150, 100)
        self.startBtn.move(130, 380)
        self.startBtn.setAlignment(Qt.AlignCenter)
        self.startBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정

        self.startBtn = QLabel('', self)
        self.startBtn.setPixmap(QPixmap('image/choice/answer/20대.png'))
        self.startBtn.resize(150, 100)
        self.startBtn.move(420, 380)
        self.startBtn.setAlignment(Qt.AlignCenter)
        self.startBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정

        self.startBtn = QLabel('', self)
        self.startBtn.setPixmap(QPixmap('image/choice/answer/30대.png'))
        self.startBtn.resize(150, 100)
        self.startBtn.move(700, 380)
        self.startBtn.setAlignment(Qt.AlignCenter)
        self.startBtn.setScaledContents(1)  # 이미지 크기에 맞게 조정




if __name__ == '__main__':
    app = QApplication(sys.argv)
    chooseWindow = ChooseWindow()
    chooseWindow.show()
    sys.exit(app.exec_())