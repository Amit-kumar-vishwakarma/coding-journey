student = {
    "" "name": "amit",
    "age": 34,
    "dender": "male",
    "city": "lucknow",
}
# it is taking string as value [it only check for keys ]
print ("age"in student)
# thatswhy when we put real value instead of keys it prints false 
print (34 in student)

# basic understanding
k = input("emter key= ")
if k in student:
    print(student[k])
else:
    print("key not found")