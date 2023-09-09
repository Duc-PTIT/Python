from math import *
def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = input()
    s = ''
    for i in range(len(n)-1, len(n) - 1 - 4, -1):
        s = n[i] + s
    if prime(int(s)):
        print('YES')
    else: print('NO')
