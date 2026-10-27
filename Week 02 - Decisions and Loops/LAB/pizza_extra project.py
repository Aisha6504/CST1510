# Python Pizza

bill = 0

size = input("Which size pizza do you want? S, M, or L: ")
pepperoni = input("Do you want pepperoni? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")

# Pizza size
if size.lower() == "s":
    bill = 15
elif size.lower() == "m":
    bill = 20
elif size.lower() == "l":
    bill = 25
else:
    print("Invalid pizza size.")
    exit()

# Pepperoni
if pepperoni.lower() == "y":
    if size.lower() == "s":
        bill += 2
    else:
        bill += 3

# Extra cheese
if cheese.lower() == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")