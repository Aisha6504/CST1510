'''Addition quiz 
step 1: generate two single digit integers for  number 1(e.g. 4) and number 2 (e.g. 5)
step 2: prompt the use to answer, "what is 4+5?"(user input)
step 3: check if the answer is correct or not'''
import random

while True:
    num1 = random.randint(1,9)
    num2 = random.randint(1,9)
    answer = int(input(f"what is {num1} + {num2}?"))
    if answer ==num1+num2:
        print("Correct!")
        break
    else:
        print("Incorrect.please try again")
