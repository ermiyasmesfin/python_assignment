# loan calculator

# tuition =10000
#
# time = 10

def interest(am,time,rate):
    return am *(1 + rate) ** time


amount =int(input("enter amount: "))
years =int(input("enter years: "))

percent = 5.0
print("interest rate        total payment")
while percent <= 8.0:
    print(percent,"%",end="     ")
    print(interest(amount,years,percent))
    percent += 0.125