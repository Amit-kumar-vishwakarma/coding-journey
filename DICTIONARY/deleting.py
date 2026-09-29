student = {
    "name": "amit",
    "age": 34,
    "gender": "male",
    "city": "lucknow",

}
print(student,id(student))
# pop uses to remove the item from a dictionary 

student.pop("name")
print(student)
print(student,id(student))

#  .clear (it is used to make dictionary empty )
# it removes all element from the table 
student.clear()
print(student)

# del(delet) it deletes the variable 

del student["age"]
print(student)