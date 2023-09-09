from math import *

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print('1 *', end = ' ')
        for i in range(2, isqrt(n) + 1):
            cnt = 0
            if n % i == 0:
                while n % i == 0:
                    cnt += 1
                    n //= i
                if n != 1:
                    print(i, '^', cnt, ' *', sep='', end=' ')
                else:
                    print(i, '^', cnt, sep='')
        if n != 1:
            print(n, '^1', sep='')



