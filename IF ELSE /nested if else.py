"""the question says that if a person is greater then 18
and he is cltisen of india ,he can vote
if he is less then 18 he is a child"""

age = int(input("enter your age"))

if age >= 18:
    citizenship = input("enter your citizenship ")
    if citizenship == "inian":
        print("you can vote")
    else:
        print("you cant vote")

else:
    print("you are underage")
