from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def sumdi(n):
    s = 0
    for x in n:
        s += int(x)
    return s
def check(s):
    for i in range(len(s)):
        if i % 2 == 0 and int(s[i]) % 2 == 1 :
            return False
        elif i % 2 == 1 and int(s[i]) % 2 == 0:
            return False
    return prime(sumdi(s))


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        if check(s):
            print('YES')
        else:
            print('NO')



