"""
Given a list of numbers (which may contain duplicates),
write a Python script that takes an integer as input from the user
 and removes all occurrences of that integer from the list
"""

# method1
# this  method will be fail if there in more same number symultaniously
# def remove_occurence(lst, target):
#     for num in lst:
#         if num == target:
#             lst.remove(num)
#     return lst

# method 2
# this removes all the same value and makes a new list
# def remove_occurence(lst, target):
#     new_list=[]
#     for num in lst:
#         if num != target:
#             new_list.append(num)
#     return new_list


# mwthod3
# change in same list
def remove_occurence(lst, target):
    while target in lst:
        lst.remove(target)


nums = [2, 2, 2, 3, 45, 5, 3, 3, 3, 3, 45, 6, 34, 4, 6]
remove_occurence(nums, 2)
print(f"nums={nums}")
