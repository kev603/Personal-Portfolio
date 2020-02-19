#rock, plastic, dragon game program
#in this program the user will play against the computer where the pc will generate a random choice
#rules are:
#rock beats dragon
#dragon burns plastic
#plastic wraps rock
#if both players have the same choice, players will have to choose again

#welcome string
print("\t <---Welcome to Rock, Plastic, Dragon Game--->")

def RPDSuarez():
    choiceA = user()  #user's choice
    choiceB  = computer()  #computer's choice
    whoWon(choiceA, choiceB)    #determines who won by taking the choices from both
    


def exitProg():
    # this are the choices the user has at the end of the game to either keep playing or leave the game
    print("1. Continue Playing")
    print("2. Exit Game")
    choice = eval(input("Enter your choice: ")) #the user types the selected choice, either 1 or 2
    while choice != 1 and choice != 2:
        print("invalid input")
        choice = eval(input("Enter your choice: "))
    
    if choice == 1:
        RPDSuarez()
    elif choice == 2:
        print("Exiting...Byeee!!!")
     

#user function call, it gets the input of the user so that it can then be
#compared with the comouter's choice
def user():
    print("Pick between Rock, Plastic, or Dragon")  #the user's list of choices
    userChoice = input("Please type your choice: ")   #the user then enters their choice
    #the user's choice cannot be other than the ones shown
    while userChoice not in ["Rock", "rock", "Plastic", "plastic", "Dragon", "dragon"]:
        print("Ivalid Input. Try Again")
        print("Pick between Rock, Plastic, or Dragon")
        userChoice = input("Please type your choice: ")
    choiceA = 0 #user's choice interpreted as a general number so that it can be compared with the computer's choice
    if userChoice == "Dragon" or userChoice == "dragon":
        choiceA = 1
        print("You picked Dragon")
    elif userChoice == "Rock" or userChoice == "rock":
        choiceA = 2
        print("You picked Rock")
    elif userChoice == "Plastic" or userChoice == "plastic":
        choiceA = 3
        print("You picked Plastic")
    return choiceA  #this function call returns the user's general choice as a number,
                    #which is then used for comparisson

    #compuyter's choice
    #10 = dragon
    #20 = rock
    #30 = plastic
#this is the computer function call, which generates a random choice from
#from the computer so that then it can be compared with the user's input
def computer():
    import random
    pcChoices = [10,20,30]  #computer's list of choices
    randomSelect = random.choice(pcChoices)
    choiceB = 0 #computer's choice interpreted as a general number so it can be compared with the user's choice
    if randomSelect == 10:
        choiceB = 1
        print("The CPU chosed Dragon") #prints out the choice
    elif randomSelect == 20:
        choiceB = 2
        print("The CPU chosed Rock")
    elif randomSelect == 30:
        choiceB = 3
        print("The CPU chosed Plastic")
    return choiceB

#1 beats 3
#2 beats 1
#3 beats 2
#a = choiceA aka the user
#b = choiceB aka the computer
#this function call is the one that compares the user's input and the
#computer randomly generated choice, and then determines which one is the
#winner
def whoWon(a,b):
# if choiceA and ChoiceB are equal to each other, that means there is a tie
#and tie == True
    if a == b:
        print("\t Tts a Tie")
        RPDSuarez()  #it goes back to the user and the computer function call to redo the process
        return             #of getting a different choice each   
    if a == 1 and b == 2:   
        print("\t You Lost")
    elif a == 1 and b == 3:
        print("\t You Won")
    elif a == 2 and b == 1:
        print("\t You Won")
    elif a == 2 and b == 3:
        print("\t You Lost")
    elif a == 3 and b == 1:
        print("\t You Lost")
    elif a == 3 and b == 2:
        print("\t You Won")

    exitProg()  #give the user the option to either keep playing or exit game



RPDSuarez()
