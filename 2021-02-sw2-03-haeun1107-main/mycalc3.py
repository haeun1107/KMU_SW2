from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]

        for i in range(len(self.digitButton)):
            self.digitButton[i] = Button(str(i), self.buttonCliked)

        # . and = Buttons
        self.decButton = Button('.', self.buttonCliked)
        self.eqButton = Button('=', self.buttonCliked)

        # Operator Buttons
        self.mulButton = Button('*', self.buttonCliked)
        self.divButton = Button('/', self.buttonCliked)
        self.addButton = Button('+', self.buttonCliked)
        self.subButton = Button('-', self.buttonCliked)

        # Parentheses Buttons
        self.lparButton = Button('(', self.buttonCliked)
        self.rparButton = Button(')', self.buttonCliked)

        # Clear Button
        self.clearButton = Button('C', self.buttonCliked)

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        numLayout.addWidget(self.digitButton[0], 3, 0)
        for i in range(1, 10):
            row = int((9-i) / 3)
            col = int((i+2) % 3)
            numLayout.addWidget(self.digitButton[i], row, col)

        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)

        opLayout.addWidget(self.clearButton, 3, 0)

        mainLayout.addLayout(opLayout, 1, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

    def buttonCliked(self):
        try:
            button = self.sender()
            key = button.text()
            if key == '=':
                result = str(eval(self.display.text()))
                self.display.setText(result)
            elif key == 'C':
                self.display.setText('')
            else:
                self.display.setText(self.display.text() + key)
        except SyntaxError:
            self.display.setText('잘못된 수식입니다.')
        except ZeroDivisionError:
            self.display.setText('0으로 나눌 수 없습니다.')

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()

    sys.exit(app.exec_())
