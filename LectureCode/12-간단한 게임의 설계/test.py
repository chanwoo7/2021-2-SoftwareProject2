character = "t"
secretWord = "contentment"
guessedChars = []
numTries = 3
correctLetters = []
correctLetterIndexes = []
currentStatus = "_on_en__en_"
statuslist = list(currentStatus)

if character in secretWord:
    guessedChars.append(character)
    correctLetters.append(character)
    for idx, value in enumerate(secretWord):
        if value == character:
            correctLetterIndexes.append(idx)
    for idx in correctLetterIndexes:
        statuslist[idx] = character
else:
    numTries += 1
currentStatus = "".join(statuslist)


print(character)             # t
print(secretWord)            # contentment
print(guessedChars)          # ['t']
print(numTries)              # 3
print(correctLetters)        # ['t']
print(correctLetterIndexes)  # ['0']
print(currentStatus)         # e_____
print(statuslist)            # ['e', '_', '_', '_', '_', '_']

# t
# contentment
# ['t']
# 3
# ['t']
# [3, 6, 10]
# _ontent_ent
# ['_', 'o', 'n', 't', 'e', 'n', 't', '_', 'e', 'n', 't']