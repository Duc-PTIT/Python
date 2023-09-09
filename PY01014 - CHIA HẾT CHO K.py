from math import *

if __name__ == '__main__':
    a, k, n = map(int, input().split())
    b = []
    i = k - (a % k)
    n = n - a

    while i <= n:
        b.append(i)
        i += k
    if len(b) == 0:
        print('-1')
    else:
        for x in b:
            print(x, end = ' ')