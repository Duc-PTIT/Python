t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = dict({})
    for x in a:
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    for x, y in d.items():
        if y % 2 == 1:
            print(x)
            break