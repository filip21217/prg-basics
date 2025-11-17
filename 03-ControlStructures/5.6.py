###
# Calculates the sum of even numbers from 1 to a given number N
#
N = 10
sum_even = 0

i = 1  # zaczynamy od 1

while i <= N:          # dopóki i jest mniejsze lub równe N
    if i % 2 == 0:     # jeśli liczba jest parzysta
        sum_even += i  # dodajemy ją do sumy
    i += 1             # przechodzimy do kolejnej liczby

print(f"The sum of even numbers from 1 to {N} is: {sum_even}")
