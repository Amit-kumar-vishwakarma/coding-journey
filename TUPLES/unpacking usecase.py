def min_max(lst):
    mini = min(lst)
    maxi= max(lst)
    return maxi, mini

ans1 ,ans2 = min_max([12,34,56,78,9,0])
print(f"maximum number={ans1}")
print(f"minimum number {ans2}")
