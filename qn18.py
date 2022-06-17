# e^x approxiamtion
import  math

num = int(input("input number: "))

ex = 1

for n in range(1,20):
    ex = ex + (math.pow(num,n)/ math.factorial(n))


print("e^", num, " = ", ex)
