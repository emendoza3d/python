"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment info.
[ ] 2. ATM runs in a "while True" loop to remain awake.
[ ] 3. Main menu uses match-case logic for selections.
[ ] 4. Inputs are validated (e.g., .isdigit()) to prevent crashes (include try except)
[ ] 5. Logic prevents overdrafts and negative deposits.
[ ] 6. All currency is formatted to two decimal places (:.2f).
[ ] 7. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# Structure: Use match-case for the main menu.
# Input Validation: Use .isdigit() or similar logic to prevent crashes if the user types text instead of numbers.
# Use try-except to catch any user entry errors missed by while validation.
# Math Safety: No overdrafts (withdrawing more than you have) and no negative deposits.
# Formatting: All currency must use:.2f.

# balance = 1000.00
# WHILE True loop:
# a. Print Menu (1. Balance, 2. Deposit, 3. Withdraw, 4. Transfer, 5. Exit)
# b. Get user choice
# c. MATCH choice:
# case "1": Print formatted balance
# case "2": Get deposit amt -> Validate it is numeric -> Add to balance
# case "3": Get withdraw amt -> Validate it is numeric -> Check for Overdraft -> Subtract
# case "4": Get transfer amt -> Validate it is numeric -> Check for Overdraft -> Subtract
# case "5": Print goodbye -> Break loop
# case _: Print "Invalid Selection"

balance = 1000.00

choice = 1

try:
    while choice > 0 and choice < 4:
        print(f"1.  Balance")
        print(f"2.  Deposit")
        print(f"3.  Withdraw")
        print(f"4.  Exit")

        choice = int(input("Please enter the number of your selection:  "))

        match choice:
            case 1:
                print(f"{(balance):.2f}")
            case 2:
                # deposit = float(input("Please enter the amount to Deposit:  "))
                deposit = input("Please enter the amount to deposit:  ")
                while not deposit.isdigit():
                    print("You must enter a number (100.00)")
                    deposit = input("Please enter the amount to deposit:  ")
                deposit = float(deposit)

                balance = balance + deposit
                print(f"{balance:.2f}")
                # get amount to deposit from user
                # add deposit to balance
                # print new balance
            case 3:
                withdraw = input("Please enter the amount to withdraw:  ")
                while not withdraw.isdigit():
                    print("You must enter a number (100.00)")
                    withdraw = input("Please enter the amount to withdraw:  ")
                withdraw = float(withdraw)
                if withdraw < balance:
                    balance = balance - withdraw
                else:
                    print("You don't have enough money for that")
                print(f"Your current balance is:  ${balance:.2f}")

            case 4:
                print("Thank you for banking with us ;)")
except ValueError:
    print("data entry error")
except Exception as e:
    print(e)
