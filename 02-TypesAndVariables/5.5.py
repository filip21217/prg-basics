price = float(input('Enter price: '))
discount = float(input('Enter Discount in %: '))
discount_value = price * discount / 100
price_after_discount = price - discount_value
print(f'Price after discount is {price_after_discount}')
reduction = price - price_after_discount
print(f'Reduction value is: {reduction}')