parking_hours = int(input('Enter how many hours did you use parking: '))
if 1<= parking_hours <= 2:
    print("Amount to pay is 5 PLN")
elif 3<= parking_hours <=6:
    print('Amount to pay is 15 PLN')
elif parking_hours > 6:
    print('Amount to pay is 20 PLN')