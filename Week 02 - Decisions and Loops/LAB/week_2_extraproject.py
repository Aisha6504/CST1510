size = input("What size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if pepperoni == "Y":
    if size == "S":
        bill = bill + 2
    else:
        bill = bill + 3

if cheese == "Y":
    bill = bill + 1

print(f"Your final bill is: ${bill}.")
# 2nd question

print("Welcome to Treasure Island!")

choice1 = input("Left or right? ")

if choice1 == "left":
    choice2 = input("Swim or wait? ")

    if choice2 == "wait":
        choice3 = input("Red, blue, or yellow door? ")

        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("Burned by fire. Game over.")
        else:
            print("Eaten by beasts. Game over.")
    else:
        print("Attacked by a shark. Game over.")
else:
    print("You fell into a hole. Game over.")
   # question no 3
   account_a = "Cats"
followers_a = 5000

account_b = "Dogs"
followers_b = 8000

while True:
    print("A:", account_a)
    print("B:", account_b)

    guess = input("Which has more followers? A, B, or quit: ")

    if guess == "quit":
        break

    if followers_a > followers_b:
        correct = "A"
    else:
        correct = "B"

    if guess == correct:
        print("Correct")
    else:
        print("Wrong")
# project 3
account_a = "Cats"
followers_a = 5000

account_b = "Dogs"
followers_b = 8000

while True:
    print("A:", account_a)
    print("B:", account_b)

    guess = input("Which has more followers? A, B, or quit: ")

    if guess == "quit":
        break

    if followers_a > followers_b:
        correct = "A"
    else:
        correct = "B"

    if guess == correct:
        print("Correct")
    else:
        print("Wrong")
# project 4
secret = 42
guesses = 0

while True:
    guess = int(input("Guess the number: "))
    guesses = guesses + 1

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        print("Correct!")
        print("It took you", guesses, "guesses.")
        break