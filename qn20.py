# max of list and count
numbers = input('Enter numbers ')
user_list = numbers.split()
# print list
print('list: ', user_list)

for i in range(len(user_list)):
    user_list[i] = int(user_list[i])

max = 0
count = 0
for n in user_list:
    if n > max:
        max = n
        count = 0

    if n == max:
        count += 1



print("max: ",max ,"count: ",count)
