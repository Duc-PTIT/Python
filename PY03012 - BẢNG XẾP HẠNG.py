from functools import cmp_to_key
class SinhVien:
    def __init__(self, ten, sobai, luotsub):
        self.ten = ten
        self.sobai = sobai
        self.luotsub = luotsub

    def show(self):
        print(self.ten, self.sobai, self.luotsub)

def cmp(a, b):
    if a.sobai != b.sobai:
        return b.sobai - a.sobai
    else:
        if a.luotsub != b.luotsub:
            return a.luotsub - b.luotsub
        else:
            if a.ten > b.ten:
                return 1
            else: return -1

if __name__ == '__main__':
    t = int(input())
    a = []
    for _ in range(t):
        x = input()
        y, z = map(int, input().split())
        a.append(SinhVien(x, y, z))
    a.sort(key = cmp_to_key(cmp))
    for x in a:
        x.show()