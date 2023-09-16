n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s1 = set(a)
s2 = set(b)
if s1 == s2:
    print('YES')
else: print('NO')