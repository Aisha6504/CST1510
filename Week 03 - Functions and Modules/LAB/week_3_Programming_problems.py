## Task 1: Quiz
from random import randint


def addition():
    n1 = randint(0, 9)
    n2 = randint(0, 9)

    answer = int(input(f"What is {n1} + {n2}? "))
    return answer == n1 + n2


def subtraction():
    n1 = randint(0, 9)
    n2 = randint(0, 9)

    answer = int(input(f"What is {n1} - {n2}? "))
    return answer == n1 - n2


def multiplication():
    n1 = randint(0, 9)
    n2 = randint(0, 9)

    answer = int(input(f"What is {n1} * {n2}? "))
    return answer == n1 * n2


def division():
    n1 = randint(0, 9)
    n2 = randint(0, 9)

    if n2 == 0:
        print("Error: Cannot divide by zero.")
        return False

    answer = float(input(f"What is {n1} / {n2}? "))
    return round(answer, 2) == round(n1 / n2, 2)


def exponent():
    n1 = randint(0, 9)
    n2 = randint(0, 3)

    answer = int(input(f"What is {n1} ** {n2}? "))
    return answer == n1 ** n2


def remainder():
    n1 = randint(0, 9)
    n2 = randint(1, 9)

    answer = int(input(f"What is {n1} % {n2}? "))
    return answer == n1 % n2


score = 0

while True:
    print("\n----- Math Practice -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponent")
    print("6. Remainder")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        correct = addition()
    elif choice == "2":
        correct = subtraction()
    elif choice == "3":
        correct = multiplication()
    elif choice == "4":
        correct = division()
    elif choice == "5":
        correct = exponent()
    elif choice == "6":
        correct = remainder()
    elif choice == "7":
        print("Final score:", score)
        break
    else:
        print("Invalid choice.")
        continue

    if correct:
        print("Correct!")
        score += 1
    else:
        print("Incorrect.")

    print("Score:", score)

    again = input("Practice again? (y/n): ")
    if again.lower() != "y":
        print("Final score:", score)
        break
## Task 2: Pentagon Area
#Ask for the side length `s` and compute the area: `area = 5*s**2 / (4*tan(pi/5))`. Print to 2 d.p.

#**Example Output:**
```
#Area = 172.05
```
#*Optional hint:* `from math import tan, pi`


from math import tan, pi

s = float(input("Enter the side length: "))

area = (5 * s**2) / (4 * tan(pi / 5))

print(f"Area = {area:.2f}") 