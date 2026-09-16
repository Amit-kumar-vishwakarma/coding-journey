"""
write a function that prints all the factors 
of a number entered by the user.
"""
def print_factors():
    num =int (input("Enter the number ="))
    for i in range (1,num+1):
          if num %i ==0:
               print(i,end=" ")


print_factors()