f = open("DATA2.in", "r")
se = set({})
for x in f:
    if x[-1] == '\n':
        x = x[:len(x)-1]
    se.add(x.lower())
for x in sorted(se):
    print(x)
