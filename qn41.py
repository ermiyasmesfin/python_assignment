# sum of series factorial sum to n
import math
n = 5
tot = 0

for i in range(1,n+1):
    tot = tot + math.factorial(i)


print("sum = ",tot)