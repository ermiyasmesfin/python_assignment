# tuition increase

tuition =10000
rate =0.05
time = 10

def compound(time):
    return tuition *(1 + rate) ** time

print("after ten years: ",compound(10))
print("4 years total : ",compound(10)+compound(11)+compound(12)+compound(13))
