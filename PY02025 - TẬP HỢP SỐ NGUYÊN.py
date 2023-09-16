n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s1 = set(a)
s2 = set(b)
s3 = s1 & s2
s4 = s1 - s2
s5 = s2 - s1
for x in sorted(s3):
    print(x, end = ' ')
print()
for x in sorted(s4):
    print(x, end = ' ')
print()
for x in sorted(s5):
    print(x, end = ' ')
print()