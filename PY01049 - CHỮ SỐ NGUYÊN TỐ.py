from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    cnt = 0
    for x in n:
        if(x == '2' or x == '3' or x == '5' or x == '7'):
            cnt += 1
    return cnt > len(n) - cnt

t = int(input())
for _ in range(t):
    n = input()
    if check(n) and prime(len(n)):
        print('YES')
    else: print('NO')



