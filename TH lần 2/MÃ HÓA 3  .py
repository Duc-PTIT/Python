sample = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def rotate(s):
    res = ''
    offset = 0
    for i in s:
        offset = offset + ord(i) - ord('A')
    offset = offset % 26
    for i in range(0, len(s)):
        tmp = (offset + (ord(s[i]) - ord('A'))) % 26
        res = res + sample[int(tmp)]
    return res
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        s1 = s[0:len(s)//2]
        s2 = s[len(s)//2:len(s)]
        s1 = rotate(s1)
        s2 = rotate(s2)
        for i in range(0, len(s1)):
            vt = ord(s1[i]) - ord('A')
            offset = (vt + (ord(s2[i]) - ord('A'))) % 26
            print(sample[offset], end = '')
        print()
