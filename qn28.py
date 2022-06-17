x=int(input("Enter the number of students: "))
i=1
namelist=[]
scorelist=[]
sortedlist=[]
while i <= x:
    name=input("Enter the name of student %d: "%i)
    score=int(input("Enter the score of student %d: "%i))
    namelist.append(name)
    scorelist.append(score)
    i+=1
sortedlist=sorted(scorelist)
secondhighest=sortedlist[-2]
print("student with the highest score is", namelist[scorelist.index(max(scorelist))] , "with score of %d"%max(scorelist))
print("student with the second highest score is", namelist[scorelist.index(secondhighest)], "with score of %d"%int(secondhighest))

