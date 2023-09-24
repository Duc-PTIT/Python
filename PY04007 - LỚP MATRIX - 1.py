t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    c = []
    for _ in range(m):
        b = [0] * n
        c.append(b)
    for i in range(n):
        for j in range(m):
            c[j][i] = a[i][j]
    d = []
    for _ in range(n):
        b = [0] * n
        d.append(b)
    for i in range(n):
        for j in range(n):
            for k in range(m):
                d[i][j] += a[i][k] * c[k][j]
    for i in range(n):
        for j in range(n):
            print(d[i][j], end=' ')
        print()
