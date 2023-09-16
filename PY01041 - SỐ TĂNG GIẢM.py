
def find(s):
    for i in range(0, len(s) -1):
        if s[i] == s[i+1]:
            return -1
        if s[i] > s[i + 1]:
            return i
    return -1
def solve(s):
    index = find(s)
    if index == -1:
        return "NO"
    else:
        for i in range(index, len(s) - 1):
            if s[i] < s[i+1]:
                return "NO"
        return "YES"

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        print(solve(input()))


