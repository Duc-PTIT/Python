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
        a, b = map(int, input().split())
        c = gcd(a,b)
        ans = 0
        while c != 0:
            ans += c % 10
            c //= 10
        if prime(ans):
            print('YES')
        else: print('NO')


