a = []
while len(a) < 10:
    a += list(map(int, input().split()))
se = set({})
for x in a:
    temp = x % 42
    se.add(temp)
print(len(se))