
class SinhVien:
    def __init__(self, ma, ten, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10):
        self.ma = 'HS{:02d}'.format(ma)
        self.ten = ten
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
        self.d4 = d4
        self.d5 = d5
        self.d6 = d6
        self.d7 = d7
        self.d8 = d8
        self.d9 = d9
        self.d10 = d10
        self.dtb = (2*d1 + 2*d2 + d3 + d4 + d5 + d6 + d7 + d8+ d9 + d10)/12
        self.dtb += 0.01
        if self.dtb >= 9:
            self.hocluc = "XUAT SAC"
        elif self.dtb >= 8:
            self.hocluc = "GIOI"
        elif self.dtb >= 7:
            self.hocluc = "KHA"
        elif self.dtb >= 5:
            self.hocluc = "TB"
        else: self.hocluc = "YEU"

    def show(self):
        print(self.ma, self.ten, "%.1f" % self.dtb, self.hocluc)

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    a = []
    for _ in range(t):
        name = input()
        d1, d2, d3, d4, d5, d6, d7, d8, d9, d10 = map(float, input().split())
        a.append(SinhVien(cnt, name, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10))
        cnt += 1
    a.sort(key = lambda x: (-x.dtb, x.ma))
    for x in a:
        x.show()
