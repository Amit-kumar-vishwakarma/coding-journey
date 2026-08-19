"""
90 abobe ->A
81 to 90 ->B
71 to 80 ->C
61 to 70 ->D
60 and below -> fail
"""

marks = int(input("entaer marks="))
if marks >= 90:
    print("pass with first devision")

elif marks >= 80:
    print("pass with second devision")

elif marks >= 70:
    print("pass with third devision")

else:
    marks <= 60
    print("you are fail")
