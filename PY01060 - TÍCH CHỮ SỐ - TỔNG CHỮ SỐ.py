from math import *

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        summ, mul = 0, 1
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    mul *= int(s[i])
            else:
                summ += int(s[i])
        print(mul, summ)



