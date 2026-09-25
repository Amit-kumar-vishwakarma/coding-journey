# make a list from 1 to 10 ->[1,2,3,4,....9,10]
# treditional method
new_list = []
for i in range(1, 11):
    new_list.append(i)
print(new_list)


# list comprehention
new_list = [i for i in range(1, 11)]
print(new_list)

# all negatiove(10,9,8...)
new_list = [i for i in range(10, -1, -1)]
print(new_list)

# print 1 to 10 but square

new_list = [i * i for i in range(1, 11)]
print(new_list)

# 1 to 20 but inly even numbers
new_list = [i for i in range(1, 21) if i % 2 == 0]
print(new_list)
