"""
Given two lists, merge them into a single new list without modifying theo riginals 
"""

# def merge_two_list(lst1,lst2):
#     return lst1+lst2

def merge_two_list(lst1,lst2):
    new_list =[]
    for num in lst1:
        new_list.append(num)
    for num in lst2:
            new_list.append(num)
    return new_list
    


num1=[2,33,44,5,66,7,7]
num2=[34,2,43,56,2,45,6]
print(merge_two_list(num1,num2))