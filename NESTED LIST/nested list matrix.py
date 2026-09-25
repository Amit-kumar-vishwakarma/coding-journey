# 4x5 co;umn matrix
# print this matrix
matrix = [
    [2, 3, 4, 5, 6],
    [9, 8, 7, 6, 5],
    [1, 3, 5, 7, 9],
    [2, 3, 5, 7, 9],
]

rows =len(matrix)
colums = len(matrix[0])
for i in range(0,rows):
    for j in range (0,colums):
        print (matrix[i][j],end=" ")
    print()

