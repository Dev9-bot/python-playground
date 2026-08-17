secret_number= 67
attempts= 0
while True:
    guess= int(input("Guess the secret number"))
    attempts = attempts + 1
    if guess == secret_number:
        print("That's Dang Right!")
        print("You have Guessed the Number in", attempts, "attempts")
        break
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too High! Try again.")
  