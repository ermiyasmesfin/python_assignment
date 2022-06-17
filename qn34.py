column = 8
k = column * 2
for i in range(column):
    column = (7-i)*4
    n = 0

    for space in range(1, k):
        print(end=" ")
    k -= 1

    for j in range(1, k):
        print(end="  ")
    for b in range(i+1):
        a = 2**n
        print(a, end="  ")
        n += 1
    n -= 2
    for b in range(i):
        a = 2**n
        print(a, end="  ")
        n -= 1
    print()