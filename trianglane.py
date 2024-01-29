#J4 for the CCC 2023 Junior Contest
numOfColumns = int(input())

rowOne = input()
rowTwo = input()

rowOne = rowOne.replace(" ", "")
rowTwo = rowTwo.replace(" ", "")


rowOneList = list(rowOne)
rowTwoList = list(rowTwo)

lenRowOne = len(rowOne)
lenRowTwo = len(rowTwo)

totalNumberOfWet = 0

#Cycle through all in row one
for j in range(0, lenRowOne):
    if rowOneList[j] == "1":
        totalNumberOfWet = totalNumberOfWet + 3
        if j != (lenRowOne-1):
            if rowOneList[j+1] == "1":
                totalNumberOfWet = totalNumberOfWet - 1
        if j != 0:
            if rowOneList[j-1] == "1":
                totalNumberOfWet = totalNumberOfWet - 1

#Cycle through all in row two
for i in range(0, lenRowTwo):
    if rowTwoList[i] == "1":
        totalNumberOfWet = totalNumberOfWet + 3
        if i != (lenRowTwo-1):
            if rowTwoList[i+1] == "1":
                totalNumberOfWet = totalNumberOfWet - 1
        if i != 0:
            if rowTwoList[i-1] == "1":
                totalNumberOfWet = totalNumberOfWet - 1

for k in range(0, numOfColumns, 2):
    if rowOneList[k] == "1" and rowTwoList[k] == "1":
        totalNumberOfWet = totalNumberOfWet-2



print(totalNumberOfWet)


