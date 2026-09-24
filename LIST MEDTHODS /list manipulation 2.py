nums = [4, 7, 3, 8, 1, 1, 2, 10, 9, 6, 9, 11, 34, 5, 5, 5, 1]

# # sort vs sorted 
# # sorted arranges the list in ascending order/desc
# # externally changes the values 
new_list = sorted(nums)
print(new_list)
# # # for ascending order 
# # internally arranges the values 
nums.sort()
print(nums)
# # for desc
nums.sort(reverse=True)
print(nums)

# # internally arranges the values in reverce order 
nums.reverse()
print(nums)
# use to find index of list 
print(nums.index(8))

# used to find that same number is repeating how many times 
print(nums.count(5))
# use to clear the list {not deleting just clearing the list}
nums.clear()
print(nums)

