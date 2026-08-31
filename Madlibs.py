"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Copy and paste THIS comment from opening to closing quotes).
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

# ℹ️ Little Jack Horner
# Sat in the corner,
# Eating a Christmas pie;
# He put in his thumb,
# And pulled out a plum,
# And said, "What a good boy am I!"
# 🆘 Help


# ℹ️ Declare Variables
name = ""  # ℹ️ initialixex the variable (optional)
place = ""
food = ""
body_part = ""
fruit = ""
human = ""


# ℹ️ Get user input and assign to varibles

name = input("please enter a person's name: ")
place = input("please enter a type of place: ")
food = input("please enter a food: ")
body_part = input("please enter a body part: ")
fruit = input("please enter a type fruit: ")
human = input("please enter a type of human: ")


#  ℹ️ Output
print(f"mad Lib for Little Jack Horner\n\n")
print(f"Little {name}\n\n")
print(f"Sat in the {place}\n\n")
print(f"Eating a {food}\n\n")
print(f"He put in his {body_part}\n\n")
print(f"And pulled out a {fruit}\n\n")
print(f"And said, What a good {human} am I!\n\n")
