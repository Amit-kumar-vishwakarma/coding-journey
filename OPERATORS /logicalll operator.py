# logical operators are
# AND OR NOT

chemistry = 50
english = 45
maths = 47

## print true if pass in every subjects
print(chemistry > 40 and english > 40 and maths > 40)


# print true if pass in anysubjects(kisi ek me bhi paas matlab paas)
print(chemistry > 40 or english > 50 or maths > 50)

# print false becaude the values are complemented
print(not (chemistry > 40 and english > 40 and maths > 40))
