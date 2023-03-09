import random

class Word:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)

    def randFromDB(self, minLength):
        selected = False
        self.minLength = minLength
        self.word = ""

        if self.minLength > len(max(self.words, key=len)):
            self.minLength = len(max(self.words, key=len))

        while not selected:
            r = random.randrange(self.count)
            if len(self.words[r]) >= self.minLength:
                selected = True
                self.word = self.words[r]

        return self.word
