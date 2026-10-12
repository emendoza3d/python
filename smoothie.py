"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")
SIZES = ("small", "medium", "large")

def main():
    print("Welcome to Quacken Smoothie Hut")
    
    choice_size = input("Size (Small/Medium/Large): ").title().strip()
    choice_milk = input("Select BASES: ")
    choice_fruit = input("Select FRUITS: ")


# TODO: Define get_price(size)
def get_price(SIZES):
    match SIZES:
        case "small":
            return 3.00
        case "medium":
            return 4.00
        case "large":
            return 5.00
        case _:
            print("Sorry, that is not a valid size. Please choose small, medium, or large.")
            return 0

# TODO: Define blend(size, base, fruit, price)
def blend (size, base, fruit, price):
    print("You selected")
    print(size)
    print(base)
    print(fruit)
    print(f"$ {price:.2f}")



# TODO: Define main() to collect input and call your logic
def main():
    try:
        size = input("What size smoothie do you want (small, medium, large): ")
        price = get_price(size)
        for fruit in FRUITS:
            print(fruit)
        my_fruit = input("Which fruit would you like?  ")
        for base in BASES:
            print(base)
        my_base = input("Which base would yo like?  ")
    except ValueError:
        print("data entry error")
    except Exception as e:
        print(e)
    blend (size, my_base, my_fruit, price)



main()
# print("\n--- Blended Treat ---")
# print(f"Size: {SIZES}")
# print(f"Base: Starting your drink with {BASES} base.")
# print(f"Flavor: {FRUITS}.")
