"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 5 inputs have 'while' loop validation.
[ ] 3. The more tickets loop uses .upper() and correct Boolean logic.
[ ] 4. Include a try and except statement around the entire program. Should have one defined
       exception (probably value error) and a generic exception
[ ] 5. Have pinned a variable in the WATCH window and took a screenshot.
First Name & Last Name: Cannot be blank.
Age: Must be a number; also check whether they are older or younger than 21 to determine whether they get a drink ticket.
Phone Number: Cannot be blank.
Ticket Count: Must be a valid integer > 0 (Crash-Proof!).
Additional Tickets? (Y/N)
-----------------------------------------------------------------------
"""

fname = ""

while not fname:
    fname = input("Please tell us your First name:  ").upper()
    fname = fname.strip()

lname = ""

while not lname:
    lname = input("Please tell us your Last name and Last name:  ").upper()
    lname = lname.strip()

age = ""

while not age or age < 0:
    age = int(input("Please tell us your age:  "))

phnumber = ""

while not phnumber:
    phnumber = input("Please tell us your Phone Number:  ")
    phnumber = phnumber.strip()

tickets = ""
tickets = -1

while tickets < 0 or not tickets:
    tickets = int(input("Please tell us how many tickets you need.  "))

more = ""
while more != "Y" and more != "N":
    more = input("Will you be needing more tickets?:  ").upper()
