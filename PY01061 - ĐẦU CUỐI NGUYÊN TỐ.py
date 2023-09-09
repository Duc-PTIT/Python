from calendar import prcal
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
        s = input()
        s1 = ""
        s2 = ""
        for i in range(0,3,1):
            s1 += s[i]
        for i in range(len(s) - 1, len(s) - 4, -1):
            s2 = s[i] + s2
        if prime(int(s1)) and prime(int(s2)):
            print('YES')
        else: print('NO')



