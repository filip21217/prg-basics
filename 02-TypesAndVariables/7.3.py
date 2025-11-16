n = float(input('Wpisz liczbę: '))

if n.is_integer():        
    if int(n) % 2 == 0:
        print('Liczba jest parzysta')
    else:
        print('Liczba jest nieparzysta')
else:
    print('To nie jest liczba całkowita, więc nie może być parzysta')