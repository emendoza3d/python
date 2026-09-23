"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Department constant defined in ALL_CAPS.
[ ] 3. Username tuple and password list defined.
[ ] 4. While loop runs interactively.
[ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
Header Docstring: Include the complete checklist docstring at the top of your file. (Note: Do not include student names per grading policy).

Department Constant: Define a system constant in ALL_CAPS representing your department name.

Parallel Structures: Define a constant tuple for usernames (`USER_NAMES`) and a parallel mutable list for passwords (`passwords`).

Interactive `while` Loop: Use a persistent while loop to keep the terminal running so users can look up users, update passwords, or test security tampering. Provide a menu of options - lookup username, change username, change password, quit - change username will break

The Tamper Trap (`try/except`): Allow the user to attempt changing a username inside the tuple. Catch the resulting TypeError and print a message telling the user to email the help desk because usernames cannot be changed.

Password Updates: Allow the user to update a password inside the mutable list using a valid index.

Error Handling: Gracefully catch ValueError and IndexError when handling index lookups or numerical input.
"""

# try statement


# set department name
DEPARTMENT = ("Mages",)
# set tuple for user names
USERNAME = (
    "Sam",
    "Timmy",
    "Jimmy",
    "Kevin",
    "Rob",
)

# set passwords"

password = [
    "lkj",
    "asdf",
    "werre",
    "zxcvzx",
    "mnbkjhk",
]


while True:
    try:

        print(f"1.  Look up Username")
        print(f"2.  Add Username")
        print(f"3.  change Password")
        print(f"4.  Exit")

        choice = int(input("Please enter the number of your selection:  "))

        match choice:
            case 1:
                name = input("Please enter user name you want to look up  ")
                if name in USERNAME:
                    print(f"{name} is an employee")
                else:
                    print(f"{name} is not an employee")

            case 2:
                name = input("Please enter user name you want to add  ")

                USERNAME.append(name)

            case 3:
                name = input("Please enter the user name:  ")
                if name in USERNAME:
                    location = USERNAME.index(name)
                    new_password = input("Enter new password  ")
                    password[location] = new_password
                    print("Password has been changed")
                    print("password")
                else:
                    print("I'm sorry, that user does not exist.")

            case 4:
                print("Have a good day")
    except ValueError:
        print("data entry error")
    except Exception as e:
        print(e)

# except stateme,nt
