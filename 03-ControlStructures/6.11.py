current_price = float(input('Enter current price: '))
p_price = float(input('Enter previous price: '))
reduction = (p_price - current_price) / p_price * 100
print(f'Price has been reduced by {reduction}%')
if reduction >= 10:
    print('Buy the product!!')
else:
    print("Don't buy the product!!")