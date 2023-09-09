from math import *

def check(s):
    for i in range(1, len(s), 2):
        if s[i] != '0':
            return False
    return True

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        summ, mul = 0, 1
        if check(s):
            mul = 0
            for i in range(0, len(s), 2):
                summ += int(s[i])
        else:
            for i in range(len(s)):
                if i % 2 == 0:
                    summ += int(s[i])
                else:
                    if s[i] != '0':
                        mul *= int(s[i])
        print(summ, mul)



