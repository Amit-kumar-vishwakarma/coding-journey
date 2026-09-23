# used to print index and value both

#       0  1  2  3   4   5  6   7   8   9   10
nums = [3, 4, 6, 8, 23, 56, 89, 54, 32, 9, 22]

for index, value in enumerate(nums):
    print(f"index = {index} and value = {value}")




# print index of even numbers 

for index, value in enumerate(nums):
    if value %2==0:
        print (index)
    