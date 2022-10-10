#-*- coding: utf-8 -*-

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QScrollArea, QScrollBar

from hangman import Hangman
from guess import Guess
from word import Word

class HangmanGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Initialize word database
        self.word = Word('words.txt')

        # Hangman display window
        self.hangmanWindow = QTextEdit()
        self.hangmanWindow.setReadOnly(True)
        self.hangmanWindow.setAlignment(Qt.AlignLeft)
        font = self.hangmanWindow.font()
        font.setFamily('Courier New')
        self.hangmanWindow.setFont(font)

        # Layout
        hangmanLayout = QGridLayout()
        hangmanLayout.addWidget(self.hangmanWindow, 0, 0)

        # Status Layout creation
        statusLayout = QGridLayout()

        # Display widget for current status
        self.currentWord = QLineEdit()
        self.currentWord.setReadOnly(True)
        self.currentWord.setAlignment(Qt.AlignCenter)
        font = self.currentWord.font()
        font.setPointSize(font.pointSize() + 8)
        self.currentWord.setFont(font)
        statusLayout.addWidget(self.currentWord, 0, 0, 1, 2)

        # Display widget for already used characters
        self.guessedChars = QLineEdit()
        self.guessedChars.setReadOnly(True)
        self.guessedChars.setAlignment(Qt.AlignLeft)
        self.guessedChars.setMaxLength(52)
        statusLayout.addWidget(self.guessedChars, 1, 0, 1, 2)

        # Display widget for message output
        self.message = QLineEdit()
        self.message.setReadOnly(True)
        self.message.setAlignment(Qt.AlignLeft)
        self.message.setMaxLength(52)
        statusLayout.addWidget(self.message, 2, 0, 1, 2)

        # Input widget for user selected characters
        self.charInput = QLineEdit()
        self.charInput.setMaxLength(1) #입력의 길이가 1
        statusLayout.addWidget(self.charInput, 3, 0)

        # Input widget for minlength

        self.lenInput = QLineEdit()
        statusLayout.addWidget(self.lenInput, 5, 0)

        # Button for submitting a minlength

        self.enterButton = QToolButton()
        self.enterButton.setText('Enter minlength')
        self.enterButton.clicked.connect(self.enterClicked)
        statusLayout.addWidget(self.enterButton, 5, 1)


        # Button for submitting a character
        self.guessButton = QToolButton()
        self.guessButton.setText('Guess!')
        self.guessButton.clicked.connect(self.guessClicked)
        statusLayout.addWidget(self.guessButton, 3, 1)

        # Button for a new game
        self.newGameButton = QToolButton()
        self.newGameButton.setText('New Game')
        self.newGameButton.clicked.connect(self.beforenew)
        statusLayout.addWidget(self.newGameButton, 4, 0)

        # Layout placement
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hangmanLayout, 0, 0)
        mainLayout.addLayout(statusLayout, 0, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle('Hangman Game')

        # Start a new game on application launch!
        #self.startGame()

    def beforenew(self):
        self.hangmanWindow.clear()
        self.currentWord.clear()
        self.guessedChars.clear()
        self.message.clear()
        self.enterButton.setEnabled(True)
        self.guessButton.setEnabled(True)

    def startGame(self):
        self.hangman = Hangman()
        self.guess = Guess(self.secret)
        self.gameOver = False

        self.changeFont()  #단어의 길이에 맞게 폰트 크기를 조정

        self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())   #현재 단어를 나타내는 문자열
        self.currentWord.setText(self.guess.displayCurrent())    #현재 맞춘 단어 상태
        self.guessedChars.setText(self.guess.displayGuessed())   #사용된 문자들
        self.message.clear()

    def changeFont(self):
        self.font = self.currentWord.font()
        if len(self.secret) == 13: self.font.setPointSize(12)
        elif len(self.secret) == 14 or len(self.secret) == 15:
            self.font.setPointSize(10)
        elif 16<=len(self.secret) <= 18: self.font.setPointSize(9)
        elif len(self.secret) == 19: self.font.setPointSize(8)
        elif len(self.secret) == 20: self.font.setPointSize(7)
        else:     #단어의 길이가 12이하인 경우
            self.font.setPointSize(25)
        self.currentWord.setFont(self.font)

    def enterClicked(self):
        minlength = self.lenInput.text() #단어의 최소길이
        self.lenInput.clear()
        self.message.clear()

        if not minlength.isdigit(): # 숫자 입력
            QMessageBox.warning(self, "Error", "Enter number!")
        else:
            self.secret = self.word.randFromDB(int(minlength)) #비밀단어
            if int(minlength) >= self.word.maxLength:
                QMessageBox.warning(self, "Warning", 'out of range! - minlength is 20')
            self.enterButton.setDisabled(True) # enter 버튼 비활성화

            self.startGame()

    def guessClicked(self):
        try:
            guessedChar = self.charInput.text()
            self.charInput.clear()
            self.message.clear()

            if not guessedChar.isalpha():  # 공백문자, 숫자가 입력된 경우
                self.message.setText("Enter alphabet!")
            elif guessedChar in self.guess.guessedChars:  # 이미 사용한 글자인지를 판단하고, 아닌 경우 메시지 출력, 리턴
                self.message.setText('you already guessed "{}"'.format(guessedChar))
            else:
                success = self.guess.guess(guessedChar)
                if success == False: # 비밀단어에 포함되지 않았을 때
                    self.hangman.decreaseLife()  # 남아 있는 목숨을 1만큼 감소
                    self.message.setText('No "{}" in the word'.format(guessedChar))
                else:
                    self.message.setText("a correct word!")
                self.hangmanWindow.setPlaceholderText(self.hangman.currentShape())  # hangmanWindow 에 현재 hangman 상태 그림을 출력
                self.currentWord.setText(self.guess.displayCurrent())  # currentWord 에 현재까지 부분적으로 맞추어진 단어 상태를 출력
                self.guessedChars.setText(self.guess.displayGuessed())  # guessedChars 에 지금까지 이용한 글자들의 집합을 출력

                if self.guess.finished(): # 정답을 맞추었을 때
                    self.message.setText("Success!")
                    self.gameOver = True
                # 메시지 ("Success!") 출력하고, self.gameOver 는 True 로

                elif self.hangman.getRemainingLives() == 0:
                    self.message.setText("Fail! - {}".format(self.secret))
                    self.gameOver = True
                # 메시지 ("Fail!" + 비밀 단어) 출력하고, self.gameOver 는 True 로

            if self.gameOver == True:
                self.guessButton.setDisabled(True)
                # Guess! 버튼 비활성화
        except:
            QMessageBox.warning(self, "Error", "Enter number before you guess!")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = HangmanGame()
    game.show()
    sys.exit(app.exec_())
