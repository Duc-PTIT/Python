from math import *

def tn(n):
    s = str(n)
    if len(s) == 1:
        return False
    temp = s[::-1]
    return temp == s

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    maxx = -1
    for i in range(n):
        for j in range(m):
            if tn(a[i][j]):
                maxx = max(maxx, a[i][j])
    if maxx == -1:
        print('NOT FOUND')
    else:
        print(maxx)
        for i in range(n):
            for j in range(m):
                if a[i][j] == maxx:
                    print('Vi tri [',i, '][', j, ']', sep = '')