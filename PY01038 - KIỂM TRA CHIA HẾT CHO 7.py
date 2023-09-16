def Solve(s):
    cnt = 0
    sum = int(s)
    while sum % 7 != 0:
        sum += int(s[::-1])
        s = str(sum)
        cnt += 1
        if cnt > 1000:
            return -1
    return sum


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        print(Solve(s))
