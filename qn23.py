# count prime in range

def check_prime(num):
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                return False
        return True
    else:
        return False

a= int(input("input number :"))
count = 0
for n in range(2,a+1):
    if check_prime(n):
        count += 1

print("number of primes upto",a,"is :",count)