# max and min list


total = input("enter total :")
numbers = []

for n in range(0, int(total)):
    numbers.append(int(input("enter number : ")))


print("maximum= ", max(numbers), "minimum= ", min(numbers))

