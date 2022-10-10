import pickle

dbfilename = 'assignment3.dat'
ass = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()

    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    ASS = open(ass, 'wb')
    pickle.dump(scdb, fH)
    pickle.dump(scdb, ASS)
    fH.close()
    ASS.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        for i in scdb:
            i['Age'] = int(i['Age'])
            i['Score'] = int(i['Score'])
        try:
            if inputstr == "": continue
            parse = inputstr.split(" ")
            if parse[0] == 'add':
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
            elif parse[0] == 'del':
                cnt = 0
                while cnt < len(scdb):
                    if scdb[cnt]['Name'] == parse[1]:
                       scdb.remove(scdb[cnt])
                    else:
                        cnt += 1
            elif parse[0] == 'show':
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            elif parse[0] == 'find':
                find = []
                for f in scdb:
                    if f['Name'] == parse[1]:
                        find.append(f)
                key = 'Name'
                showScoreDB(find, key)
            elif parse[0] == 'inc':
                for i in scdb:
                    if i['Name'] == parse[1]:
                        i['Score'] += int(parse[2])
            elif parse[0] == 'quit':
                break
            else:
                print("Invalid command: " + parse[0])
        except Exception as e:
            print("Invalid command :", e)

def showScoreDB(scdb, keyname):
    for i in scdb:
        i['Age'] = str(i['Age'])
        i['Score'] = str(i['Score'])
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
