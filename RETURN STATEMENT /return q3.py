"""
weite a function called abslite value
that takes the number and return 
its abslute value without using the built in abs() function 
"""

def abslute_value(num):
    if num >= 0:
        return num
    return num  * -1

print(abslute_value(100)) 
print(abslute_value(-100))
print(abslute_value(34))      