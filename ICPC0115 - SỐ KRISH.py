def fac(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

def solve(s):
    x = int(s)
    ans = 0
    for i in s:
        ans += fac(int(i))
    return ans == x

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        if solve(s):
            print('Yes')
        else: print('No')


