from math import *

n, m = map(int, input().split())
for x in range(n, m - 1):
    for y in range(x + 1, m):
        for z in range(y + 1, m + 1):
            if gcd(x, y) == 1 and gcd(y, z) == 1 and gcd(x, z) == 1:
                print('(', x, ', ', y, ', ', z, ')', sep = '')
