"""given a lidt of numbers , use a loop to calculalte
and print their average .
can use len() but avoide sum() for the total

"""


def calculate_avg(nums):
    n = len(nums)
    total = 0
    for num in nums:
        total += num
    return total / n


nums = [6, -5, 4, 2, 10, 91, -75, 49, 9]

ans = (calculate_avg(nums))
print(f"average is = {ans:.3f}")
