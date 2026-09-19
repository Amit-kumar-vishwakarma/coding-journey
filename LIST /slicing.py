# slicing

lst = [12, 23, 34, 55, 76, 75, 75, 85, 76, 91, 0]

print(lst[0:4])
print(lst[-1:-5])
# to go to end 
print(lst[0:])
# leave blank space after 1st index 
# same happens for starting too
print(lst[:4])

# to leave or jump steps 
print(lst[0:9:2])

# to move through negative 
print(lst[9::-1])