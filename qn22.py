# digit count

def counter (n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    print("number of digits: ", count)


number = 1
isneg = False
while number > 0:

    while True:
        try:
            number = int(input("enter number: "))
            break
        except:
            print("Please input an  integer")
    if number > 0:
        counter(number)
