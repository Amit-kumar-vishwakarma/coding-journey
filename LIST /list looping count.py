# COUNT EVEN NUMBERS IN THIS LIST

#       0  1  2  3   4   5  6   7   8   9   10
nums = [3, 4, 6, 8, 23, 56, 89, 54, 32, 9, 22]

n = len(nums)
i = 0
Count = 0
while i <= n - 1:
    if nums[i] % 2 == 0:
        #  if nums[i] % 2 != 0: for odd numbers 
        Count += 1
    i += 1
print(Count)