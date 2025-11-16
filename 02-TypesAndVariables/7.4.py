# Pobranie obwodu drzewa od użytkownika
circumference = float(input("Podaj obwód drzewa w cm: "))

# Obliczenie średnicy (π ≈ 3.14)
diameter = circumference / 3.14

# Sprawdzenie, czy drzewo można ściąć
can_cut = diameter >= 50

# Wyświetlenie wyniku
print("Drzewo można ściąć:", can_cut)
