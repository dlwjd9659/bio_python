a = [3, 1, 1, 2, 0, 0, 2, 3, 3]
a.sort()
d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1



print(d)
