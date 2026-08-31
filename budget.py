"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

# get info from user

gross_income = float(input("What is your gors monthly income? "))
housing = float(input("What do you spend on our rent or mortgage? "))
phone = float(input("What do you spend on your phone each month? "))
food = float(input("What do you spend on food each month? "))
car = float(input("What do you spend of your car each month? "))
electricity = float(input("What do you spend on electricity? "))

fed_tax = gross_income * 0.20
net_income = gross_income - fed_tax

total_expenses = housing + phone + food + car + electricity

remaining = net_income - total_expenses

print(f"you spent {total_expenses:,.2f}")
print(f"that was {total_expenses/net_income:,.2%} of your net income")
