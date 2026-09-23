"""
erite a program that takes a list and a target number
use a loop to determine if the target number
exits in the list .
dont use operator
"""


def target_exists(lst, target):
    for num in lst:
        if num == target:
            return True
    return False


nums = [6, -5, 4, 2, 10, -75, 49, 9]

print(target_exists(nums, 18))
print(target_exists(nums, 9))
