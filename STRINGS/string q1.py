"""
Take a name as input from the user. Print its first character,
its last
character, and the total length of the name
"""


def print_details(name):
    first = name[0]
    last = name[-1]
    n = len(name)
    print(f"first= {first},last={last} and length is {n}")


print_details("amit_vishwakarma")
