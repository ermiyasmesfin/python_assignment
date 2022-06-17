# hr to min kilo to pound  mile to km


def hr_to_min(hr):
    return hr*60

def kg_to_lb(kg):
    return kg*2.2

def mile_to_km(mile):
    return mile*1.609

print("enter 1 for length ,2 for weight ,3 for time  conversion")
choice= int(input("enter choice :"))

num= int(input("enter value :"))
if choice == 1:
    print(num," mile = ",mile_to_km(num), " kms")
elif  choice == 2:
    print(num," Kg = ",kg_to_lb(num), " lbs")
elif  choice == 3:
    print(num," Hours = ",hr_to_min(num), " mins")