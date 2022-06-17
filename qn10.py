# student mark greater 20


total = input("enter total :")
marks = []
greater = 0
for n in range(0, int(total)):
    marks.append(int(input("enter mark : ")))

for n in range(0, int(total)):

    if marks[n] > 20:
        greater = greater + 1

print(greater)

