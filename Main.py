import user_guess
import Comp_guess

player = input("Enter the players name : ")
mode = int(input(" Select a game mode\n-------------------- \n1.User Guessing number \n2.Computer guessing number : "))
limit = int(input("Enter the Max Limit of the numbers : "))

if mode == 1:
    user_guess.user_guess(limit, player)
elif mode == 2:
    Comp_guess.computer_guess(limit, player)

while True:
    again = input("Wanna play again ? (Y)/(N) : ").lower()
    if again == 'y':
        mode = int(input("Select mode\n--------------------\n 1.User Guessing number \n2.Computer guessing number : "))
        limit = int(input("Enter the Max Limit of the numbers : "))

        if mode == 1:
            user_guess.user_guess(limit, player)
        elif mode == 2:
            Comp_guess.computer_guess(limit, player)
    else:
        print(f"Thanks for playing {player}!! Have a nice day !!")
        exit(0)
