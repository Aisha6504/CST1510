""" Create a variable `password_list` and set it to an empty list `[]`.
14. Repeat steps 9–11, but this time use `.append()` to add each random
    character to `password_list` instead of adding it to a string.
15. Call `random.shuffle(password_list)` to mix up the order.
    (Note: `shuffle()` changes the list in place and returns `None`, so
    don't write `password_list = random.shuffle(password_list)`.)
16. Create a variable `password` and set it to `""`.
17. Write a `for char in password_list:` loop that adds each `char` to
    `password`.
18. Print `password`. Run it a few times with the same inputs and check
    the order changes each time.

**Extension:** replace steps 16–17 with one line:
`password = "".join(password_list)`."""
import random
import string

letters = list(string.ascii_letters)
numbers = list("0123456789")
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

nr_letters = int(input("How many letters would you like? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

password_list = []

# Add random letters
for _ in range(nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Add random numbers
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the list
random.shuffle(password_list)

# Convert list into a string
password = "".join(password_list)

print(f"Your password is: {password}")