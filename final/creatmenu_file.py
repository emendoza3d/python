"""
-----------------------------------------------------------------------
ASSIGNMENT 12A: THE CONFIGURABLE MENU & AUDITOR
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. PHASE 1: External menu_config.txt file created in workspace.
[ ] 3. Program reads and parses the .txt file into a Dictionary.
[ ] 4. PHASE 2: break the dictionary into individual variables.
[ ] 6. Print each category and its details
[ ] 7. try/except used to prevent crashes on FileNotFoundError.
-----------------------------------------------------------------------
"""

def get_menu_options():
    menu = {}
    while True:
        print("Type 'Q' when done")
        category = input("Please give me the category for this part of the menu: ").upper()
        if category == "Q":
            break
        items = input("Please enter items separated by commas: ")
        menu[category] = items
    return menu

def save_to_file(menu):
    with open("menu.txt", "a") as file:
        all_items = menu.items()
        for item in all_items:
            output = (f"{item[0]} : {item[1]}")
            file.write(output + "\n")

def main():
    my_menu = get_menu_options()
    save_to_file(my_menu)

main()

