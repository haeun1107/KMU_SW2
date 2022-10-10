import random

class Word:

    def __init__(self, filename):
        self.words = []
        self.maxLength = 0
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            self.maxLength = max(len(line)-1, self.maxLength) # 최대 길이 20
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)

    def test(self):
        return 'default'


    def randFromDB(self, minLength):
        minLength = min(minLength, self.maxLength) # minLength가 단어의 최대길이를 벗어났을 경우 maxLength로
        selected = False
        while not selected:
            r = random.randrange(self.count)
            if len(self.words[r]) >= minLength:
                selected = True
        return self.words[r]
