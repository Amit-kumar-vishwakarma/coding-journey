"""
given teo list of same length write a code using loop to creat
a new list where each element is the sum of corrosponding element
from both original lists.

"""


def sum_of_two_list(list1, list2):
    new_list = []
    n = len(list1)
    for i in range(0, n):
        total = list1[i] + list2[i]
        new_list.append(total)
    return new_list


nums1 = [6, -5, 4, 2, 10, 1, 75, 9, 9]
nums2 = [4, 1, 4, 76, 41, 5, 3, 44, 2]
ans = sum_of_two_list(nums1, nums2)
print(ans)
