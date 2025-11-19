def f(number, even):
    y = 0
    x = str(number)
    for i in x:
       x = int(i)
       if even :
          if x % 2 == 0:
             y += x
        if not even:
          if x % 2 != 0:

#def f(x, y):
#    count = 0
#    for n in range(x, y):
#        if n < 0 and n % 2 == 0:
#            count += 1
#    return count  