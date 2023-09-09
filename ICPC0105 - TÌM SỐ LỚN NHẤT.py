t = int(input())
for _ in range(t):
    s = input()
    temp = ''
    for x in s:
        if x.isalpha():
            temp += ' '
        else: temp += x
    a = map(int, temp.split())
    print(max(a))