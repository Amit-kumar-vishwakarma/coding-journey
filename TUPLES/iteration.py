my_tuple = (1, 2, 3, 4, 5, 6.7, "amit")
n = len(my_tuple)
for i in range(0, n):
    print(my_tuple[i], end=" ")


print()
for element in my_tuple:
    print(element, end=" ")


print()
for ( index,value,)in enumerate(my_tuple):
    print(f"index = { index} and value = {value}")
