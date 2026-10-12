"""

using functions to create a menu
"""

# global
NAMES = []  # an empty list


def display_menu():
    # display menu
    print("1.  Create")
    print("2.  Read")
    print("3.  Update")
    print("4.  Delete")

    try:
        selection = int(input("Please enter the number of your selection:  "))
    except Exception as e:
        print("Sorry. That was not a valid choice.")
        display_menu()

    return selection


def run_menu(choice):
    match choice:
        case 1:
            create()
        case 2:
            read()
            print(NAMES)
        case 3:
            update()
        case 4:
            delete()
        case _:
            print("Sorry, that is not a valid choice")
            value = display_menu()
            run_menu(value)


def create():
    # create a record
    name = input("Please enter your first name:  ")
    NAMES.append(name)


def read():
    # read a record
    pass


def update():
    # update a record
    pass


def delete():
    # delete a record
    pass


def main():
    value = display_menu()
    run_menu(value)
    print(NAMES)


main()
