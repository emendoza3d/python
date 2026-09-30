"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""
import random

# TODO: Create a tuple of at least 8 responses
RESPONSES = ("Yes", "No", "Maybe", "Ask again later","Look with in", "Didn't you ask that yesterday","Now your doin too much","It's too early for this")

print("Welcome to the Digital Oracle!")

while True:
    # TODO: Create a while loop that keeps asking questions
    topic = (input("Ask and I will provide eluminating clearity: ").lower().strip())

    if topic != "quit":

        selected = random.randint(0, 7)
        print(RESPONSES[selected])
        # TODO: Use random.choice(RESPONSES) to answer
        # TODO: If user types "quit", break the loop
    else:
        print("Goodbye")
        break