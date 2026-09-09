"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""

# while loop
there = False
while not there:
    answer = input("Are we there yet? (yes/no):  ").lower()

    if answer == "yes":
        there = True


# 99 bottles of beer on the wall


for i in range(99, 1, -1):

    print(f"{i} Bottles of beer on the wall")
    print(f"{i} Bottles of beer")
    print("Take one down,")
    print("Pass it around,")
    print(f"{i-1} Bottles of beer on the wall\n\n")

print(f"1 Bottle of beer on the wall")
print(f"1 Bottle of beer")
print("Take one down,")
print("Pass it around,")
print(f"0 Bottles of beer on the wall\n\n")
