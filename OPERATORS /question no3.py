"""
a student scored marks in 3 subjects . take all three as input
,calulate the avg and total ,and print both using f string
"""

sub1 = int(input("enter marks in sub 1="))
sub2 = int(input("enter marks in sub 2="))
sub3 = int(input("enter marks in sub 3="))
sub4 = int(input("enter marks in sub 4="))

total = sub1 + sub2 + sub3 + sub4

avg = (sub1 + sub2 + sub3 + sub4) / 4


avg = total / 4

print("total marks", total)
print("avg marks", avg)
