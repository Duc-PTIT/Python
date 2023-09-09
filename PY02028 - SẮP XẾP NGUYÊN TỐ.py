from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for x in a:
        if prime(x):
            b.append(x)
    b.sort()
    i = 0
    for x in a:
        if prime(x):
            print(b[i], end = ' ')
            i += 1
        else: print(x, end = ' ')