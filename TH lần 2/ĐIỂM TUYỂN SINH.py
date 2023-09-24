from functools import cmp_to_key
class ThiSinh:

    def __init__(self, id, ten, diem, dt, kv):
        self.id =  'TS{:02d}'.format(id)
        a = ten.split()
        self.ten = " ".join(a)
        self.ten = self.ten.title()
        self.diem = diem
        self.dt = dt
        self.kv = kv
        if self.dt != "Kinh":
            self.diem += 1.5
        if self.kv == 1:
            self.diem += 1.5
        if self.kv == 2:
            self.diem += 1

    def show(self):

        if self.diem >= 20.5:
            tt = 'Do'
        else: tt = 'Truot'
        print(self.id, self.ten, '%.1f' % self.diem, tt)

def cmp(a, b):
    if a.diem != b.diem:
        return b.diem - a.diem
    else:
        if a.id > b.id:
            return 1
        else:
            return -1

if __name__ == '__main__':
    t = int(input())
    a = []
    cnt = 1;
    for _ in range(t):
        a.append(ThiSinh(cnt, input(), float(input()), input(), int(input())))
        cnt += 1
    a.sort(key = cmp_to_key(cmp))
    for x in a:
        x.show()