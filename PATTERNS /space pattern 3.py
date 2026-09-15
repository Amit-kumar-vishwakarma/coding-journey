"""
                1 
            1   2   3
        1   2   3   4   5 
    1   2   3   4   5   6   7  
1   2   3   4   5   6   7   8  9 
    1   2   3   4   5   6   7 
         1  2   3   4   5 
            1   2   3
                1 
"""



# Part 1: Upper Pyramid (Upar ka hissa)
for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print(k, end=" ")
    print()

# Part 2: Lower Inverted Pyramid (Neeche ka hissa)
for i in range(4, 0, -1):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for k in range(1, i * 2):
        print(k, end=" ")
    print()



     