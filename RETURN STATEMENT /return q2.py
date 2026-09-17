"""write a function called min_of_three
and return the smallest without using
any built in function
"""


def min_of_three(n1, n2, n3):
    if n1 < n2 and n1 < n3:
        return n1
    elif n2<n3 and n2<n1:
        return n2
    return n3


print(min_of_three(30,40,20))
print(min_of_three(0,4,20))