from math import *

t = int(input())
for _ in range(t):
    s = input()
    temp = s[::-1]
    n1 = int(s)
    n2 = int(temp)
    if gcd(n1, n2) == 1:
        print('YES')
    else: print('NO')

