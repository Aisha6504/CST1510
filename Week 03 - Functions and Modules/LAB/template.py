"""
RECORD CHECK  -  my version
===========================

Name  : Aisha Ahmed
Lane  :  AI 
Date  : 09/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).
#
#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.
#
#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.
#
#    Give each function a one-line docstring saying what it does.

# your function(s) go here
def status_of(percent):
    """Return a status based on the percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and percentage."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report."""
    print(label)
    print(f"Value: {value}")
    print(f"Limit: {limit}")
    print(f"Difference: {difference}")
    print(f"Percent: {percent:.1f}%")
    print(f"Status: {status}")


difference, percent = check(87, 100)
status = status_of(percent)
print_report("Test 1", 87, 100, difference, percent, status)

# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
label = input("Enter label: ")
value = float(input("Enter value: "))
limit = float(input("Enter limit: "))
def status_of(percent):
    """Return a status based on percentage."""
    if percent >= 100:
        return "OVER LIMIT"
    elif percent >= 90:
        return "WARNING"
    else:
        return "OK"


def check(value, limit):
    """Return the difference and percentage."""
    difference = value - limit
    percent = (value / limit) * 100
    return difference, percent


def print_report(label, value, limit, difference, percent, status):
    """Print a formatted report."""
    print()
    print("Report")
    print("=" * 30)
    print("Label:", label)
    print("Value:", value)
    print("Limit:", limit)
    print("Difference:", difference)
    print("Percent:", round(percent, 2))
    print("Status:", status)
# Processing
difference, percent = check(value, limit)
status = status_of(percent)

# Output
print_report(label, value, limit, difference, percent, status)
# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.

difference =  value - limit  # replace with your code
percent = (value / limit) * 100  # replace with your code
status =  status_of(percent)     # replace with your code


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

def print_report(label, value, limit, difference, percent, status):
    """Print a record report."""

    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {label}")
    print("=" * 34)

    print(f"Value      : {value}")
    print(f"Limit      : {limit}")
    print(f"Difference : {difference}")
    print(f"Percent    : {percent:.2f}%")
    print(f"Status     : {status}")

    print("=" * 34)
    over_limit_count = 0

while True:
    label = input("Enter label (or quit): ")

    if label.lower() == "quit":
        break

    value = float(input("Enter value: "))
    limit = float(input("Enter limit: "))

    difference, percent = check(value, limit)
    status = status_of(percent)

    if status == "OVER LIMIT":
        over_limit_count += 1

    print_report(
        label,
        value,
        limit,
        difference,
        percent,
        status
    )

print(f"\nOVER LIMIT records: {over_limit_count}")

# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
