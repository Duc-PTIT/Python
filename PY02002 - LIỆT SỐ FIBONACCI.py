t = int(input())
fibo = []
fibo.append(1)
fibo.append(1)
f1, f2 = 1, 1
for i in range(2,92):
    fibo.append(fibo[i-1] + fibo[i-2])
for _ in range(t):
    n, m = map(int, input().split())
    for i in range(n-1, m):
        print(fibo[i], end = ' ')
    print()

