from math import *

while True:
    a = list(map(int, input().split()))
    if a == [0, 0, 0, 0]:
        break
    cnt = 0
    while len(set(a)) > 1:
        b = [0] * 4
        for i in range(0, 3):
            b[i] = abs(a[i] - a[i + 1])
        b[3] = abs(a[3] - a[0])
        cnt += 1
        a = b
    print(cnt)