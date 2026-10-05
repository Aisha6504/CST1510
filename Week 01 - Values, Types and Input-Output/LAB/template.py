'''
RECORD CHECK  -  my version
===========================

Name  :Aisha
Lane  :  AI 
Date  : 25/9/2026

# Run it:   python template.py

'''
# ==================================================================== INPUT
# 1. Ask the user for your three values.

#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

print("Please enter three values:")
label = input("Enter a label (name, hostname, IP): ")    # : replace with an input() call
first = float(input("Please enter a number"))  # : replace with an input() call, converted
second = float(input("Please enter a number"))   # : replace with an input() call, converted


# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

difference = first - second
percent = (first / second) * 100
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  First value   : {first:>10.2f}")
print(f"  Second value  : {second:>10.2f}")
print(f"  Difference     : {difference:>+10.2f}")
print(f"  Percent        : {percent:>10.2f}%")

print("  Status         : Calculation complete.")
print("=" * 34)


# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

# : your report lines go here


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
# my try 