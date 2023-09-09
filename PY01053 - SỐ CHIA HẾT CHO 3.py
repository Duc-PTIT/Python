
def solve(s):
    x = int(s)
    ans = 0
    for i in s:
        ans += int(i)
    return ans

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        if solve(s) % 3 == 0:
            print('YES')
        else: print('NO')


