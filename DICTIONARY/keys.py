marks = {
    "science": 88,
    "maths": 67,
    "comp": 87,
    "history": 65,
}
# # keys helps us to print the keys of a dictionary
# # 
# print(marks.keys()) 

# # iteration 
# for sub in marks.keys():
#   print(sub)

# #    to print the value with key 
# for sub in marks.keys():
#   print(sub,marks[sub])

# # another way 
#   print(f"subject={sub} and marks ={marks[sub]}")

#    to get total
total=0
for sub in marks.keys():
    print(f"subject={sub} and marks ={marks[sub]}")
    total += marks[sub]
print(total)