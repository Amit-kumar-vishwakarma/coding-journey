text = "programing"
n = len(text)
for i in range(0,n):
    print(text[i])

    #  to count how many o's are there 
    text = "programing"
n = len(text)
total = 0
for i in range(0,n):
    if text[i]=="g"or text[i]=="G":
        total +=1
print(total)       

#  METHOD 2 
for char in text:
    print(char)

    # enumerate
    for ind, ch in enumerate(text):
        print(f"ind={ind}and ch {ch}")