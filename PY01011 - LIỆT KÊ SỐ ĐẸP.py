def tn(n):
    s = str(n)
    if len(s) % 2 == 1:
        return False
    else:
        for x in s:
            if x != '0' and x != '2' and x != '4' and x != '6' and x != '8':
                return False
        if s == s[::-1]:
            return True
        return False

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        for i in range(22, n, 2):
            if tn(i):
                print(i, end=' ')
        print()

