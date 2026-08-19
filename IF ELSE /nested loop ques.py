"""take a year as input .check wether it is a leap year
if it is divisible by 4 but not divisable by 100 , unless it also devisable by 400

200 not a lea year
204 leap year
400 nota leap year
"""

year = int(input("enter year="))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("leap year")
else:
    print("not a lrap year")
