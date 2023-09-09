from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        cnt = 0
        for x in range(n):
            if gcd(n, x) == 1:
                cnt += 1
        if prime(cnt):
            print('YES')
        else: print('NO')