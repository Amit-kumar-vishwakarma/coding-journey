"""ask a number from user , and print al the factor

enter the number = 10
1 2 5 10"""

# num = int(input("enter the number ="))
# i=1
# while i <=num:
#     if num %i==0:
#          print(i ,end=" ")
#     i =i+1


""" ask a number from user , and count al the factor 

enter the number = 10 
1 2 5 10  answer will be 4"""

num = int(input("enter the number ="))
i = 1
count = 0
while i <= num:
    if num % i == 0:  
        count = count + 1
    i = i + 1

print(f"total factors of {num}are {count}")
