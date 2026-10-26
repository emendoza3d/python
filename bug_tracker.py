"""
-----------------------------------------------------------------------
ASSIGNMENT 11A REVISED: THE BUG TRACKING LOG
-----------------------------------------------------------------------
[ ] 1. Program uses a while loop to keep asking for bugs.
[ ] 2. Uses the datetime module to get a timestamp format.
[ ] 3. Stores the timestamp, file name, description, and priority in a dictionary.
[ ] 4. Uses `with open("bug_log.txt", "a")` to append to the file safely.
[ ] 5. The bug_log.txt file is formatted neatly with newlines.
-----------------------------------------------------------------------
"""

import datetime

right_now = datetime.datetime.now()



def append_lines():
        
    while True:    
        my_file = input("Please enter File    ")
        discription = input("Please enter Error Discription   ")
        priority = input("Please enter Priority as high, medium, or low   ")
        another = input("Do you need to enter another y/n?  ")

        with open("bugtracker.txt", "a") as f:
            f.write(f"{right_now}\n")  
            f.write(f"File: {my_file}\n") 
            f.write(f"Error Discription: {discription}\n") 
            f.write(f"Priority: {priority}\n") 
        if another == ("y"):
            continue
        else:
            break


def main():
    with open("bugtracker.txt", "a") as f:
        f.write("-----Bug Errors-----/n")
    append_lines()

        
main()            
                            