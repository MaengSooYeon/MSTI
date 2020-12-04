# 결과로 나온 타입의 이름과 빈도수를 볼 수 있는 화면

import re
# import string
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

# result.txt 파일에 있는 결과 빈도 수 구하는 코드
frequency = {}
document_text = open('file/result.txt', 'r', encoding='utf-8')
text_string = document_text.read()
match_pattern = re.findall(r'\b[가-힣]+\b', text_string)
# match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()

f = open("file/result_cnt.txt", 'w+', encoding='utf-8')
for words in frequency_list:
    data = f'{words} type {frequency[words]}\n'
    f.write(data)
    # print(words,'type', frequency[words])
f.close()

class showResultWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # window setting
        self.setStyleSheet('background-color: #FFFFFF')
        self.setWindowTitle('MSTI')
        self.setWindowIcon(QIcon('image/icon.png'))
        self.setFixedSize(1000, 600)
        self.center()

        # result count txt file
        with open('file/result_cnt.txt', 'r', encoding='utf8') as file:
            content = file.read()
            self.content = QLabel(content, self)
            self.content.resize(710, 500)
            self.content.move(10, 100)
            self.content.setAlignment(Qt.AlignCenter)
            self.content.setScaledContents(1)
            self.content.setFont(QFont("한컴산뜻돋움", 14))
            print(content)
            file.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_result_window = showResultWindow()
    show_result_window.show()
    sys.exit(app.exec_())