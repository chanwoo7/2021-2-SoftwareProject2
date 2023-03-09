# https://makersweb.net/python/1098
import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import (QWidget, QLabel, QSizePolicy,
                             QApplication, QVBoxLayout, QHBoxLayout,
                             QDesktopWidget, QPushButton)
from PyQt5.QtGui import QFontDatabase, QFont, QImage, QPalette, QBrush, QIcon
from random import randint


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

        self.timeCount = None

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
        self.questionCurr = self.question_number_list[1]    # 일단 임의로 지정한 수 (연결 필요)
        self.questionTotal = 10
        self.questionNumLabel = QLabel(f"{self.questionCurr}/{self.questionTotal}")
        self.questionNumLabel.setFont(self.font)

        self.waitLabel = QLabel("아래에 표시되는 색을 기억하세요!")  # 그냥 색만 달랑 나오기엔 이상할 것 같아서 넣어봄, 빼도 됨
        self.waitLabel.setAlignment(Qt.AlignCenter)
        self.waitLabel.setFont(self.font)

        self.transparentColor = QLabel("")
        self.transparentColor.setStyleSheet("background-color: #{00000000}")
        self.transparentColor.setAlignment(Qt.AlignCenter)
        self.transparentColor.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.showButton = QPushButton("색 보기 (Show)")
        self.showButton.setFont(self.font)
        self.showButton.clicked.connect(self.showColor)

        # 하위 레이아웃
        self.topBox = QHBoxLayout()
        self.topBox.addWidget(self.questionNumLabel)
        self.topBox.addStretch(1)

        self.colorBox = QHBoxLayout()
        self.colorBox.addSpacing(400)
        self.colorBox.addWidget(self.transparentColor)
        self.colorBox.addSpacing(400)

        self.showButtonBox = QHBoxLayout()
        self.showButtonBox.addSpacing(500)
        self.showButtonBox.addWidget(self.showButton)
        self.showButtonBox.addSpacing(500)

        # 메인 레이아웃
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.topBox)
        self.mainLayout.addSpacing(10)
        self.mainLayout.addWidget(self.waitLabel)
        self.mainLayout.addSpacing(10)
        self.mainLayout.addLayout(self.colorBox)
        self.mainLayout.addSpacing(10)
        self.mainLayout.addLayout(self.showButtonBox)
        self.mainLayout.addSpacing(30)

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

    def showColor(self):
        colorList_txt = open('textFile/colorList.txt', 'r', encoding='utf8')
        self.answer_color_list = []
        for line in colorList_txt:
            word = line.rstrip('\n')
            self.answer_color_list.append(word)

        colorList_txt.close()

        r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
        self.answer_color = "%02x%02x%02x" % (r, g, b)

        self.answer_color_list.append(self.answer_color)
        a = open('textFile/colorList.txt', 'w', encoding='utf8')
        for p in self.answer_color_list:
            a.write(p + '\n')
        a.close()

        self.color = QLabel("")
        self.color.setStyleSheet(f"background-color: #{self.answer_color}")
        self.color.setAlignment(Qt.AlignCenter)
        self.color.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.colorBox.replaceWidget(self.transparentColor, self.color)

        self.showButton.setDisabled(True)
        if self.timeCount:
            self.timeCount.stop()
            self.timeCount.deleteLater()
        self.timeCount = QTimer()
        self.timeCount.timeout.connect(self.twopage)
        self.timeCount.setSingleShot(True)
        self.timeCount.start(int(self.text_list[1])*500)

    def twopage(self):
        self.switch_window.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Layout()
    sys.exit(app.exec_())
