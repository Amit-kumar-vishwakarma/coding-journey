# start and end by user 
# start to end print using while loop 
start =int(input ("enter the starting number"))
end= int(input("enter the last nujmber"))
i = start
while i <= end:
    print(i,end=" ")
    i += 1
    print(f"after while loop, start value is {start}")