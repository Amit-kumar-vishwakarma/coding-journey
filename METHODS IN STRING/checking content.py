"""
CHECKING CONTENT (T/F) 
isalpha(): All Letters? 
isdigit(): All Digits?
isalnum()): AlphaNumeric Only?
isspace): All Whitespace?
startswith() and endswith()
"""
# text= "vishwakarma"
# print(text.isalpha()) # it gives true and false 
# print(text.isdigit()) # it checks about digits
# print(text.isalnum()) # AlphaNumeric Only(either alphabet or string)
# print(text.isspace()) # checkes only spaces
# print(text.startswith("a")) # it checks the starting alphabet 
# print(text.endswith("a")) # it checks end alphabet 

# use case \
age = input("enter your age")
if age.isdigit():
   if int(age)>=18:
      print("you can vote")
   else:
      print("cant vote")
else:
   print("please enter proper age")
     