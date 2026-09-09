# while loop demo
# calculating average test score

Entering = True  # flag
total = 0
count = 0


while entering:
    print("Enter each test score, enter -1 when done.")
    score = float(input("Enter the test score:  "))
    if score > 0:
        total += score  # short cut total = total + score
        count += 1
    else:
        print("Entry completed")


average = total / count

print(f"The average test score was: {average:,.1f}")



for x in range(1, 11):
    print(x)

for y in range(10, 0, -1):
    print(y)

for day in ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", ):
int(day)