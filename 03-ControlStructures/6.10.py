# Dog age calculator

# Pobieramy wiek psa w ludzkich latach
human_years = float(input("Enter the dog's age in human years: "))

# Liczymy wiek psa
if human_years <= 2:
    dog_years = human_years * 10.5
else:
    # Pierwsze 2 lata = 2 × 10.5
    dog_years = 2 * 10.5
    # Reszta lat = (human_years - 2) × 4
    dog_years += (human_years - 2) * 4

print(f"The dog's age in dog's years is {dog_years} years.")

