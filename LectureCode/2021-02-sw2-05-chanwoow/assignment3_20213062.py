import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    for person in scdb:
        person['Age'] = int(person['Age'])
        person['Score'] = int(person['Score'])
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                addPerson(scdb, parse[1], parse[2], parse[3])
            except IndexError:
                print("Empty Name or Age or Score")
        elif parse[0] == 'del':
            try:
                delPerson(scdb, parse[1])
            except IndexError:
                print("Empty Name")
        elif parse[0] == 'find':
            try:
                findPerson(scdb, parse[1])
            except IndexError:
                print("Empty Name")
        elif parse[0] == 'inc':
            try:
                incPerson(scdb, parse[1], int(parse[2]))
            except IndexError:
                print("Empty Name or Score")
        elif parse[0] == 'show':
            sortKey ='Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            break
        else:
            print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    try:
        for p in sorted(scdb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                print(str(attr) + "=" + str(p[attr]), end=' ')
            print()
    except KeyError:
        print("Invalid key: " + keyname)


def addPerson(scdb, name, age, score):
    record = {'Name': name, 'Age': age, 'Score': score}
    scdb += [record]


def delPerson(scdb, name):
    for p in scdb:
        if p['Name'] == name:
            scdb.remove(p)

def findPerson(scdb, name):
    for p in scdb:
        if p['Name'] == name:
            print(f"Age={p['Age']}, Name={p['Name']}, Score={p['Score']}")

def incPerson(scdb, name, score):
    for incP in scdb:
        if incP['Name'] == name:
            incP['Score'] += score


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
