class Hangman:

    text = [

'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|\

\n Remaining Lives = 0
''',

'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   /
 _|_
|   |______
|          |
|__________|\

\n Remaining Lives = 1
''',

'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |
 _|_
|   |______
|          |
|__________|\

\n Remaining Lives = 2
''',

'''\
   ____
  |    |
  |    o
  |   /|
  |    |
  |
 _|_
|   |______
|          |
|__________|\

\n Remaining Lives = 3
''',

'''\
   ____
  |    |
  |    o
  |    |
  |    |
  |
 _|_
|   |______
|          |
|__________|\

\n Remaining Lives = 4
''',

'''\
   ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|\

\n Remaining Lives = 5
''',

'''\
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
\n
Remaining Lives = 6

''',

    ]


    def __init__(self):
        self.remainingLives = len(self.text) - 1


    def getRemainingLives(self):
        return self.remainingLives


    def decreaseLife(self):
        self.remainingLives -= 1


    def currentShape(self):
        return self.text[self.remainingLives]
