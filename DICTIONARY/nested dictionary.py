students = {
    "101": {"name": "Rahul", "age": 21, "city": "Delhi"},
    "102": {"name": "Priya", "age": 20, "city": "Mumbai"},
    "103": {"name": "Karan", "age": 22, "city": "Pune"},
}
# accessing dictionary 
# inserting key under key helps to access the dictionary 
# print(students["101"])
# print(students["101"]["name"])
# print(students["101"]["city"])
total =0
for roll_no ,details in students.items():
    # to get specific things like name, age, etc
    total += details['age']
    print(f"roll_no={roll_no} and details are ={details["name"]},age = {details['age']}")
print(total)