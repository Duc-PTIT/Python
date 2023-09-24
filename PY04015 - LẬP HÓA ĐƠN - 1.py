from functools import cmp_to_key

class KhachHang:
    def __init__(self, id, ten, bd, kt):
        self.id = "KH{:02d}".format(id)
        self.ten = ten
        self.bd = bd
        self.kt = kt
    def solve(self):
        ans = self.kt - self.bd
        if ans <= 50:
                return ans * 100 * 1.02
        elif ans <= 100:
            return (100 * 50 + (ans - 50) * 150) * 1.03
        else:
            return (100 * 50 + 150 * 50 + (ans - 100) * 200) * 1.05
    def show(self):
        print(self.id, self.ten, "%.0f" % self.solve())

def cmp(a, b):
    if a.solve() != b.solve():
        return b.solve() - a.solve()
    return a.id - b.id

if __name__ == '__main__':
    t = int(input())
    cnt = 1
    a = []
    for _ in range(t):
        x = KhachHang(cnt, input(), int(input()), int(input()))
        cnt += 1
        a.append(x)
    a.sort(key = cmp_to_key(cmp))
for x in a:
    x.show()



