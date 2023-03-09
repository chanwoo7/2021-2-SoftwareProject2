from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt5.QtWidgets import QLayout, QGridLayout


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)  # 읽기 전용
        self.display.setAlignment(Qt.AlignRight)  # 숫자가 우측으로 정렬됨
        self.display.setMaxLength(15)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)  # 창의 크기를 변경 불가

        mainLayout.addWidget(self.display, 0, 0, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

