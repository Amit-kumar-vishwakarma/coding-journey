"""
given a list of numbers , write pytthon code to find and print
largest element . dont use built in max function
"""

nums = [6, -5, 4, 2, 10, -75, 49, 9]
maxi = float("-inf")
for num in nums:
    if num > maxi:
        maxi = num
print(f"maximum number = {maxi}")
