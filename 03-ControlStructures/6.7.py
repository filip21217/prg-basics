age = int(input('Enter your age: '))
if age < 13:
    print("You're a child")
elif 13 <= age <= 19:
    print("You're a Teen")
elif 20 <= age <= 64:
    print("You're a Adult")
elif age > 64:
    print("You're a Senior")  