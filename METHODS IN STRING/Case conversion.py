"""
CASE CONVERSION

upper (): Converts all characters in the string to uppercase. lower (): Converts all characters in the string to lowercase.

title(): Converts the first character of each word to uppercase and the remaining to lowercase.

capitalize(): Converts only the first characterof the entire string to uppercase and the rest to lowercase.

swapcase(): Swaps the case of each character - uppercase becomes lowerase and vice versa.

"""

text = " Amit is a good programer"  # text is immutable (IT RETURNS)
ans = text.upper()
print(ans)
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())# converts small case letters to big vise versa 
