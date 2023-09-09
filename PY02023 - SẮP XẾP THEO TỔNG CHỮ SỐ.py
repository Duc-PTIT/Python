from math import *
from functools import cmp_to_key
def sumDi(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    return sum
def cmp(a, b):
    if sumDi(a) != sumDi(b):
        return sumDi(a) - sumDi(b)
    else: return a - b

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = cmp_to_key(cmp))
    for x in a:
        print(x, end = ' ')
    print()



