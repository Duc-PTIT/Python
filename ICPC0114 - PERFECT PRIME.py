from math import *

def prime(n):
    if(n < 2):
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check1(n):
    for x in n:
        if(x != '2' and x != '3' and x != '5' and x != '7'):
            return False
    return True

def check2(n):
    s = n[::-1]
    if(prime(int(s))):
        return True
    return False

def check3(n):
    sum = 0
    for x in n:
        sum += int(x)
    if(prime(sum)):
        return True
    return False
t = int(input())
for _ in range(t):
    s = input()
    if check1(s) and check2(s) and check3(s):
        print('Yes')
    else: print('No')

