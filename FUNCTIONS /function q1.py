""" 
write a function that ask a number from user
 and print if number is even or odd 
"""

def odd_even():
    num =int (input("Enter the number ="))
    if num %2 == 0:
        print("even")
    else:
        print("odd")


odd_even()