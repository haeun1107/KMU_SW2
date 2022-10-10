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
        scoredb = self.readScoreDB()
        self.writeScoreDB()
        self.change_int(scoredb)
        self.add_click(scoredb)
        self.del_click(scoredb)
        self.find_click(scoredb)
        self.inc_click(scoredb)
        self.show_click(scoredb)
        self.showScoreDB(scoredb)

    def initUI(self):
        self.name = QLabel('Name :', self)
        self.input_name = QLineEdit(self)
        self.input_name.move(45, 0)
        self.age = QLabel('Age :', self)
        self.age.move(170, 0)
        self.input_age = QLineEdit(self)
        self.input_age.move(205, 0)
        self.score = QLabel('Score :', self)
        self.score.move(330, 0)
        self.input_score = QLineEdit(self)
        self.input_score.move(375, 0)
        self.amount = QLabel('Amount :', self)
        self.amount.move(200, 33)
        self.input_amount = QLineEdit(self)
        self.input_amount.move(255, 30)
        self.key = QLabel('Key :', self)
        self.key.move(370, 33)
        self.result = QLabel('Result :', self)
        self.result.move(0, 85)
        self.input_result = QTextEdit(self)
        self.input_result.resize(495, 135)
        self.input_result.move(0, 110)

        self.keycombobox = QComboBox(self)
        self.keycombobox.addItem("Name")
        self.keycombobox.addItem("Age")
        self.keycombobox.addItem("Score")
        self.keycombobox.move(400, 33)

        self.addbutton = QPushButton("Add")
        self.delbutton = QPushButton("Del")
        self.findbutton = QPushButton("Find")
        self.incbutton = QPushButton("Inc")
        self.showbutton = QPushButton("show")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.addbutton)
        hbox.addWidget(self.delbutton)
        hbox.addWidget(self.findbutton)
        hbox.addWidget(self.incbutton)
        hbox.addWidget(self.showbutton)

        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addLayout(hbox)
        vbox.addStretch(5)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            print("New DB: ", self.dbfilename)
            return []

        self.scdb = []

        try:
            self.scdb = pickle.load(fH)
        except:
            print("Empty DB: ", self.dbfilename)
        else:
            print("Open DB: ", self.dbfilename)
        fH.close()

        return self.scdb

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scdb, fH)
        fH.close()

    def change_int(self, scdb):
        for i in scdb:
            i['Age'] = int(i['Age'])
            i['Score'] = int(i['Score'])

    def add_click(self, scdb):
        self.addbutton.clicked.connect(lambda: self.addScoreDB(scdb))

    def del_click(self, scdb):
        self.delbutton.clicked.connect(lambda: self.delScoreDB(scdb))

    def find_click(self, scdb):
        self.findbutton.clicked.connect(lambda: self.findScoreDB(scdb))

    def inc_click(self, scdb):
        self.incbutton.clicked.connect(lambda: self.incScoreDB(scdb))

    def show_click(self, scdb):
        self.showbutton.clicked.connect(lambda: self.showScoreDB(scdb))

    def addScoreDB(self, scdb):
        record = {'Name': self.input_name.text(), 'Age': self.input_age.text(), 'Score': self.input_score.text()}
        scdb += [record]
        self.showScoreDB(scdb)

    def delScoreDB(self, scdb):
        cnt = 0
        while cnt < len(scdb):
            if (self.input_name.text() == scdb[cnt]['Name']):
                scdb.remove(scdb[cnt])
            else:
                cnt += 1
        self.showScoreDB(scdb)

    def findScoreDB(self, scdb):
        text = ""
        for f in scdb:
            if f['Name'] == self.input_name.text():
                for attr in sorted(f):
                    text += f'{attr} = {f[attr]} \t'
                text += '\n'
        self.input_result.setText(text)

    def incScoreDB(self, scdb):
        for i in scdb:
            if i['Name'] == self.input_name.text():
                i['Score'] += int(self.input_amount.text())
        self.showScoreDB(scdb)

    def showScoreDB(self, scdb):
        self.input_result.clear()
        for i in scdb:
            i['Age'] = str(i['Age'])
            i['Score'] = str(i['Score'])
        text = ""
        for i in sorted(scdb, key=lambda person: person[self.keycombobox.currentText()]):
            for attr in sorted(i):
                text += f'{attr} = {i[attr]} \t'
            text += '\n'
            self.input_result.setText(text)
        self.change_int(scdb)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
