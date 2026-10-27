import random

while True:
    account_a = random.choice(["Instagram", "TikTok", "YouTube", "Facebook"])
    account_b = random.choice(["Snapchat", "X", "LinkedIn", "Pinterest"])

    followers_a = random.randint(100, 1000)
    followers_b = random.randint(100, 1000)

    print(f"\nA: {account_a}")
    print(f"B: {account_b}")

    guess = input("Which has more followers? (A/B or quit): ")

    if guess.lower() == "quit":
        print("Thanks for playing!")
        break

    if followers_a > followers_b:
        correct_answer = "a"
    else:
        correct_answer = "b"

    if guess.lower() == correct_answer:
        print("Correct!")
    else:
        print("Wrong!")

    print(f"{account_a}: {followers_a} followers")
    print(f"{account_b}: {followers_b} followers")