marks = {
    "science": 88,
    "maths": 67,
    "comp": 87,
    "history": 65,
}
# # it gives keys +value both
# print(marks.items())

# for i in marks.items():
#     print(i)

# this is giving tuples as output

# for detail in marks.items():
#  subject = detail[0]
#  marks = detail[1]
#  print(subject,marks)

#  this is acting as tuple and to unpack this we need to add two variable to it
# unpacking is happining at this place 
for subject, marks in marks.items():
    print(f" subject is {subject } and marks are {marks}")
