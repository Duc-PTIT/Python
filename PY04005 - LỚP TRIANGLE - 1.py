from math import *
from sys import stdin

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        return sqrt(pow(self.x-other.x,2) + pow(self.y - other.y,2))

if __name__ == '__main__':
    a = []
    for x in stdin:
        for i in x.split():
            a.append(i)
    t = int(a[0])
    i = 0
    for _ in range(t):
        p1 = Point(float(a[i + 1]), float(a[i + 2]))
        p2 = Point(float(a[i + 3]), float(a[i + 4]))
        p3 = Point(float(a[i + 5]), float(a[i + 6]))
        AB = p1.distance(p2)
        AC = p1.distance(p3)
        BC = p2.distance(p3)
        if (AB + BC) <= AC or (AB + AC) <= BC or (AC + BC) <= AB:
            print('INVALID')
        else:
            print('%.3f' % (AB + BC + AC))
        i += 6