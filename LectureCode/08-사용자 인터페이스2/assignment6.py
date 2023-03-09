import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scdb = []
        self.readScoreDB()
        # self.showScoreDB(self.scdb, self.name)

    def initUI(self):
        name = QLabel('Name:')
        age = QLabel('Age:')
        score = QLabel('Score:')
        amount = QLabel('Amount:')
        key = QLabel('Key:')
        result = QLabel('Result:')

        nameEdit = QLineEdit()
        ageEdit = QLineEdit()
        scoreEdit = QLineEdit()
        amountEdit = QLineEdit()

        keyCombo = QComboBox()
        keyCombo.addItem('Name')
        keyCombo.addItem('Age')
        keyCombo.addItem('Score')
        resultText = QTextEdit()

        addButton = QPushButton("Add")
        # addButton.clicked.connect()
        delButton = QPushButton("Del")
        findButton = QPushButton("Find")
        incButton = QPushButton("Inc")
        showButton = QPushButton("Show")

        box1 = QHBoxLayout()
        box1.addWidget(name)
        box1.addWidget(nameEdit)
        box1.addWidget(age)
        box1.addWidget(ageEdit)
        box1.addWidget(score)
        box1.addWidget(scoreEdit)

        box2 = QHBoxLayout()
        box2.addStretch(1)
        box2.addWidget(amount)
        box2.addWidget(amountEdit)
        box2.addWidget(key)
        box2.addWidget(keyCombo)

        box3 = QHBoxLayout()
        box3.addStretch(1)
        box3.addWidget(addButton)
        box3.addWidget(delButton)
        box3.addWidget(findButton)
        box3.addWidget(incButton)
        box3.addWidget(showButton)

        box4 = QHBoxLayout()
        box4.addWidget(result)
        box4.addStretch(1)

        box5 = QHBoxLayout()
        box5.addWidget(resultText)

        verticalBox = QVBoxLayout()
        verticalBox.addLayout(box1)
        verticalBox.addLayout(box2)
        verticalBox.addLayout(box3)
        verticalBox.addLayout(box4)
        verticalBox.addLayout(box5)

        self.setLayout(verticalBox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scdb = []
            return

        try:
            self.scdb = pickle.load(fH)
        except:
            print("Empty DB: ", self.dbfilename)
        else:
            print("Open DB: ", self.dbfilename)
        fH.close()

        for person in self.scdb:
            person['Age'] = int(person['Age'])
            person['Score'] = int(person['Score'])
        return self.scdb

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scdb, fH)
        fH.close()

    def showScoreDB(self, scdb, keyname):
        try:
            for p in sorted(scdb, key=lambda person: person[keyname]):
                for attr in sorted(p):
                    print(str(attr) + "=" + str(p[attr]), end=' ')
                print()
        except KeyError:
            print("Invalid key: " + keyname)

    def addPerson(self, scdb, name, age, score):
        record = {'Name': name, 'Age': age, 'Score': score}
        scdb += [record]

    def delPerson(self, scdb, name):
        for p in scdb:
            if p['Name'] == name:
                scdb.remove(p)

    def findPerson(self, scdb, name):
        for p in scdb:
            if p['Name'] == name:
                print(f"Age={p['Age']}, Name={p['Name']}, Score={p['Score']}")

    def incPerson(self, scdb, name, score):
        for incP in scdb:
            if incP['Name'] == name:
                incP['Score'] += score

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())

