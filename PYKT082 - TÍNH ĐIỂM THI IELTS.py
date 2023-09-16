def getDiem(n):
    if n >= 39:
        return 9.0
    elif n >= 37:
        return 8.5
    elif n >= 35:
        return 8.0
    elif n >= 33:
        return 7.5
    elif n >= 30:
        return 7.0
    elif n >= 27:
        return 6.5
    elif n >= 23:
        return 6.0
    elif n >= 20:
        return 5.5
    elif n >= 16:
        return 5.0
    elif n >= 13:
        return 4.5
    elif n >= 10:
        return 4.0
    elif n >= 7:
        return 3.5
    elif n >= 5:
        return 3.0
    elif n >= 3:
        return 2.5

t = int(input())
for _ in range(t):
    b = list(map(float, input().split()))
    sum = 0
    lis = getDiem(b[0])
    rea = getDiem(b[1])
    for i in range (2, len(b)):
        sum += b[i]
    sum += lis + rea
    temp = sum
    sum /= 4
    temp //= 4
    if sum - temp >= 0.75:
        sum = temp + 1
    elif sum - temp >= 0.25:
        sum = temp + 0.5
    else: sum = temp
    print('%.1f' % sum)
