# e approximation


import  math

num = 1

ex = 1

for n in range(1,30):
    ex = ex + (math.pow(num,n)/ math.factorial(n))


print("e^", num, " = ", ex)
