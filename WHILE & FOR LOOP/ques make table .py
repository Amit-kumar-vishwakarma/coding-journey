# ask a number from user , and print multiple table upto 10
# 4 x1 = 4
# 4 X2 = 8


num = int(input("enter the number ="))
i = 1
while i <= 10:
    ans = num * i
    print(f"{num}x {i}={ans} ")
i = i + 1
