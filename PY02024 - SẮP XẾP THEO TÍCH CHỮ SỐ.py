from math import *

def Mul(n):
    sum = 1
    while n != 0:
        sum *= n % 10
        n //= 10
    return sum

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = lambda x : (Mul(x), x))
    for x in a:
        print(x, end = ' ')
    print()



