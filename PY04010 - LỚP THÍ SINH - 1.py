from math import *

class Sinhvien:
    def __init__(self, name, dob, d1, d2, d3):
        self.name = name
        self.dob = dob
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
    def show(self):
        summ = self.d1 + self.d2 + self.d3
        print(self.name, self.dob, '%.1f' % summ)


if __name__ == '__main__':
    name = input()
    dob = input()
    d1 = float(input())
    d2 = float(input())
    d3 = float(input())
    x = Sinhvien(name, dob, d1, d2, d3)
    x.show()