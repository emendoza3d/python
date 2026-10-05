"""
-----------------------------------------------------------------------
ASSIGNMENT 8A: OPTION A - NATO TRANSLATOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. NATO_ALPHABET constant is a dictionary (Full A-Z).
[ ] 3. Program takes a word and uppercases it.
[ ] 4. Program loops through letters and prints NATO words.
[ ] 5. A 'try/except' block handles punctuation or numbers.
-----------------------------------------------------------------------
"""

# import random

nato_phonetics = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",
}

choice = 1

while True:
    try:
        print( )
        print(f"1.  Letter")
        print(f"2.  Word")
        print(f"3.  Exit")

        choice = int(input("Please enter the number of your selection:  "))

        match choice:
            case 1:
                word = input("Enter the letter you need: ").upper()
                for letter in word:
                    if letter in nato_phonetics:
                        print(nato_phonetics [letter], end = " ")

            case 2:
                value = input("Enter the word you need: ").strip().title()
                my_values = value.split()
                for the_value in my_values:
                
                    for letter, phonetic in nato_phonetics.items():
                        if the_value.upper() == phonetic.upper():
                            print(letter, end = "")

            case 3:
                print("Goodbye ;)")
                break
    except ValueError:
        print("data entry error")
        continue
    except Exception as e:
        print(e)





# quiz = list(nato_phonetics.items())
# random.shuffle(quiz)

# quiz_questions = dict(pairs)

# word = input("Enter the phonetic conversion you need: ").upper()

# # TODO: Loop through each character
# for letter in word:
#     if letter in nato_phonetics:
#         print(nato_phonetics [letter])

# # TODO: try to print the NATO code, except if character is missing







# for key, value in nato_pairs.items():
#     anser = int(input(f"please enter the letter you want the word for "))
#     if anser == key:
#         print("correct")
#         correct += 1
# score = correct / 10
# print(f"Score:")