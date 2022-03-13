import random


def user_guess(x,n):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input("Guess the number : "))
        if guess < random_number:
            print("The number you Guessed is less than the random number i choose ")
        elif guess > random_number:
            print("The number you Guessed is Greater than the random number i choose ")
    print(f"Yayy You Guessed The Right number {n} it's {random_number} , congratulations !!!!  ")


