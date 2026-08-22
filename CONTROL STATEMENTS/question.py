"""
take number as input from user one by one .
skip negative numbers and keep adding positive num
stop when user enters o and print the total
(use both continue and break)
"""

total = 0
while True:
    num = int(input("enter the number="))
    if num == 0:
        break
    if num < 0:
        continue
    total += num

print(total)
