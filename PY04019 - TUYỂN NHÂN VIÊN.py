from functools import cmp_to_key

class SinhVien:
    def __init__(self, id, ten, d1, d2):
        self.id = 'TS0' + str(id)
        self.ten = ten
        self.d1 = d1
        self.d2 = d2

    def dtb(self):
        if self.d1 > 10:
            self.d1 /= 10
        if self.d2 > 10:
            self.d2 /= 10
        return (self.d1 + self.d2) / 2
    def show(self):
        x = self.dtb()
        if x > 9.5:
            s = "XUAT SAC"
        elif x >= 8:
            s = "DAT"
        elif x >= 5:
            s = "CAN NHAC"
        else:
            s = "TRUOT"
        print(self.id, self.ten, "%.2f" % x, s)

def cmp(a, b):
    return b.dtb() - a.dtb()

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    a = []
    for _ in range(t):
        x = SinhVien(cnt, input(), float(input()), float(input()))
        cnt += 1
        a.append(x)
    a.sort(key = cmp_to_key(cmp))
    for x in a:
        x.show()