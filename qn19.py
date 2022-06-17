# leap year betwwen 2001-2100

tot = 0
for year in range(2001,2101):

    if (year % 400 == 0) and (year % 100 == 0):
        print(year, end=" ")
        tot += 1
    elif (year % 4 == 0) and (year % 100 != 0):
        tot += 1
        if tot % 10 == 0:
            print(year)
        else:
            print(year, end=" ")

