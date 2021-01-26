#!/usr/bin/env python3

#Rock, Paper and Scissor

import random

def computer_choice():
    comp_ch = random.randint(1,3)
    if comp_ch == 1:
        com = "R"
    elif comp_ch == 2:
        com = "P"
    elif comp_ch == 3:
        com = "S"
    return com            
computer_turn = computer_choice()

def gamePlay(computer,your):
    if computer == your:
        return None
    elif computer == "R":
        if your == "P":
            return True
        elif your == "S":
            return False
    elif computer == "P":
        if your == "S":
            return True
        elif your == "R":
            return False
    elif computer == "S":
        if your == "P":
            return True
        elif your == "R":
            return False


print("Computer chose between Rock,Paper and Scissor!!\n")
user_choice = input("""Now it is your turn to choose......
(R) - Rock
(P) - Paper
(S) - Scissor
Enter the Choice : """)
your_turn = user_choice.upper()

g = gamePlay(computer_turn,your_turn)

print(f"Compter chose {computer_turn} and you chose {your_turn}")

if g == None:
    print("The game tied")
elif g:
    print("You won the game :)")
else:
    print("You have lost the game :/")