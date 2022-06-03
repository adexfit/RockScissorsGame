import random

options = ["R", "S", "P"]

def interpret(a):
    if a == "R":
        return "Rock"
    elif a == "P":
        return "Paper"
    elif a == "S":
        return "Scissors"

def newgame():
    computer_choice = []

    print("Player's turn")
    print("Type 'R' for rock, 'P' for paper and 'S' for scissors:")
    your_choice = input("your choice:")
    while your_choice not in options:
        print("wrong selection")
        print("Type 'R' for rock, 'P' for paper and 'S' for scissors:")
        your_choice = input("your choice:")

    print("")    
    print("CPU's turn")
    computer_choice.append(random.choice(options))
    print('CPU has made a choice')
    print("Result")
    print("Player ({}) : CPU ({})".format(interpret(your_choice), interpret(computer_choice[-1])))

    if computer_choice[-1] == your_choice:
        print("No winner, we are starting again !")
        print("")
        newgame()
        

    if computer_choice[-1] == "P" and your_choice == "S":
        print("You are the winner !")
    elif your_choice == "P" and computer_choice[-1] == "S": 
        print("CPU is the winner !")
    elif computer_choice[-1] == "R" and your_choice == "P":
        print("You are the winner !")
    elif your_choice == "R" and computer_choice[-1] == "P": 
        print("CPU is the winner !")
    elif computer_choice[-1] == "R" and your_choice == "S":
        print("CPU is the winner !")
    elif your_choice == "R" and computer_choice[-1] == "S": 
        print("You are the winner !")

 
newgame()
    