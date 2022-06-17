# ISBN

number = input("enter number :")
nums = []

nums[:0] = number

check_sum = (int(nums[0])*1 +int(nums[1])*2 +int(nums[2])*3 +int(nums[3])*4 +int(nums[4])*5 +int(nums[5])*6 +int(nums[6])*7 +int(nums[7])*8 +int(nums[8])*9 ) % 11

nums.append(str(check_sum))
out = ""
out = out.join(nums)
print(out)


