total_sum = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break
    total_sum += number
    count += 1

# compute mean outside the loop
if count > 0:
    arithmetic_mean = total_sum / count
else:
    arithmetic_mean = 0  # no numbers entered

print(f"The total sum of the numbers is: {total_sum}")
print(f"The arithmetic mean of the numbers is: {arithmetic_mean}")