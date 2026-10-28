## Task 1: Dice Throws
'''Create a list of seven dice throws.
- The throws should be randomly generated and added to the list.
- Shuffle the list and print it out.
- Sort the list in descending order and print it out.
- Count the occurrences and print them out.'''
## Task 1: Dice Throws


from random import randint, shuffle

# Create a list of 7 dice throws
throws = []

for i in range(7):
    throws.append(randint(1, 6))

print("Original list:", throws)

# Shuffle the list
shuffle(throws)
print("Shuffled list:", throws)

# Sort in descending order
throws.sort(reverse=True)
print("Sorted descending:", throws)

# Count occurrences
for number in range(1, 7):
    count = throws.count(number)
    print(f"{number}: {count}")
#task 2 
print("task 2")
from random import sample

# Generate 6 unique numbers between 1 and 49
ticket = sample(range(1, 50), 6)

# Sort in ascending order
ticket.sort()

print("Lottery ticket numbers:", ticket)