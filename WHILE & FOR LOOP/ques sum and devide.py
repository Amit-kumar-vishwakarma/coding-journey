#

# take value from user

start = int(input("enter the starting number"))
end = int(input("enter the ending number"))
i = start
total = 0
while i <= end:
    if i % 2 == 0 and i % 7 == 0:
        total = total + i
    i = i + 1
print(f"total = {total}")
