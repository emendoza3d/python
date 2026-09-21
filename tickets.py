"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
Step 2: The Logic Guide
You will need a while loop to keep the process running. Inside the loop:

Print the seats list so the user knows what is available.
Get input (remember to cast to int).
The Exit Switch: Check if the choice is 0. If it is, use break to end the program.
The Membership Check: Use if choice in seats:
If yes: Use seats.remove(choice) to sell the ticket.
If no: Print a friendly message saying that seat is gone or doesn't exist.
-----------------------------------------------------------------------
"""

seats = list(range(1, 21))
# until user types 0
while True:
    if len(seats) == 0:
        print("Sorry there are no seats left. Goodbye.")
    print(seats)

    try:
        seat = int(input("Which seat would you like?: "))
        if seat == 0:
            print("Goodbye")
            break
        seats.remove(seat)
        continue
    except ValueError:
        print("Sorry, the seat you selected in not available please select another.")
        continue
