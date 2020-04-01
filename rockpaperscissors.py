from random import randint

choices = ["Rock","Paper","Scissors"]

computer = choices[randint(0, 2)]

playerPoints = 0
computerPoints = 0

goOn = True

while(goOn):
    #Ask for player input
    player = input("Rock, Paper or Scissors? or enter Finish to end!\n")
    # Check if player wants to stop playing
    if (player == "Finish"):
        goOn = False
    # Check if there is a tie
    elif (player == computer):
        print("Tie!")
    # What happens if the player inputs Rock?
    elif (player == "Rock"):
        if (computer == "Paper"):
            # computer rolls paper and wins the game
            print("You lose!", computer, "covers", player)
            computerPoints += 1
        else:
            # computer rolls scissors and loses the game
            print("You win!", player, "smashes", computer)
            playerPoints += 1
    # What happens if the player inputs Scissors?
    elif (player == "Scissor"):
        if (computer == "Rock"):
            # computer rolls Rock and wins the game
            print("You lose!", computer, "smashes", player)
            computerPoints += 1
        else:
            # computer rolls Paper and loses the game
            print("You win!", player, "cuts", computer)
            playerPoints += 1
    # What happens if the player inputs Paper?
    elif (player == "Paper"):
        if (computer == "Scissors"):
            # computer rolls Scissors and wins the game
            print("You lose!", computer, "cuts", player)
            computerPoints += 1
        else:
            # computer rolls Rock and loses the game
            print("You win!", player, "covers", computer)
            playerPoints += 1
    else:
        print("That is not a valid play. Check your spelling!")

    # Have the computer make another choice
    computer = choices[randint(0, 2)]
    print("********Next Turn*********")

# print out the final points
print("*******Final Points********")
print("Player Points: ", playerPoints)
print("Computer Points: ", computerPoints)
