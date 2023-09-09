from math import *

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        d = dict({})
        a.sort()
        for x in a:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
        maxx = max(d.values())
        if(maxx <= n/2):
            print('NO')
        else:
            for x, y in d.items():
                if y == maxx:
                    print(x)
                    break;





