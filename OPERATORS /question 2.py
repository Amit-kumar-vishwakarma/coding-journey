"""take the users age as input
chek wether they are elegible to vote(age>=18)and
 wether they are senior citizen (age>=60).print both results."""

age = int(input("Enter your age = "))
can_vote = age >= 18
senier_citizen = age >= 60

print(f"user can vote={can_vote}")
print(f"user is senier citizen={senier_citizen}")



# using if else
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote: Yes")
else:
    print("Eligible to vote: No")

if age >= 60:
    print("Senior citizen: Yes")
else:
    print("Senior citizen: No")