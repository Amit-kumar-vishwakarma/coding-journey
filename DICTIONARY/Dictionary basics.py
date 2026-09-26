marks = {
    "science": 88,
    "maths": 67,
    "comp": 87,
    "history": 65,
}
# # in dictionary key values cant be replaceed .
# print(marks["science"])
# #  get dont shows syntex error it prints none as default
# print(marks.get("sciencee",0))
# #  to change the default value just put desired value after comma 

subject = "history"
ans = marks.get(subject)
if ans is None:
    print ("subject not found")
else:
    print(f"marks scored = {ans}")
