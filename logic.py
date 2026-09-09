"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment title.
[ ] 2. Ask user for two integers (num1 and num2).
[ ] 3. Perform 6 logical checks: (Both > 0, Both > 100, Either Even, Either < 100, Not Equal, Not Zero).
[ ] 4. Use if/elif/else to categorize num1 (Positive/Negative/Zero).
[ ] 5. Code is clean and uses descriptive variable names.
[ ] 6. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

print("Please enter a digit for num1")
num1 = int(input("number 1:  "))
print("Please enter a digit for num2")
num2 = int(input("number 2:  "))


if num1 > 0 & num2 > 0:
    print("They are both greater than 0")

if num1 < 100 & num2 < 100:
    print("then both are less than 100")

if num1 % 2 == 0 & num2 % 2 == 0:
    print("both numbers are even")

if num1 == num2:
    print("Equal to each other")

if num1 > 0:
    print("num1 is positive")

elif num1 < 0:
    print("num1 is negative")

else:
    print("num1 is 0")
