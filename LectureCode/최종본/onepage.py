import sys
from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QWidget, QLabel, QSizePolicy,
                             QPushButton, QApplication, QVBoxLayout,
                             QHBoxLayout, QDesktopWidget, QDialog,
                             QSlider, QTextEdit)
from PyQt5.QtGui import QFontDatabase, QFont, QImage, QPalette, QBrush, QIcon


class Layout(QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

        # 배경 설정
        oImage = QImage("image/gray.jpg")
        sImage = oImage.scaled(1500, 900)
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        # 폰트 설정
        QFontDatabase.addApplicationFont("NanumSquare_acB.ttf")

        self.font = [i for i in range(4)]
        fontSizeList = [50, 30, 20, 10]

        for i in range(4):
            self.font[i] = QFont("나눔스퀘어_ac Bold", fontSizeList[i])
            self.font[i].setBold(True)

        # 각종 버튼 및 라벨 선언
        self.settingButton = QPushButton("")
        self.settingButton.setIcon(QIcon("image/settingIcon.png"))
        self.settingButton.setIconSize(QSize(70, 70))
        self.settingButton.clicked.connect(self.clickedSetting)
        self.settingLabel = QLabel("설정")
        self.settingLabel.setFont(self.font[3])
        self.settingLabel.setAlignment(Qt.AlignCenter)

        self.helpButton = QPushButton("")
        self.helpButton.setIcon(QIcon("image/questionIcon.png"))
        self.helpButton.setIconSize(QSize(70, 70))
        self.helpButton.clicked.connect(self.clickedHelp)
        self.helpLabel1 = QLabel("도움말")
        self.helpLabel1.setFont(self.font[3])
        self.helpLabel1.setAlignment(Qt.AlignCenter)

        self.titleLabel = QLabel('무슨 색이게?')
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFont(self.font[0])

        self.subtitleLabel = QLabel('색 민감도 테스트')
        self.subtitleLabel.setAlignment(Qt.AlignCenter)
        self.subtitleLabel.setFont(self.font[2])

        self.startButton = QPushButton("게임 시작! (Start)")
        self.startButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.startButton.setFont(self.font[1])
        self.startButton.clicked.connect(self.onepage)

        self.ourName = QLabel("AD프로젝트 1조 - 20213062 이찬우, 20213075 전석환 제작")
        self.ourName.setFont(self.font[3])

        # 하위 레이아웃
        self.settingBox = QVBoxLayout()
        self.settingBox.addWidget(self.settingButton)
        self.settingBox.addWidget(self.settingLabel)

        self.helpBox = QVBoxLayout()
        self.helpBox.addWidget(self.helpButton)
        self.helpBox.addWidget(self.helpLabel1)

        self.topBox = QHBoxLayout()
        self.topBox.addStretch(1)
        self.topBox.addLayout(self.settingBox)
        self.topBox.addLayout(self.helpBox)

        self.startBox = QHBoxLayout()
        self.startBox.addSpacing(200)
        self.startBox.addWidget(self.startButton)
        self.startBox.addSpacing(200)

        self.bottomBox = QHBoxLayout()
        self.bottomBox.addStretch(1)
        self.bottomBox.addWidget(self.ourName)

        # 메인 레이아웃
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.topBox)
        self.mainLayout.addSpacing(10)
        self.mainLayout.addWidget(self.titleLabel)
        self.mainLayout.addSpacing(10)
        self.mainLayout.addWidget(self.subtitleLabel)
        self.mainLayout.addSpacing(100)
        self.mainLayout.addLayout(self.startBox)
        self.mainLayout.addSpacing(100)
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

    def clickedSetting(self):
        SettingLayout(self)

    def clickedHelp(self):
        HelpLayout(self)

    def onepage(self):
        self.switch_window.emit()


class SettingLayout(QDialog):

    def __init__(self, parent):
        super(SettingLayout, self).__init__(parent)

        # 세팅 불러오기
        setting_txt = open('textFile/setting.txt', 'r', encoding='utf8')
        self.text_list = []
        for line in setting_txt:
            word = line.rstrip('\n')
            self.text_list.append(word)

        setting_txt.close()

        # 배경 설정
        oImage = QImage("image/gray.jpg")
        sImage = oImage.scaled(500, 500)
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        # 폰트 설정
        QFontDatabase.addApplicationFont("NanumSquare_acB.ttf")
        self.font = QFont("나눔스퀘어_ac Bold", 15)
        self.font.setBold(True)

        # 각종 라벨 및 슬라이더 선언
        self.timeExplaneLabel = QLabel("- 시간 설정 -")
        self.timeExplaneLabel.setFont(self.font)

        self.timeSlider = QSlider()
        self.timeSlider.setOrientation(Qt.Horizontal)
        self.timeSlider.setTickPosition(QSlider.TicksBelow)
        self.timeSlider.setTickInterval(1)
        self.timeSlider.setMinimum(1)
        self.timeSlider.setMaximum(5)
        self.timeSlider.setValue(int(self.text_list[1]))
        self.timeSlider.valueChanged.connect(self.changedTime)

        self.timeLabel = QLabel()
        self.timeLabel.setText(str((self.timeSlider.value())/2) + "초")
        self.timeLabel.setFont(self.font)

        self.diffiExplaneLabel = QLabel("- 난이도 설정 -")
        self.diffiExplaneLabel.setFont(self.font)

        self.diffiSlider = QSlider()
        self.diffiSlider.setOrientation(Qt.Horizontal)
        self.diffiSlider.setTickPosition(QSlider.TicksBelow)
        self.diffiSlider.setTickInterval(1)
        self.diffiSlider.setMinimum(1)
        self.diffiSlider.setMaximum(5)
        self.diffiSlider.setValue(int(self.text_list[3]))
        self.diffiSlider.valueChanged.connect(self.changedDiffi)
        self.diffiSlider.valueChanged.connect(self.changedDiffi)

        self.diffiLabel = QLabel()
        if self.diffiSlider.value() == 1: diffi = "매우 쉬움"
        elif self.diffiSlider.value() == 2: diffi = "쉬움"
        elif self.diffiSlider.value() == 3: diffi = "보통"
        elif self.diffiSlider.value() == 4: diffi = "어려움"
        else: diffi = "매우 어려움"
        self.diffiLabel.setText(diffi)
        self.diffiLabel.setFont(self.font)

        # 메인 레이아웃
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.timeExplaneLabel)
        self.mainLayout.addWidget(self.timeSlider)
        self.mainLayout.addWidget(self.timeLabel)
        self.mainLayout.addSpacing(50)
        self.mainLayout.addWidget(self.diffiExplaneLabel)
        self.mainLayout.addWidget(self.diffiSlider)
        self.mainLayout.addWidget(self.diffiLabel)

        # 창 기본 설정
        self.setFixedSize(500, 500)
        self.setWindowTitle('설정')
        self.setWindowIcon(QIcon("image/colortable.png"))

        self.setLayout(self.mainLayout)

        self.show()

    def changedTime(self):
        self.timeSliderValue = self.timeSlider.value()
        self.text_list[1] = int(self.text_list[1])
        self.text_list[1] = self.timeSliderValue
        self.text_list[1] = str(self.text_list[1])

        a = open('textFile/setting.txt', 'w', encoding='utf8')
        for p in self.text_list:
            a.write(p + '\n')
        a.close()

        self.timeLabel.setText(str(self.timeSliderValue/2) + "초")

    def changedDiffi(self):
        self.diffiSliderValue = self.diffiSlider.value()
        self.text_list[3] = int(self.text_list[3])
        self.text_list[3] = self.diffiSliderValue
        self.text_list[3] = str(self.text_list[3])

        a = open('textFile/setting.txt', 'w', encoding='utf8')
        for p in self.text_list:
            a.write(p + '\n')
        a.close()

        if self.diffiSlider.value() == 1: diffi = "매우 쉬움"
        elif self.diffiSlider.value() == 2: diffi = "쉬움"
        elif self.diffiSlider.value() == 3: diffi = "보통"
        elif self.diffiSlider.value() == 4: diffi = "어려움"
        else: diffi = "매우 어려움"
        self.diffiLabel.setText(diffi)


class HelpLayout(QDialog):

    def __init__(self, parent):
        super(HelpLayout, self).__init__(parent)

        # 배경 설정
        oImage = QImage("image/gray.jpg")
        sImage = oImage.scaled(1000, 750)
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)

        # 폰트 설정
        QFontDatabase.addApplicationFont("NanumSquare_acB.ttf")

        self.font = [i for i in range(2)]
        fontSizeList = [20, 15]

        for i in range(2):
            self.font[i] = QFont("나눔스퀘어_ac Bold", fontSizeList[i])
            self.font[i].setBold(True)

        # 라벨 선언
        self.helpLabel1 = QLabel("- 게임 설명")
        self.helpLabel1.setFont(self.font[0])
        # self.helpLabel1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.helpLabel1.setAlignment(Qt.AlignTop)

        self.helpText1 = QTextEdit()
        self.helpText1.setText("'무슨 색 이게?' 게임은 주어지는 색을 잠깐 보고 그 색이 무슨 색이었는지 맞추는 게임입니다.")
        self.helpText1.setFont(self.font[1])
        self.helpText1.setFixedHeight(120)
        self.helpText1.setStyleSheet("background-color: rgba(255, 255, 255, 128);")  # border: 2px solid black;
        self.helpText1.setReadOnly(True)

        self.helpLabel2 = QLabel("- 게임 방법")
        self.helpLabel2.setFont(self.font[0])
        # self.helpLabel2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.helpLabel2.setAlignment(Qt.AlignTop)

        self.helptext2 = QTextEdit()
        self.helptext2.setText("""설정 버튼을 통해 게임에 적용될 시간 제한과 난이도를 설정할 수 있습니다. 설정을 마친 후 Start 버튼을 누르게 되면 게임을 시작할 수 있습니다.

게임이 시작되면 각 라운드마다 맞혀야 할 색깔을 확인할 수 있는 버튼이 나타나고, 이용자께서 설정한 시간 제한에 맞게 색이 보여진 후 자동으로 다음 화면으로 넘어갑니다.

그리고는 주어졌던 색을 12개의 색 중에서 찾아서 버튼을 눌러야 하며, 10개의 라운드가 끝나면 총 몇 개를 맞추었는지 확인할 수 있습니다!""")
        self.helptext2.setFont(self.font[1])
        self.helptext2.setStyleSheet("background-color: rgba(255, 255, 255, 128);")
        self.helptext2.setReadOnly(True)

        # 하위 레이아웃
        self.helpLayout1 = QHBoxLayout()
        self.helpLayout1.addSpacing(30)
        self.helpLayout1.addWidget(self.helpText1)
        self.helpLayout1.addSpacing(30)

        self.helpLayout2 = QHBoxLayout()
        self.helpLayout2.addSpacing(30)
        self.helpLayout2.addWidget(self.helptext2)
        self.helpLayout2.addSpacing(30)

        # 메인 레이아웃
        self.mainLayout = QVBoxLayout()
        # self.mainLayout.addWidget(self.titleLabel)
        self.mainLayout.addSpacing(30)
        self.mainLayout.addWidget(self.helpLabel1)
        self.mainLayout.addSpacing(10)
        self.mainLayout.addLayout(self.helpLayout1)
        self.mainLayout.addSpacing(30)
        self.mainLayout.addWidget(self.helpLabel2)
        self.mainLayout.addSpacing(10)
        self.mainLayout.addLayout(self.helpLayout2)
        self.mainLayout.addSpacing(30)

        # 창 기본 설정
        self.setFixedSize(1000, 750)
        self.setWindowTitle('도움말')
        self.setWindowIcon(QIcon("image/colortable.png"))

        self.setLayout(self.mainLayout)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Layout()
    sys.exit(app.exec_())
