import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
print(sys.argv)
label = QPushButton("Exit")
label.show()
app.exec_()
