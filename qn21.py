# xyz =cubic sum
import math


def sum_cubic(n):
    total = 0
    for x in str(n):
        total = total + math.pow(int(x), 3)
    return total


def check(a,b):
    for n in range(a,b):
        if n == sum_cubic(n):
            print(n)


check(100,1000)