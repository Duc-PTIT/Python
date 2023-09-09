n = int(input())
C = []
L = []
ans = []
while n != len(L) + len (C):
    for i in input().split():
        ans.append(int(i))
        if int (i) % 2 == 1:
            L.append(int (i))
        else:
            C.append(int(i))
C.sort()
L.sort(reverse = True)
i, j = 0, 0
for x in ans:
    if x % 2 == 0:
        print(C[i], end = ' ')
        i += 1
    else:
        print(L[j], end = ' ')
        j += 1