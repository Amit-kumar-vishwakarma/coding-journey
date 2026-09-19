lst = ["amit", "vikas", "vishal", "anand", 56, 90, 0, 22, 0.5]
# print(lst[0])
# print(lst[1])
# print(lst[3])
# print(lst[5])
# print(lst[8])
# print(lst[-1])
# print(lst[-5])
# print(lst[-8])
# to print last element
print(f"last element={lst[-1]}")
print(f"last element={lst[8]}")

# without using -1
n = len(lst)
print(f"last element is = {lst[n-1]}")
