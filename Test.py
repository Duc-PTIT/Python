t = int(input())
while t > 0:
    t -= 1
    n, m, l = map(int, input().split())
    a = [[0] * m] * n
    for i in range(n):
        a[i] = [int(x) for x in input().split()]
        p = n - l + 1
        q = m - l + 1
    for i in range(0, n):
        for j in range(0, m):
            if i == 0 or j == 0:
                if j == 0:
                    a[i][j] += a[i-1][j]
                if i == 0:
                    a[i][j] += a[i][j-1]
            else:
                a[i][j] += a[i][j-1] + a[i-1][j] - a[i-1][j-1]

    for i in range(0, p):
        for j in range(0, q):
            if i == 0 and j == 0:
                print(int(a[i + l - 1][j + l - 1] / (l * l)), end = ' ')
            elif i == 0:
                print(int((a[i + l - 1][j + l - 1] - a[i + l - 1][j - 1]) / (l * l)), end = ' ')
            elif j == 0:
                print(int((a[i + l - 1][j + l - 1] - a[i - 1][j + l - 1]) / (l * l)), end = ' ')
            else:
                print(int((a[i + l - 1][j + l - 1] - a[i - 1][j + l - 1] - a[i + l - 1][j - 1]
                          + a[i-1][j-1]) / (l * l)), end=' ')
        print()