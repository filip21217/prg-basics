import math
h = float(input('Enter the height of the observer above sea level in meters: ' ))
h += 20
d = 3.57 * math.sqrt(h)
print('the distance to the horizon is', d)