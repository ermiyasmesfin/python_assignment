# check prime


def check_prime(n):
    for x in range(2,n):
        if(n % x) == 0:
            return False
    return True

print(check_prime(11))

