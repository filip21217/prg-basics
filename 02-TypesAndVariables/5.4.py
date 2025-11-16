import math 
amount = float(input("Enter the amount: "))
rounded_amount = round(amount, 2)
vat = (23/100) * rounded_amount
print("The VAT on the amount is:", vat)
