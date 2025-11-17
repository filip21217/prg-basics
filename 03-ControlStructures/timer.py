###
# Takes a number from the user and counts down to zero.
# Last five seconds are shown in words.
#
import time

countdown = int(input("Enter the number of seconds to count down: "))

while countdown > 0:

    # Ostatnie 5 sekund pokazujemy słownie
    if countdown == 5:
        print("five")
    elif countdown == 4:
        print("four")
    elif countdown == 3:
        print("three")
    elif countdown == 2:
        print("two")
    elif countdown == 1:
        print("one")
    else:
        print(countdown)

    countdown -= 1
    time.sleep(1)  # Wait for 1 second

print("Time's up!")

