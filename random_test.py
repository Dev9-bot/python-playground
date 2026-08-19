import random

secret_number = 67
attempts = 0

while True:
    guess = int(input("Guess the secret number between 1 and 100: "))
    attempts += 1

    if guess < secret_number:
        print("Too Low! Try again.")

    elif guess > secret_number:
        print("Too High! Try again.")

    else:
        if attempts == 1:
            print("Holy cow! You guessed it on the first try!")

        print("Congratulations! You guessed the secret number:", secret_number)
        print("Number of attempts:", attempts)
        break
