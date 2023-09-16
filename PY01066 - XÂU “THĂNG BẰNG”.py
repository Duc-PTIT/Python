from math import *

def check(s):
    t = s[::-1]
    for i in range(1,len(s)):
        if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(t[i]) - ord(t[i-1])):
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        if check(s):
            print('YES')
        else: print('NO')
