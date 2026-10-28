name=input("Please Enter a name:")
intrest=input("Please Enter an intrest:")
nationality = input("Please Enter a nationality: (British,American, PAkistani,Indian):")
course = input("Please Enter your course:")
programing_experience = input("please enter your programing experience:")
print(f"User Information\n\tName: {name}\n\tInterest: {intrest}\n\tNationality: {nationality}\n\tCourse: {course}\n\tExperience: {programing_experience}")
# task 2
print("Task 2")
width = 4.5
height = 7.9

area = width * height
perimeter = 2 * (width + height)

print("Area =", area)
print("Perimeter =", format(perimeter, ".2f"))
# task 3
print("Task 3")
employee = input("Enter employee name: ")
hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter hourly rate: "))
federal_tax_rate = float(input("Enter federal tax rate (%): "))
state_tax_rate = float(input("Enter state tax rate (%): "))

gross_pay = hours_worked * hourly_rate
federal_withholding = gross_pay * (federal_tax_rate / 100)
state_withholding = gross_pay * (state_tax_rate / 100)
net_pay = gross_pay - federal_withholding - state_withholding

print("\nEmployee:", employee)
print(f"Gross pay: £{gross_pay:.2f}")
print(f"Federal withholding: £{federal_withholding:.2f}")
print(f"State withholding: £{state_withholding:.2f}")
print(f"Net pay: £{net_pay:.2f}")