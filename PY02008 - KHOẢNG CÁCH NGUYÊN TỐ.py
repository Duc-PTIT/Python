from math import *

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(k, end = ' ')
    start = 2
    while n != 0:
        for i in range(start, 8000):
            if prime(i):
                k += i
                print(k, end = ' ')
                start = i + 1
                break;
        n -= 1



