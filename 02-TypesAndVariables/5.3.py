
a = int(input('Enter length (a): '))
b = int(input('Enter width (b): '))
c = int(input('Enter height (c): '))


cuboid_volume = a * b * c
print('Cuboid Volume:', cuboid_volume)

surface_area = 2 * (a*b + b*c + c*a)
print('Surface Area:', surface_area)
