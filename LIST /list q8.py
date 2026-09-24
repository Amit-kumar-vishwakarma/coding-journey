"""
write a program that takes a list of numbers
using a loop and determine wether it is shorted or not
print true or false
"""


def is_sorted(lst):
    n=len(lst)
    for i in range(0,n-1):
        if lst[i]>lst[i+1]:
            return False
    return True
nums = [3, 6, 8, 9, 13, 17, 18, 23, 45, 58, 79, 100]

print(is_sorted(nums))
