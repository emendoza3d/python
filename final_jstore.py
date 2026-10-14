

    #ring options, Global constants
SHAPE = ("round", "cushion", "marquise", "oval")
STYLE = ("solitaire", "halo", "vintage", "3 stone")
METAL = ("yellowg", "whiteg", "roseg", "platinum")
DIAMOND = ("natural", "lab")
MENU = "menu.txt"

def login():
    # Gets login info
    # returns customer ID
    if
        print("Already a customer? Please log in.")
        id = (input("Please enter your email:  "))
    else:
        print("First time with us? Let us get to know you")
        email = input("Email:  ").strip().lower()
        phone = input("Phone number:  ").strip()

        


        # Have customer text with ID and names, check if on it. If on it display name, office, extension otherwise get them.
    pass

def past_orders(Customer):
    # check for and display most recent 5 orders if there are any, ask if they want to reorder, give them menu
    # return number of past order or 6 if they want to create a new order
    pass

def new_order(customer):
    # display choices, collect information, save and pass back a LIST named order
    pass


def verify(order):
    # verify order by displaying on screen and asking confirm, correct, cancel
    pass


def save_order(order):
    # save to txt file
    pass


def change_order(order):
    # display numbered parts of order allow them to change
    pass


def display_order(order):
    # in real world would print label
    pass


# Main traditionally is coded at the end of the page so the other functions are loaded first
def main():
    # main organizes all of the functions
    id = login()
    saved = past_orders(id)
    # if saved order chosen  skip new order
    order = new_order(id)
    approved = verify(order)
    # if approved save - otherwise change
    save_order(order)
    change_order(order)
    display_order(order)


main()
