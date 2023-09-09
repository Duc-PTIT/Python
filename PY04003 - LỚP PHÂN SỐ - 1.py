from math import *

class Fraction:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def rutgon(self):
        x = gcd(self.tu, self.mau)
        self.tu = self.tu // x
        self.mau = self.mau // x
    def show(self):
        print(self.tu, '/', self.mau, sep = '')

if __name__ == '__main__':
    tu, mau = map(int, input().split())
    f = Fraction(tu, mau)
    f.rutgon()
    f.show()