import sys
def readIntoList(fileName):
    with open(fileName,'r') as file:
        text = file.read()
        myList = text.split()
    return myList

def wordDictionary(myList):
    wordDict = dict()
    for word in myList:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1
    sortedItems = sorted(wordDict.items(), key=lambda item: item[-1], reverse=True)
    print(sortedItems)
    return sortedItems


N = sys.argv[1]
myList = readIntoList("C:\\Homework\\Python\\file.txt")
sortedDict = wordDictionary(myList)
print("the most " + N + " repeated words are:")
for i in range(int(N)):
    print("key: " + str(sortedDict[i][0]) + ", repeats " + str(sortedDict[i][1]) + " times")
    














