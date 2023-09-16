f1 = open("DATA1.in", "r")
f2 = open("DATA2.in", "r")
se1 = set({})
se2 = set({})
a = []
for line in f1:
    b = list(map(str, line.lower().split()))
    a += b
se1 = set(a)
f1.close()
a.clear()
for line in f2:
    b = list(map(str, line.lower().split()))
    a += b
se2 = set(a)
f2.close()
ans1 = se1 - se2
ans2 = se2 - se1
for x in sorted(ans1):
    print(x, end = ' ')
print()
for x in sorted(ans2):
    print(x, end = ' ')