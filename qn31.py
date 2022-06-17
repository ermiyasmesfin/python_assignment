# ascii ! to ~

count = 0
for i in range(33,127):
    ch = chr(i)
    print(ch,end=" ")
    count += 1
    if count == 10:
        print("")
        count=0