"""
Reverse a list without using the reverse() method
or list slicing
"""


def reverse_list(lst):
    n = len(lst)
    new_list = []
    for i in range(n - 1, -1, -1):
        new_list.append(lst[i])
    return new_list


nums = [2, 4, 5, 67, 8, 3, 3, 5, 34, 345]

ans = reverse_list(nums)
print(ans)
