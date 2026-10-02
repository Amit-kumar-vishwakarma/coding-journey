"""
clean phone number 
take a phone number as input in the formate +91-657888-5590.
remove all dashes and their country code . print it in clean formate

"""

def clean_number(phone_number:str):
    phone_number =  phone_number.replace("-","")
    phone_number =  phone_number.replace("+91","")
    print(phone_number)


phone = "+91-657888-5590"
clean_number(phone)