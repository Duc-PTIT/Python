
class NhanVien:
    def __init__(self, ma, ten, luong, ngay):
        self.ma = ma
        self.ten = ten
        self.luong = luong * 1000
        self.ngay = ngay
        self.phong = d[self.ma[3:]]

    def solve(self):
        nhom = self.ma[0:1]
        nam = int(self.ma[1:3])
        phongban = self.ma[3:]
        heso = 0
        if nhom == "A":
            if nam >= 1 and nam <= 3:
                heso = 10
            if nam >= 4 and nam <= 8:
                heso = 12
            if nam >= 9 and nam <= 15:
                heso = 14
            if nam >= 16:
                heso = 20
        elif nhom == "B":
            if nam >= 1 and nam <= 3:
                heso = 10
            if nam >= 4 and nam <= 8:
                heso = 11
            if nam >= 9 and nam <= 15:
                heso = 13
            if nam >= 16:
                heso = 16
        elif nhom == "C":
            if nam >= 1 and nam <= 3:
                heso = 9
            if nam >= 4 and nam <= 8:
                heso = 10
            if nam >= 9 and nam <= 15:
                heso = 12
            if nam >= 16:
                heso = 14
        else:
            if nam >= 1 and nam <= 3:
                heso = 8
            if nam >= 4 and nam <= 8:
                heso = 9
            if nam >= 9 and nam <= 15:
                heso = 11
            if nam >= 16:
                heso = 13
        self.tong = heso * self.luong * self.ngay

    def show(self):
        print(self.ma, self.ten, self.phong, self.tong)

if __name__ == '__main__':
    a = []
    d = dict({})
    t1 = int(input())
    for _ in range(t1):
        s = input()
        kh = s[:2]
        ten = s[3:]
        d[kh] = ten
    t2 = int(input())
    for _ in range(t2):
        x = NhanVien(input(), input(), int(input()), int(input()))
        x.solve()
        a.append(x)
    for x in a:
        x.show()


