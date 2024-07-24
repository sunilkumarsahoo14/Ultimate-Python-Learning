# Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [1, 4, 5, 78, 434, 233, 76, 99]

def greater(a, b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))