n, k = map(int, input().split())
a = list(map(int, input().split()))
d = dict({})
for x in a:
    if x in d:
        d[x] += 1
    else: d[x] = 1
max1, max2 = -1, -1
for x in d.values():
    if x > max1:
        max2= max1
        max1 = x
    elif x < max1 and x > max2:
        max2 = x
if max2 == -1:
    print('NONE')
else:
    for x, y in d.items():
        if y == max2:
            print(x)
            break