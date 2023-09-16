from functools import cmp_to_key
class Cathi:
    def __init__(self, id, date, time, room):
        self.id = 'C{:03d}'.format(id)
        self.date = date
        self.time = time
        self.room = room
    def show(self):
        print(self.id, self.date, self.time, self.room, sep = " ")

def cmp(a, b):
    if a.date != b.date:
        if a.date > b.date:
            return 1
        else: return -1
    else:
        if a.time != b.time:
            if a.time > b.time:
                return 1
            else:
                return -1
        else:
            if a.id > b.id:
                return 1
            else:
                return -1

if __name__ == '__main__':
    f = open("DATA2.in", "r")
    t = int(f.readline())
    cnt = 1
    a = []
    for _ in range(t):
        date = f.readline()
        if date[-1] == '\n':
            date = date[:len(date) - 1]
        time = f.readline()
        if time[-1] == '\n':
            time = time[:len(time) - 1]
        room = f.readline()
        if room[-1] == '\n':
            room = room[:len(room) - 1]

        x =  Cathi(cnt, date, time, room)
        cnt += 1
        a.append(x)
    a.sort(key = cmp_to_key(cmp))
    for x in a:
        x.show()

