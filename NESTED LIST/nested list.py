# 3x3 matrix
matrix = [
    [2, 3, 4],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix)
print (type(matrix))

# accesing of matrix

print(matrix[0])
print(matrix[1])
print(matrix[2])

# accesing specofic element 
print(matrix[0][2])
print(matrix[2][2])

# PRINTING ALL ELEMENT usimg FOR loop

for i in range (0,3):
    for j in range(0,3):
        print (matrix[i][j],end=" ")
    print()

    # sum of all element 
total =0
for i in range (0,3):
    for j in range(0,3):
        total = total + matrix [i][j]

print(total)

