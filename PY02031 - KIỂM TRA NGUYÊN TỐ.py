from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    m, n = map(int, input().split())
    a = []
    for _ in range(m):
        b = list(map(int, input().split()))
        a.append(b)
    for i in range(m):
        for j in range(n):
            if prime(a[i][j]):
                a[i][j] = 1
            else: a[i][j] = 0
    for i in range(m):
        for j in range(n):
            print(a[i][j], end = ' ')
        print()




