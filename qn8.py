# prime checking

def check_prime(n):
    for x in range(2,n):
        if(n % x) == 0:
            return False
    return True

print(check_prime(11))



# sum digits

def sum_dig(n):
    total = 0
    for x in str(n):
        total = total + int(x)
    return total

print(sum_dig(34))
