"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""

TOPPINGS = ("extra cheese", "sausage", "mushroom", "olives")
SIZE = ("Small", "Medium", "Large")

def your_order(customer, toppings = "None", size = "Medium"):
    pass

def create_order():
    customer = input("Name  ")
    for pizza in SIZE:
        print (f"  {pizza}")
    my_size = input("Please enter what size pizza you want.  ")
    for topping in TOPPINGS:
        print (f"  {topping}")
    my_toppings = (input("Please enter the the toppings you would like seperated by commas or type none if you don't want any.  "))

    # delivery options
    answer = input("Pick-up or delivery? (P/D):  ").lower()

    if answer == "d":
        delivery = True
        print("Delivery")
    else:
        delivery = False
        print("Pick-up")
    if delivery :
        my_delivery = "delivery"
    else: my_delivery = "Pick-up"
    return customer, my_size, my_toppings, my_delivery

def make_pizza(customer, my_size = "medium", my_toppings = "none", delivery = "pick-up"):
    print(customer)
    print(my_size)
    print(my_toppings)
    print(delivery)
    
def main():
    customer, my_size, my_toppings, delivery = create_order()
    make_pizza(customer, my_size, my_toppings, delivery)
main()