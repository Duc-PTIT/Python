t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    maxx = max(a)
    minn = min(a)
    b = [0] * 1001
    cnt = 0
    for i in range(minn, maxx + 1):
        if i not in a:
            cnt += 1
    print(cnt)
