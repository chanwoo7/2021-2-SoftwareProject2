import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QSizePolicy,
                             QPushButton, QApplication, QVBoxLayout,
                             QHBoxLayout, QDesktopWidget, QGridLayout)
from PyQt5.QtGui import QFontDatabase, QFont, QImage, QPalette, QBrush, QIcon
from choicesColorDecision import ChoicesColorDecision


class Layout(QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        # 세팅 불러오기
        setting_txt = open('textFile/setting.txt', 'r', encoding='utf8')
        self.text_list = []
        for line in setting_txt:
            word = line.rstrip('\n')
            self.text_list.append(word)

        setting_txt.close()

        question_number_txt = open('textFile/question_number.txt', 'r', encoding='utf8')
        self.question_number_list = []
        for line in question_number_txt:
            word = line.rstrip('\n')
            self.question_number_list.append(word)

        question_number_txt.close()

        colorList_txt = open('textFile/colorList.txt', 'r', encoding='utf8')
        self.answer_color_list = []
        for line in colorList_txt:
            word = line.rstrip('\n')
            self.answer_color_list.append(word)

        colorList_txt.close()

        # 배경 설정
        oImage = QImage("image/gray.jpg")
        sImage = oImage.scaled(1500, 900)
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        # 폰트 설정
        QFontDatabase.addApplicationFont("NanumSquare_acB.ttf")
        self.font = QFont("나눔스퀘어_ac Bold", 30)
        self.font.setBold(True)

        # 각종 버튼 및 라벨 선언
        self.questionCurr = self.question_number_list[1]  # 일단 임의로 지정한 수 (연결 필요)
        self.questionTotal = 10  # 일단 임의로 지정한 수 (연결 필요)
        self.questionNumLabel = QLabel(f"{self.questionCurr}/{self.questionTotal}")
        self.questionNumLabel.repaint()
        self.questionNumLabel.setFont(self.font)

        self.label1 = QLabel("무슨 색 이게?")
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setFont(self.font)

        self.button = [i for i in range(12)]
        self.colorList = ChoicesColorDecision().decide(int(self.text_list[3]), self.answer_color_list[-1])

        for i in range(12):
            self.button[i] = QPushButton("")
            self.button[i].setStyleSheet(f"background-color: #{self.colorList[i]}")
            self.button[i].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.button[i].clicked.connect(lambda state, x=i: self.compare(x))

        # 하위 레이아웃
        self.topBox = QHBoxLayout()
        self.topBox.addWidget(self.questionNumLabel)
        self.topBox.addStretch(1)

        self.colorGrid = QGridLayout()
        r, c = 0, 0
        for button in self.button:
            if c > 3:
                r += 1; c = 0
            self.colorGrid.addWidget(button, r, c)
            c += 1

        # 메인 레이아웃
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.topBox)
        self.mainLayout.addSpacing(10)
        self.mainLayout.addWidget(self.label1)
        self.mainLayout.addSpacing(10)
        self.mainLayout.addLayout(self.colorGrid)

        # 창 기본 설정
        self.setFixedSize(1500, 900)
        self.setWindowTitle('무슨 색이게?')
        self.setWindowIcon(QIcon("image/colortable.png"))

        # 창을 모니터의 중앙에 정렬
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        self.setLayout(self.mainLayout)

        self.show()

    def compare(self, num):
        result_txt = open('textFile/result.txt', 'r', encoding='utf8')
        self.result_list = []
        self.num = num
        for line in result_txt:
            word = line.rstrip('\n')
            self.result_list.append(word)

        result_txt.close()

        if self.colorList[num] == self.answer_color_list[-1]:
            self.result_list[1] = int(self.result_list[1])
            self.result_list[1] += 1
            self.result_list[1] = str(self.result_list[1])
            a = open('textFile/result.txt', 'w', encoding='utf8')
            for p in self.result_list:
                a.write(p + '\n')
            a.close()
        self.switch_window.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Layout()
    sys.exit(app.exec_())
