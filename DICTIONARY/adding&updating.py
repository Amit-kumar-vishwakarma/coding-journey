student = {"name": "rahul", "age": 21}
print(student, id(student))
# updating
student["age"] = 30
print(student, id(student))

# adding

student["gender"] = "male"
print(student)

# update
student.update(
    {
        "city": "surat",
        "phone": 12344565,
        "stste": "mumbai",
        "houseno": 23,
    }
)
print(student)
