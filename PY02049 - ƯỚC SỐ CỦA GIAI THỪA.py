t = int(input())
for _ in range(t):
    cnt = 0
    n, k = map(int, input().split())
    x = k
    while x <= n:
        temp = x
        while temp % k == 0:
            temp //= k
            cnt += 1
        x += k
    print(cnt)
