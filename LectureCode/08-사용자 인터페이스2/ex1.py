import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(550, 550)
    w.move(500, 300)
    w.setWindowTitle('Simple1')
    w.show()

    sys.exit(app.exec_())