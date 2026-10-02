"""
Email Validation

Take one email as input ,validate it contains exactly one @ and atleast one .
Print "Valid" or "Invalid".
email = "info@codeanddebug.in"
"""
def check_email_validatiion(email:str):
    if email.count("@")==1 and "." in email:
        return "valid"
    return "invalid"


email = "amit@gmail.com"
print(check_email_validatiion(email))
