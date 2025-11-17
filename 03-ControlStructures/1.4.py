account_balance = 500
total_payment = float(input('Amount to pay: '))

if total_payment < account_balance:
    print('Payment completed')
else:
    print('No funds')