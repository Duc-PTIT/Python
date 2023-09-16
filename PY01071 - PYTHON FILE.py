def check(s):
    s = s.lower()
    for x in s:
        if ord(x) < ord('a') or ord(x) > ord('z') :
            if x != '_' and x != '.':
                return False
    if ".py" in s:
        return True
    return False

if __name__ == '__main__':
    s = input()
    if check(s):
        print('yes')
    else: print('no')