from math import *

def sumdi(n):
    s = 0
    for x in n:
        s += int(x)
    return str(s)

def check(n):
    if len(n) == 1:
        return False
    temp = n[::-1]
    return temp == n

t = int(input())
for _ in range(t):
    n = input()
    if check(sumdi(n)):
        print('YES')
    else: print('NO')



