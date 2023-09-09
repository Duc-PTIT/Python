from math import *

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    maxx, minn = -1, 1000000
    for _ in range(n):
        b = list(map(int, input().split()))
        maxx = max(maxx, max(b))
        minn = min(minn, min(b))
        a.append(b)
    ans = maxx - minn
    ok = False

    for i in range(n):
        for j in range(m):
            if a[i][j] == ans and ok == False:
                print(ans)
                print('Vi tri [', i, '][', j, ']', sep = '')
                ok = True
            elif a[i][j] == ans:
                print('Vi tri [', i, '][', j, ']', sep='')
                ok = True
    if ok == False:
        print('NOT FOUND')