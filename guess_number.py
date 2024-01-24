import random

low_number = 1
highest_number = 10
guesses = 0

number = random.randint(1, highest_number)

name = input("What is your name?: ")
guess = 0

print(f"Please guess a number between {low_number} and {highest_number}")
guesses += 1

while guess != number:
    guess = int(input())

    if guess == number:
        print("You guessed it!")
        break
    else:
        if guess < number:
            print("Please guess higher")
        else:
            print("Please guess lower")
    guesses += 1

print(f"Well done {name}, it took you {guesses} guesses")







