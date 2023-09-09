def check1(n):
    temp = n[::-1]
    return temp == n
def check2(n):
    for x in n:
        if int(x) % 2 != 0:
            return False
    return True

t = int(input())
for _ in range(t):
    n = int(input())
    for x in range(22, n, 2):
        s = str(x)
        if check1(s) and check2(s) and len(s) % 2 == 0:
            print(s, end = ' ')
    print()

