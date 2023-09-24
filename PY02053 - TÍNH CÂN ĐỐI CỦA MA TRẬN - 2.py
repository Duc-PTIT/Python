from itertools import product
from math import *

t = int(input())
a = []
for _ in range(t):
    b = list(map(int, input().split()))
    a.append(b)
k = int(input())
sum1 = 0
sum2 = 0

for i in range(t):
    for j in range(t - i - 1):
        sum1 += a[i][j]
    #     print(a[i][j], end = ' ')
    # print()

for i in range(t):
    for j in range(t-i, t):
        sum2 += a[i][j]
    #     print(a[i][j], end = ' ')
    # print()

if abs(sum1 - sum2) <= k:
    print('YES')
else: print('NO')
print(abs(sum1 - sum2))