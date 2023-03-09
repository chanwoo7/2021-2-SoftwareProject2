character = "t"
secretWord = "contentment"
currentStatus = "_on_en__en_"
correctLetterIndexes = []
statuslist = list(currentStatus)


for idx, value in enumerate(secretWord):
    if value == character:
        correctLetterIndexes.append(idx)
        print(idx, value)
for idx in correctLetterIndexes:
    statuslist[idx] = character

print("=====")
print(character)             # t
print(secretWord)            # contentment
print(correctLetterIndexes)  # ['0']
print(currentStatus)         # e_____
print(statuslist)            # ['e', '_', '_', '_', '_', '_']