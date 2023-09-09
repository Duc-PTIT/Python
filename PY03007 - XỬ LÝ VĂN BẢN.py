from sys import stdin
c = []
for line in stdin:
    b = list(map(str, line.strip().split()))
    c.append(b)
a = [x for small_list in c for x in small_list]
ok = True
for x in a:
    if ok == True:
        if (x[-1] == '.' or x[-1] == '?' or x[-1] == '!'):
            s = ""
            for i in range(len(x)-1):
                s += x[i]
            print(s.title())
        else:
            print(x.title(), end = ' ')
            ok = False
    else:
        if (x[-1] == '.' or x[-1] == '?' or x[-1] == '!'):
            s = ""
            for i in range(len(x)-1):
                s += x[i]
            print(s.lower())
            ok = True
        else:
            print(x.lower(), end = ' ')
