# 레이아웃 예제
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QTextEdit, QGridLayout, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        reviewEdit = QTextEdit()

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 0, 0)
        grid.addWidget(titleEdit, 0, 1)

        grid.addWidget(author, 1, 0)
        grid.addWidget(authorEdit, 1, 1)

        grid.addWidget(review, 2, 0)
        grid.addWidget(reviewEdit, 2, 1, 5, 1)

        self.setLayout(grid)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

