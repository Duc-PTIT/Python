from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    s = 0
    for x in n:
        s += int(x)
    return prime(s)

t = int(input())
for _ in range(t):
    n = input()
    if check(n):
        print('YES')
    else: print('NO')



