# def square(num):
#     return num*num

# square= lambda num: num*num

# print(square(100))

#  return true if age= 18 else false


def is_adult(age):
    if age >= 18:
        return True
    return False


is_adult = lambda age: True if age >= 18 else False

print(is_adult(18))
print(is_adult(8))
