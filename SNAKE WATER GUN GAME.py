#SNAKE WATER GUN

print("There are 10 rounds! Play well and win:) ")

import random

i = 1
score = 0
while i <= 10:
    computer_guess = ["Snake", "Water", "Gun"]
    choice = random.choice(computer_guess)

    print("Enter one of them: S,W,G")

    player_guess = input()
    if player_guess == "S" or player_guess == "W" or player_guess == "G":
        if choice == "Snake" and player_guess == "S":
            print("Match Draw")
        elif choice == "Snake" and player_guess == "W":
            print("You loose")
        elif choice == "Snake" and player_guess == "G":
            print("you win")
            score += 1
        elif choice == "Water" and player_guess == "W":
            print("Match Draw")
        elif choice == "Water" and player_guess == "S":
            print("you win")
            score += 1
        elif choice == "Water" and player_guess == "G":
            print("you loose")
        elif choice == "Gun" and player_guess == "G":
            print("Match Draw")
        elif choice == "Gun" and player_guess == "S":
            print("you loose")
        elif choice == "Gun" and player_guess == "W":
            print("you loose")
        i += 1
    else:
        print("Please Enter correct input ")
print("Your Total Score is :  ", score)
if score >= 5:
    print("Congrats! You won the challange:)")

else:
    print("Nice try dude, play well next time! ")




