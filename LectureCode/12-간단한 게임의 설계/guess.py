class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = []      # 추측에 이용된 글자들
        self.numTries = 0           # 실패한 추측의 횟수
        self.correctLetters = []    # 지금까지 알아낸 글자들
        self.currentStatus = "_" * len(self.secretWord)

    def display(self):
        # print(self.secretWord)  # 삭제예정
        print("Current:", self.currentStatus)
        # print("GuessedChars:", ", ".join(set(self.guessedChars)))  # 삭제예정
        print("Tries:", self.numTries)

    def guess(self, character):
        self.guessedChars.append(character)
        statuslist = list(self.currentStatus)
        letterIndexes = []

        if character in self.secretWord:
            self.correctLetters.append(character)
            for idx, value in enumerate(self.secretWord):
                if value == character:
                    letterIndexes.append(idx)
            for idx in letterIndexes:
                statuslist[idx] = character
        else:
            self.numTries += 1

        self.currentStatus = "".join(statuslist)

        if self.currentStatus == self.secretWord:
            return True
        else:
            return False
