#Problem J2 CCC 2023 Junior

#Number of peppers added
numOfPeppers = int(input())

x = 0
pepperList = ""
totalSpice = 0 #Amount of spicyness

while x < numOfPeppers:
    pepperName = input()

    if pepperName == "Poblano":
        totalSpice = totalSpice + 1500

    elif pepperName == "Mirasol":
        totalSpice = totalSpice + 6000

    elif pepperName == "Serrano":
        totalSpice = totalSpice + 15500

    elif pepperName == "Cayenne":
        totalSpice = totalSpice + 40000

    elif pepperName == "Thai":
        totalSpice = totalSpice + 75000

    elif pepperName == "Habanero":
        totalSpice = totalSpice + 125000

    x += 1  


print(totalSpice)



    
