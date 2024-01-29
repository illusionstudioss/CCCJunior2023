#Problem J1 for Junior 2023 contest

#Get input
P = int(input())
C = int(input())

totalPoints = (P*50) #50 points for each package delivered
totalPoints = totalPoints - (10*C)

#Check if bonus applies
if P > C:
    totalPoints = totalPoints + 500


print(totalPoints)
