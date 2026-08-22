# take value from user and add them also
start = int(input("enter the starting number="))
end = int(input("enter the end number ="))

total = 0

for i in range(start, end + 1):
    total += i

print(total)
