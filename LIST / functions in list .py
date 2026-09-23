marks = [23, 34, 56, 44, 64, 45, 23]

# to get the length
n = len(marks)
print(f"length of list={n}")

# max
maximum = max(marks)
print(f"maximum marksin list={maximum}")

# min
minimum = min(marks)
print(f"minimum marks in list={minimum}")
# sum
total = sum(marks)
print(f"sum of marksin list ={total}")

# to sort using sorted ()function
# it will always returns new list in assinding/decending order

# to sort (assending order )
new_list = sorted(marks)
print(f"new_list is ={new_list}")

# to sort (decending order )
new_list = sorted(marks, reverse=True)
print(f"new_list is ={new_list}")
