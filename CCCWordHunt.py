wordToFind = input()
numOfRows = int(input())
numOfColumns = int(input())

x = 0
crossword = ""
while x < numOfRows:
    currentLine = input()
    crossword = crossword + currentLine
    x +=1

wordToFindList = list(wordToFind)


crossword = crossword.replace(" ", "")
crosswordLen = len(crossword)
crosswordList = list(crossword)

for i in range(0, crosswordLen):
    if crosswordList[i] == "M":
        if crosswordList[i+numOfColumns] == "E":
            print("One founds")
    

print(crossword)