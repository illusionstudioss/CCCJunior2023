#Problem J3 CCC 2023 Junior

#Get number of people intrested in attending the event
numOfPeopleIntrested = int(input())

totalList = "";

x = 0
while x < numOfPeopleIntrested:

    #See which days the person can come
    person = input()
    totalList = totalList + person
    x +=1


#convert string into a list
scheduleList = list(totalList)
lenTotalList = len(scheduleList)

#Create a loop that runs every 5th element in the array using i
#Create a loop inside that loop that will scan from i to i + 5
#Should let us go through each section sepreatly 

dayOne = 0
dayTwo = 0
dayThree = 0
dayFour = 0
dayFive = 0

for i in range(0, lenTotalList, 5):
    for j in range(i, i + 5, 5):
        #Check which index has Y
        if scheduleList[j] == "Y":
            dayOne +=1
        if scheduleList[j+1] == "Y":
            dayTwo +=1
        if scheduleList[j+2] == "Y":
            dayThree +=1
        if scheduleList[j+3] == "Y":
            dayFour +=1
        if scheduleList[j+4] == "Y":
            dayFive +=1

#Output the days with the most avalibility
highest = max(dayOne, dayTwo, dayThree, dayFour, dayFive)
finalDays = ""

if highest == dayOne: 
    finalDays = finalDays + "1"
if highest == dayTwo:
    finalDays = finalDays + "2"
if highest == dayThree:
    finalDays = finalDays +"3"
if highest == dayFour:
    finalDays = finalDays + "4"
if highest == dayFive:
    finalDays = finalDays + "5"

#Add a commo inbetween if theres multiple days
if len(finalDays) > 1:
    commas = ","
    finalDays = commas.join(finalDays)

print(finalDays)