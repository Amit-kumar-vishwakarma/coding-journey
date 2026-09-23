#       0  1  2  3   4   5  6   7   8   9   10
nums = [3, 4, 6, 8, 23, 56, 89, 54, 32, 9, 22]

n = len(nums)
i = 0
while i <= n - 1:
    print(
        nums[i],
    )
    # print(nums[i],end=" ") if need in horijontal
    i += 1

# iterating from last to first
i = n - 1
while i >= 0:
    print(nums[i], end=" ")
    i = i - 1
