nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 11, 34, 5, 5, 5, 1]

target = int(input("enter the target value ="))
if target in nums:
    nums .remove(target)
    print(f"nums{nums}")
else:
    print("cant remove")