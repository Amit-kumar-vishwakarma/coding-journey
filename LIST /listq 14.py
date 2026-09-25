"""
Write a Python script that iterates through a list of integers and replaces every negative number found in the list with the value 0.
"""


def replace_value(lst):
    n = len(lst)
    for i in range(0, n):
        if lst[i] < 0:
            lst[i] = 0
    return lst


nums = [-1, 0, 0, -2, 2, 3, 4, -50, 0, -6, 0, -8]
print(replace_value(nums))
