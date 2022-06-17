x=int(input("Enter the number of students: "))
i=1
namelist=[]
scorelist=[]
while i <= x:
    name=input("Enter the name of student %d: "%i)
    score=int(input("Enter the score of student %d: "%i))
    namelist.append(name)
    scorelist.append(score)
    i+=1
print("student with the highest score is", namelist[scorelist.index(max(scorelist))] , "with score of %d"%max(scorelist))
