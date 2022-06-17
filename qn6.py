# factorial recurrsive
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)


inp = input("number: ")
print("factorial is : ", factorial(int(inp)))