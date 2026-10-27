#Tip calculator
# 2nd
bill = float(input("Enter the total bill: "))
people = int(input("How many people are splitting it? "))
tip_percent = float(input("Enter the tip percentage (e.g. 12 for 12%): "))

tip_multiplier = 1 + (tip_percent / 100)

each_person = (bill / people) * tip_multiplier

print(f"\nEach person should pay: {each_person:.2f}")