
def solve(s):
    x = int(s)
    ans = 1
    for i in s:
        if i == '0':
            continue
        else: ans *= int(i)
    return ans

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        print(solve(s))


