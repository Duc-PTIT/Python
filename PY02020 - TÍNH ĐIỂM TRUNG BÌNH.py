t = int(input())
a = list(map(float, input().split()))
maxx = max(a)
minn = min(a)
cnt = 0
sum = 0
for x in a:
    if x != maxx and x != minn:
        sum += x
        cnt += 1
print('%.2f' % (sum / cnt))