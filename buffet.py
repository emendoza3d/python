"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: [Insert Date]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask the user for their age (convert to int) and the day of the week (convert to string).
2. Calculate the base price using if/elif/else:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)(make a variable, change to .5 if it is Tuesday)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Use a match/case statement to handle special daily rules based on the day entered:
   - Tuesday: Children through age 12 are half price! (changes price calculation)
   - Sunday: Drinks are free! (print statement no change in price)
   - Other days: Standard buffet pricing in effect.
4. Print the final price formatted as currency and display any applicable daily special notices.
-----------------------------------------------------------------------
"""

"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: [Insert Date]
FILE: buffet.py
-----------------------------------------------------------------------
"""

# TODO 1: Ask the user for the day of the week.

day_of_week = input("What day is it?:  ").lower()
# TODO 2: Use .lower() with the day input.

# day_of_week = day_of_week.lower()


# TODO 3: Use match/case to set child_price_per_year.

match day_of_week:
    case "tuesday":
        print("Kids are Half off")
        child_price = 0.5
    # Tuesday: $0.50 per year.
    case "sunday":
        print("drinks are free")
        child_price = 1
    case _:
        child_price = 1
# Sunday: $1.00 per year and print the free-drinks notice.
# Every other day: $1.00 per year using the default case (case _).

# TODO 4: Ask the user for their age and convert it to an integer.
age = int(input("How old are you?  "))
if age < 1:
    print("0.00")

elif age <= 12:
    print(f"{age * child_price}")

elif age <= 65:
    print("$16.95")

elif age > 65:
    print("$12.95")

# TODO 5: Use if/elif/else to calculate the price.
# Under 1: FREE ($0.00)
# Ages 1 to 12: age multiplied by child_price_per_year
# Ages 13 to 64: $16.95
# Age 65 and older: $12.95

# TODO 6: Print the final price formatted as currency.
