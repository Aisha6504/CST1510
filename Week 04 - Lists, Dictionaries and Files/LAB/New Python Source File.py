"""
1. At the top of your file, write `import random`.
2. Create a list called `letters` containing every letter `a`–`z` and
   `A`–`Z` as separate strings, for example `["a", "b", "c", ...]`.
3. Create a list called `numbers` containing the strings `"0"` to `"9"`.
4. Create a list called `symbols` containing some symbols, for example
   `["!", "#", "$", "%", "&", "(", ")", "*", "+"]`.
5. Use `input()` to ask how many letters the user wants. Convert it with
   `int()` and store it in `nr_letters`.
6. Do the same for symbols, storing the answer in `nr_symbols`.
7. Do the same for numbers, storing the answer in `nr_numbers`.

**Easy version — letters, then symbols, then numbers**

8. Create a variable `password` and set it to an empty string `""`.
9. Write a `for` loop using `range(nr_letters)`. Inside it, add
   `random.choice(letters)` to the end of `password` using `+=`.
10. Write a second `for` loop using `range(nr_symbols)` that does the
    same with `symbols`.
11. Write a third `for` loop using `range(nr_numbers)` that does the
    same with `numbers`.
12. Print `password`."""
import random
import string

letters = list(string.ascii_letters)
numbers = list("0123456789")
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

nr_letters = int(input("How many letters? "))
nr_symbols = int(input("How many symbols? "))
nr_numbers = int(input("How many numbers? "))

password = ""

for i in range(nr_letters):
    password += random.choice(letters)

for i in range(nr_symbols):
    password += random.choice(symbols)

for i in range(nr_numbers):
    password += random.choice(numbers)

print(password)