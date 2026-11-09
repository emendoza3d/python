
import readmenu
MENU = "menu.txt"

def login():
    # Gets login info
    # returns customer ID
    
    print("Already a customer? Please log in.")
    id = (input("Please enter your email:  "))
    
    print("First time with us? Let us get to know you")
    email = input("Email:  ").strip().lower()
    phone = input("Phone number:  ").strip()
    name = input("Full Name:   ").strip().lower()

    with open ("customer.txt", "a") as f:
        f.write(f"{id}, {email}, {phone}")

    return id
        


        # Have customer text with ID and names, check if on it. If on it display name, office, extension otherwise get them.
   

def past_orders(Customer):
    # check for and display most recent 5 orders if there are any, ask if they want to reorder, give them menu
    # return number of past order or 6 if they want to create a new order
   print("Tell us about your dream piece.")


def new_order(id):
    menu_items = readmenu.read_menu()
    print(menu_items)
    Shape, Style, Metal, Diamond = readmenu.split_into_variables(menu_items)

    # display choices, collect information, save and pass back a LIST named order
    # start here 1
    for shape_option in Shape.split(","):
        print(f"  {shape_option.strip()}")
    my_shape = input("Please enter the shape you want: ").strip()

    for style_option in Style.split(","):
        print(f"  {style_option.strip()}")
    my_style = input("Please enter the style you're looking for: ").strip()

    for metal_option in Metal.split(","):
        print(f"  {metal_option.strip()}")
    my_metal = input("Please enter the type of metal you would like: ").strip()

    for diamond_option in Diamond.split(","):
        print(f"  {diamond_option.strip()}")
    my_diamond = input("Please enter the diamond you're looking for: ").strip()
    return my_shape, my_style, my_metal, my_diamond



def verify(Shape = "round", Style = "halo", Metal = "yellow gold",Diamond = "natural"):
    print(my_shape)
    print(my_style)
    print(my_metal)
    print(my_diamond)

def main():
    my_shape, my_style, my_metal, my_diamond = new_ring()
    verify(my_shape, my_style, my_metal, my_diamond)
    # verify order by displaying on screen and asking confirm, correct, cancel
    


def save_order(order):
    # save to txt file
    with open ("ring_order.txt", "b") as f:
        f.write(f"{my_shape}, {my_style}, {my_metal}, {my_diamond}")

    

   


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