f = open("DATA.in", "r")
a = []
b = []
for line in f:
    a += line.split()
for x in a:
    ok = True
    if len(x) < 10 and x.isdigit():
        continue
    else:
        b.append(x)
b.sort()
print(*b)