""" split(): break string into list
join(): combine list into strings
"""
text= "amit is working in google"

print(text.split())

print(text.split("i")) 
print(len(text.split()))

# join
my_list= ["a","m","i","t"]
ans = ("".join(my_list))
print(ans)
print(type(ans))