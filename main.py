a = [-10, -10, 15, 2, 100]
a.sort()
a = max(a[0] * a[1], a[len(a) - 2] * a[len(a) - 3]) * a[len(a) - 1]
print(a)
