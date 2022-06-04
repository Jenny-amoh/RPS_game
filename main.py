import random

options = ["R","P","S"]

play = "yes"
while play == "yes" :
    input = str(raw_input("Pick an option between R, P and S: "))
    compOption = random.choice(options)

    while (input not in options or input == compOption):
        if input == compOption:
            compOption = random.choice(options)
            print("Its a tie , try again\n")
            input = raw_input("Pick an option between R, P and S: ")
        else:
            input = raw_input("Invalid option \n Pick an option between R, P and S: ")

    print("Computer Option : ", compOption)
    if input == "R" and compOption == "S":
        print("You win , Rock beats Scissors")
    elif input == "P" and compOption == "R":
        print("You win , Paper beats Rock\n")
    elif input == "S" and compOption == "P":
        print("You win , Scissors beats Paper\n")
    else:
        print("You lose\n")

    play = str(raw_input("Type yes to play again : "))