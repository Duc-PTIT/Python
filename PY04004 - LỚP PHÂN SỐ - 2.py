from math import *

class Fraction:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def rutgon(self):
        x = gcd(self.tu, self.mau)
        self.tu = self.tu // x
        self.mau = self.mau // x

    def tong(self, a):
        bcnn = self.mau // gcd(self.mau, a.mau) * a.mau
        self.tu = self.tu * (bcnn // self.mau)
        a.tu = a.tu * (bcnn // a.mau)
        self.tu += a.tu
        self.mau = bcnn
        return self
    def show(self):
        print(self.tu, '/', self.mau, sep = '')

if __name__ == '__main__':
    tu1, mau1, tu2, mau2 = map(int, input().split())
    f1 = Fraction(tu1, mau1)
    f2 = Fraction(tu2, mau2)
    f1.rutgon()
    f2.rutgon()
    f = f1.tong(f2)
    f.rutgon()
    f.show()