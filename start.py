a = 3
b = 2
print('hello')
print(a + b)

def sum(a, b):
    return a + b

import math
def volume(h, r):
    return math.pi * (r ** 2) * h
print(volume(7, 3))

#x = [1001]

#y = len(x)

#i = 0
# import variable directly
from math import pi


def volume2(h, r):
    return pi * r ** 2 * h

# can do from math import *, but don't do that

print(volume(5, 5))
print(volume2(5, 5))

def bin2dec(str):
    num = 0
    for i, dig in enumerate(reversed([int(x) for x in list(str)])):
        num = num + ((2 ** i) * dig)
    return num

print(bin2dec('1001'))
print(bin2dec('10'))

# make list of tuples where first number is even & second number is the square
evens = [(x, x ** 2, y, y ** 3, x * y) for x in range(20) for y in range(3, 12, 3) if x % 2 == 0]

print(evens)






