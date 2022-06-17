# divisible by 5 or 6 but not both bn 100 and 200 ten per line
count = 0
for n in range(100,201):
    if n%6==0 and n%5==0:
        continue
    if n%6==0 or n%5==0 :
        print(n,end=" ")
        count += 1
    if count == 10:
        print("")
        count=0