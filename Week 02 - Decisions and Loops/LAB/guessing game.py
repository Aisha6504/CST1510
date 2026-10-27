import random

secret_number = random.randint(1, 100)
guesses = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = input("Guess the number (or type quit): ")

    if guess.lower() == "quit":
        print(f"The secret number was {secret_number}.")
        print("Game ended.")
        break

    guess = int(guess)
    guesses += 1

    if guess > secret_number:
        print("Too high!")
    elif guess < secret_number:
        print("Too low!")
    else:
        print(f"Congratulations! You guessed the number in {guesses} attempts.")
        break