## Task 1: Password Strength Checker
password = input("Enter a password: ")

if len(password) < 8:
    print("Weak")
elif len(password) < 12:
    print("Moderate")
else:
    print("Strong")

## Task 2: Multiplication Quiz

from random import randint

number1 = randint(0, 9)
number2 = randint(0, 9)

answer = int(input(f"What is {number1} * {number2}? "))

if answer == number1 * number2:
    print("True")
else:
    print("False")

## Task 3: Sum of Numbers from 1 to n
n = int(input("Enter the value n: "))

total = 0

for i in range(1, n + 1):
    total += i

print(f"The sum of all numbers until {n} is {total}")