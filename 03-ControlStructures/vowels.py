###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0

i = 0  # ZACZYNAMY indeks od 0

while i < len(text):  # dopóki i jest mniejsze od długości tekstu
    char = text[i]     # bierzemy znak na pozycji i
    if char in vowels: # sprawdzamy, czy jest samogłoską
        vowel_count += 1
    i += 1              # PRZESUWAMY SIĘ O JEDNO MIEJSCE

print(f"The number of vowels in the text is: {vowel_count}")
