def check(userchoice, computerchoice):
    #check options:
    #paper and scissors
    if userchoice == "paper" and computerchoice == "scissors":
        result = "you lose"
    elif userchoice == "scissors" and computerchoice == "paper":
        result = "you win"

    #paper and rock
    elif userchoice == "paper" and computerchoice == "rock":
        result = "you win"

    elif userchoice == "rock" and computerchoice == "paper":
        result = "you lose"

    #paper and paper
    elif userchoice == "paper" and computerchoice == "paper":
        result = "it's a tie"

    #scissors and scissors
    elif userchoice == "scissors" and computerchoice == "scissors":
        result = "it's a tie"
    #scissors and rock
    elif userchoice == "scissors" and computerchoice == "rock":
        result = "you lose"
    elif userchoice == "rock" and computerchoice == "scissors":
        result = "you win"
    #rock and rock
    elif userchoice == "rock" and computerchoice == "rock":
        result = "it's a tie"
    else:
        result = "invalid input"
    return result




#make a list of choices
options = ["rock", "paper", "scissors"]

import random

userscore = 0
computerscore = 0

while userscore <3 and computerscore <3:
    
    #randomly select an item from that list
    computer = random.choice(options)

    #ask user for their choice
    user = input("Please enter rock, paper or scissors ")
    print("Computer chose", computer)

    oneround = check(user, computer)
    if oneround == "you win":
        userscore +=1
    elif oneround == "you lose":
        computerscore +=1
    print(oneround)
    print(userscore, ":", computerscore)




    
#output the result
if userscore ==3:
    print("User won")

else:
    print("Computer won")
