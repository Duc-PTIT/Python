from math import *

cnt = 0
n, k = map(int, input().split())
for x in range(int(pow(10,k-1)), int(pow(10,k))):
    if gcd(n, x) == 1:
        print(x, end = ' ')
        cnt += 1
        if(cnt == 10):
            cnt = 0
            print()

