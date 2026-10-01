"""
sort with last block of numbers """

marks ={
    "akshy": [43, 12, 98, 10, 22],
"priya":[176,55, 34, 89, 61],
"rahul":[20,45, 67, 30, 88],
"sneha":[91,73, 50, 14, 62],
"karan": [38, 82, 47, 95,29],
}

#  to get a specific value 
ans = dict(sorted(marks.items(),key=lambda x :x [1][4]))
print(ans)

# what if data is not uniform 
# if this happen thrn the o/p will give yiu error

# #  to get the sum of thiese lists 
ans = dict(sorted(marks.items(),key=lambda x :sum (x[1])))
print(ans)

# to get the reverse of this list 
ans = dict(sorted(marks.items(),key=lambda x :sum (x[1]),reverse=True))
print(ans)