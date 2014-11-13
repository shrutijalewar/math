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

def bin2dec(bin):
    sum = 0
    for index, bit in enumerate(bin[::-1]):
        sum += int (bit) * (2 ** index)
        return sum
print(bin2dec(1001))

#def bin2dec(x):
 #   while i < y:
  #      i = i + 1
   # while p < y:
    #    s = (p * x[i] , p - 1 * x[i + 1])
     #   return print(s)


