# sum of series

tot = 0

for n in range(1, 96, 2):
    tot = tot + n/(n+2)
print(tot)