from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for _ in range(n):
        b = list(map(int, input().split()))
        a.append(b)
    maxx = -1
    for i in range(n):
        for j in range(m):
            if prime(a[i][j]):
                maxx = max(maxx, a[i][j])
    if maxx == -1:
        print('NOT FOUND')
    else:
        print(maxx)
        for i in range(n):
            for j in range(m):
                if a[i][j] == maxx:
                    print('Vi tri [',i, '][', j, ']', sep = '')