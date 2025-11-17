ean_n = input('Enter Ean-13 number: ')

while True:
    if len(ean_n) == 13:
        break
    else:
        print('Invalid number')
        ean_n = input('Enter Ean-13 number: ')

print('Article number is correct')

if ean_n[0] == '5' and ean_n[1] == '9' and ean_n[2] == '0':
    print('Product manufactured in poland')
else:
    print('product not manufactured in poland')