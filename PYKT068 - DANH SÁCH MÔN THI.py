class MonHoc:
    def __init__(self, ma, ten, hinhthuc):
        self.ma = ma
        self.ten = ten
        self.hinhthuc = hinhthuc

    def show(self):
        print(self.ma, self.ten, self.hinhthuc)

if __name__ == '__main__':
    t = int(input())
    a = []
    for _ in range(t):
        a.append(MonHoc(input(), input(), input()))
    a.sort(key = lambda x : x.ma)
    for x in a:
        x.show()