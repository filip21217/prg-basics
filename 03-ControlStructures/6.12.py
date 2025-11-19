num_products = int(input("Number of products purchased: "))
price = float(input("Product price: "))


if num_products <= 2:
    amount_to_pay = num_products * price
else:
  
    no_discount_cost = 2 * price
    
  
    discounted_products = num_products - 2
    discounted_price = price * 0.75   
    discount_cost = discounted_products * discounted_price

    amount_to_pay = no_discount_cost + discount_cost

print(f"Amount to pay: {amount_to_pay}")
