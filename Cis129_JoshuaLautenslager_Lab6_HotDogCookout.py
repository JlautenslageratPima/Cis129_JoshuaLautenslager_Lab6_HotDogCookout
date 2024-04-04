#Cis 129
#Lab 6
#Joshua Lautenslager


import math 

def main():
    #declare local variables
    total = getTotalHotDogs()
    DOGS = 10 # Dogs in a pack
    BUNS = 8 # buns in a pack

    dogsLeft = 0 
    bunsLeft = 0
    minDogs = 0
    minBuns = 0 

    #Declare Functions
    def set_dogsLeft():
        dogsLeft = (DOGS - total % DOGS) % DOGS

    def set_minDogs():
        minDogs = math.ceil(total / DOGS)

    def set_bunsLeft(): 
        bunsLeft = (BUNS - total % BUNS) % BUNS

    def set_minBuns():
        minBuns = math.ceil(total / BUNS) 


    #Main Input Function
    def getTotalHotDogs():
        people = 0   # Number of people attending
        hotDogs = 0  # Hot dogs per person

        people = int(input("Enter the number of people attending the cookout: "))
        hotDogs = int(input("Enter the number of hot dogs for each person: "))

        total = people * hotDogs
        return total
    
    #Results Function
    def showResults(dogsLeft, minDogs, bunsLeft, minBuns):

        print("Minimum packages of hot dogs needed:", minDogs)

        print("Minimum packages of hot dog buns needed:", minBuns)

        print("Hot dogs left over:", dogsLeft)

        print("Hot dog buns left over:", bunsLeft)

main()

