marks ={"math":85,"science":92,"english":60,"hindi":78}
#  to get the tuple
# print (marks.items())

ans = sorted(marks.items(),key= lambda x: x[1])
print(ans)

# to sort a dictionary we need to convert that in dict 
ans = dict (sorted(marks.items(),key= lambda x: x[1]))
print(ans)