from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check(s):
    for i in range (len(s)):
        if((s[i] == '2' or s[i] == '3' or s[i] == '5' or s[i] == '7') and prime(i) == False) :
            return False
        elif (s[i] != '2' and s[i] != '3' and s[i] != '5' and s[i] != '7' and prime(i) == True):
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        if check(s):
            print('YES')
        else: print('NO')



