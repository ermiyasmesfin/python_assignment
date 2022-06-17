# proper number and divsiors

num =int(input("input number : "))

for n in range(1,num+1):
    tot = 0
    if num % n == 0:
        print(n, end=" , ")
        tot = tot + n
print("")
if tot == num:
    print(num," is perfect")
else :
    print(num," is NOT perfect")