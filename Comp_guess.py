import random


def computer_guess(x,n):
    feedback1 = ''
    print(f"Choose a number between 1 and {x} and lemme guess it ")
    low = 1
    high = x
    feedback = ""
    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"IS {guess} the number you Selected ?? correct (c), wrong (w) : ").lower()
        if feedback == 'w':
            feedback1=input(f"IS {guess} Lower(L) or Higher(H) : ").lower()
        if feedback1 == 'l':
            low = guess + 1
        elif feedback1 == 'h':
            high = guess - 1
    print(f"YAAYY I FOUND THE NUMBER YOU CHOOSE {n} !!! ITS {guess}")


