class Guess:

    def __init__(self, word):
        self.numTries = 0
        self.secretWord = word
        self.guessedChars = set()
        self.currentStatus = ''

    def display(self):
        blank = '_' * len(self.secretWord)
        for i in range(len(self.secretWord)):
            if self.secretWord[i] in self.currentStatus:
                blank = blank[:i] + self.secretWord[i] + blank[i+1:]
        print("Current: ", blank)
        print("Tries: ", self.numTries)

    def guess(self, character):
        self.guessedChars.add(character)
        if character in self.secretWord:
            self.currentStatus += character * self.secretWord.count(character)
        else:
            self.numTries += 1
        if len(self.secretWord) == len(self.currentStatus):
            print("Current: ", self.secretWord)
            print("Tries: ", self.numTries)
            return True
