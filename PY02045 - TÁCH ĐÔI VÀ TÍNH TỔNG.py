s = input()
while len(s) > 1:
    mid = len(s) // 2
    s1 = s[0:mid]
    s2 = s[mid:len(s)]
    temp = int(s1) + int(s2)
    s = str(temp)
    print(s)
