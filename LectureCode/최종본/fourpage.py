import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QWidget, QLabel, QSizePolicy,
                             QPushButton, QApplication, QVBoxLayout,
                             QHBoxLayout, QDesktopWidget, QDialog,
                             QLineEdit)
from PyQt5.QtGui import QFontDatabase, QFont, QImage, QPalette, QBrush, QIcon


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

        result_txt = open('textFile/result.txt', 'r', encoding='utf8')
        self.result_list = []
        for line in result_txt:
            word = line.rstrip('\n')
            self.result_list.append(word)
        result_txt.close()

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
        self.font = [i for i in range(3)]
        fontSizeList = [100, 30, 20]

        for i in range(3):
            self.font[i] = QFont("나눔스퀘어_ac Bold", fontSizeList[i])
            self.font[i].setBold(True)

        # 각종 버튼 및 라벨 선언
        self.resultLabel = QLabel('당신의 결과는?')
        self.resultLabel.setAlignment(Qt.AlignCenter)
        self.resultLabel.setFont(self.font[1])

        self.questionCorrect = self.result_list[1]
        self.questionTotal = 10
        self.scoreLabel = QLabel(f"{self.questionCorrect}/{self.questionTotal}")
        self.scoreLabel.setAlignment(Qt.AlignCenter)
        self.scoreLabel.setFont(self.font[0])

        self.scoreLetterLabel = QLabel("맞은 문제 수 / 총 문제수")
        self.scoreLetterLabel.setAlignment(Qt.AlignCenter)
        self.scoreLetterLabel.setFont(self.font[2])

        self.messages = ['"좌절하지 말아요 ㅠㅠ"', '"많이 어려웠나요?"', '"조금 더 노력하세요!"',
                         '"좋아요, 나쁘지 않아요!"', '"훌륭한 시각을 가지셨군요!"', '"당신은 색깔 구분 마스터!"']
        if int(self.questionCorrect) == 10:
            self.scoreCommentLabel = QLabel(self.messages[5])
        elif int(self.questionCorrect) >= 8:
            self.scoreCommentLabel = QLabel(self.messages[4])
        elif int(self.questionCorrect) >= 6:
            self.scoreCommentLabel = QLabel(self.messages[3])
        elif int(self.questionCorrect) >= 4:
            self.scoreCommentLabel = QLabel(self.messages[2])
        elif int(self.questionCorrect) >= 2:
            self.scoreCommentLabel = QLabel(self.messages[1])
        else:
            self.scoreCommentLabel = QLabel(self.messages[0])

        self.scoreCommentLabel.setAlignment(Qt.AlignCenter)
        self.scoreCommentLabel.setFont(self.font[1])

        self.restartButton = QPushButton("")
        self.restartButton.setIcon(QIcon("image/restart.png"))
        self.restartButton.setIconSize(QSize(150, 150))
        self.restartButton.clicked.connect(self.fourpage)
        self.restartLabel = QLabel("다시하기")
        self.restartLabel.setAlignment(Qt.AlignCenter)
        self.restartLabel.setFont(self.font[2])

        self.finishButton = QPushButton("")
        self.finishButton.setIcon(QIcon("image/finish.png"))
        self.finishButton.setIconSize(QSize(150, 150))
        self.finishButton.clicked.connect(self.clikedFinish)
        self.finishLabel = QLabel("끝내기")
        self.finishLabel.setAlignment(Qt.AlignCenter)
        self.finishLabel.setFont(self.font[2])

        self.referenceButton = QPushButton(" 참고 자료 ")
        self.referenceButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.referenceButton.setFont(self.font[2])
        self.referenceButton.clicked.connect(self.clickedReference)

        # 하위 레이아웃
        self.restartBox = QVBoxLayout()
        self.restartBox.addWidget(self.restartButton)
        self.restartBox.addWidget(self.restartLabel)

        self.finishBox = QVBoxLayout()
        self.finishBox.addWidget(self.finishButton)
        self.finishBox.addWidget(self.finishLabel)

        self.buttonBox = QHBoxLayout()
        self.buttonBox.addStretch(1)
        self.buttonBox.addLayout(self.restartBox)
        self.buttonBox.addLayout(self.finishBox)
        self.buttonBox.addStretch(1)

        self.bottomBox = QHBoxLayout()
        self.bottomBox.addStretch(1)
        self.bottomBox.addWidget(self.referenceButton)

        # 메인 레이아웃
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addSpacing(70)
        self.mainLayout.addWidget(self.resultLabel)
        self.mainLayout.addSpacing(10)
        self.mainLayout.addWidget(self.scoreLabel)
        self.mainLayout.addWidget(self.scoreLetterLabel)
        self.mainLayout.addSpacing(30)
        self.mainLayout.addWidget(self.scoreCommentLabel)
        self.mainLayout.addSpacing(30)
        self.mainLayout.addLayout(self.buttonBox)
        self.mainLayout.addStretch(1)
        self.mainLayout.addLayout(self.bottomBox)

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

    def clickedReference(self):
        ReferenceLayout(self)

    def clikedFinish(self):
        self.text_list[1] = '3'
        self.text_list[3] = '3'
        a = open('textFile/setting.txt', 'w', encoding='utf8')
        for p in self.text_list:
            a.write(p + '\n')
        a.close()

        self.question_number_list[1] = '1'
        b = open('textFile/question_number.txt', 'w', encoding='utf8')
        for p in self.question_number_list:
            b.write(p + '\n')
        b.close()

        self.answer_color_list = ['colorList']
        c = open('textFile/colorList.txt', 'w', encoding='utf8')
        for p in self.answer_color_list:
            c.write(p + '\n')
        c.close()

        self.result_list[1] = '0'
        d = open('textFile/result.txt', 'w', encoding='utf8')
        for p in self.result_list:
            d.write(p + '\n')
        d.close()

        self.close()

    def fourpage(self):
        self.question_number_list[1] = '1'
        b = open('textFile/question_number.txt', 'w', encoding='utf8')
        for p in self.question_number_list:
            b.write(p + '\n')
        b.close()

        self.answer_color_list = ['colorList']
        c = open('textFile/colorList.txt', 'w', encoding='utf8')
        for p in self.answer_color_list:
            c.write(p + '\n')
        c.close()

        self.result_list[1] = '0'
        d = open('textFile/result.txt', 'w', encoding='utf8')
        for p in self.result_list:
            d.write(p + '\n')
        d.close()

        self.switch_window.emit()

    def closeEvent(self, event):
        self.text_list[1] = '3'
        self.text_list[3] = '3'
        a = open('textFile/setting.txt', 'w', encoding='utf8')
        for p in self.text_list:
            a.write(p + '\n')
        a.close()

        self.question_number_list[1] = '1'
        b = open('textFile/question_number.txt', 'w', encoding='utf8')
        for p in self.question_number_list:
            b.write(p + '\n')
        b.close()

        self.answer_color_list = ['colorList']
        c = open('textFile/colorList.txt', 'w', encoding='utf8')
        for p in self.answer_color_list:
            c.write(p + '\n')
        c.close()

        self.result_list[1] = '0'
        d = open('textFile/result.txt', 'w', encoding='utf8')
        for p in self.result_list:
            d.write(p + '\n')
        d.close()
        self.deleteLater()
        event.accept()


class ReferenceLayout(QDialog):

    def __init__(self, parent):
        super(ReferenceLayout, self).__init__(parent)

        # 배경 설정
        oImage = QImage("image/gray.jpg")
        sImage = oImage.scaled(1000, 700)
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        # 폰트 설정
        QFontDatabase.addApplicationFont("NanumSquare_acB.ttf")
        self.font = [i for i in range(3)]
        fontSizeList = [20, 15, 12]
        for i in range(3):
            self.font[i] = QFont("나눔스퀘어_ac Bold", fontSizeList[i])
            self.font[i].setBold(True)

        self.referenceLabel1 = QLabel("- 창이 모니터의 중앙에 배치되도록 구현할 때 참고한 코드")
        self.referenceLabel1.setFont(self.font[1])
        # self.referenceLabel1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.referenceText1 = QLineEdit()
        self.referenceText1.setText("https://wikidocs.net/26684")
        self.referenceText1.setFont(self.font[2])
        self.referenceText1.setReadOnly(True)
        self.referenceText1.setStyleSheet("background-color: rgba(255, 255, 255, 128);")

        self.referenceLabel2 = QLabel("- 각 페이지를 넘나들 수 있도록 구현할 때 참고한 코드")
        self.referenceLabel2.setFont(self.font[1])
        # self.referenceLabel2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.referenceText2 = QLineEdit()
        self.referenceText2.setText("https://gist.github.com/MalloyDelacroix/2c509d6bcad35c7e35b1851dfc32d161")
        self.referenceText2.setFont(self.font[2])
        self.referenceText2.setReadOnly(True)
        self.referenceText2.setStyleSheet("background-color: rgba(255, 255, 255, 128);")

        self.referenceLabel3 = QLabel("- 타이머를 사용할 때 참고한 코드")
        self.referenceLabel3.setFont(self.font[1])
        # self.referenceLabel3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.referenceText3 = QLineEdit()
        self.referenceText3.setText("https://makersweb.net/python/1098")
        self.referenceText3.setFont(self.font[2])
        self.referenceText3.setReadOnly(True)
        self.referenceText3.setStyleSheet("background-color: rgba(255, 255, 255, 128);")

        self.referenceLabel4 = QLabel("- 배경 이미지를 설정할 때 참고한 코드")
        self.referenceLabel4.setFont(self.font[1])

        self.referenceText4 = QLineEdit()
        self.referenceText4.setText("https://lsjsj92.tistory.com/319")
        self.referenceText4.setFont(self.font[2])
        self.referenceText4.setReadOnly(True)
        self.referenceText4.setStyleSheet("background-color: rgba(255, 255, 255, 128);")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.referenceLabel1)
        self.mainLayout.addWidget(self.referenceText1)
        self.mainLayout.addSpacing(80)
        self.mainLayout.addWidget(self.referenceLabel2)
        self.mainLayout.addWidget(self.referenceText2)
        self.mainLayout.addSpacing(80)
        self.mainLayout.addWidget(self.referenceLabel3)
        self.mainLayout.addWidget(self.referenceText3)
        self.mainLayout.addSpacing(80)
        self.mainLayout.addWidget(self.referenceLabel4)
        self.mainLayout.addWidget(self.referenceText4)
        self.mainLayout.addStretch(1)

        # 창 기본 설정
        self.setFixedSize(1000, 700)
        self.setWindowTitle('참고 자료')
        self.setWindowIcon(QIcon("image/colortable.png"))

        self.setLayout(self.mainLayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Layout()
    sys.exit(app.exec_())