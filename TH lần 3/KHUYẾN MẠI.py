class calc:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
data = []
for i in range(n):
    data.append(calc(a[i], b[i]))
data.sort(reverse=True, key = lambda x: x.b - x.a)
for x in data:
    print(x.a, x.b)
sum = 0
for i in range(k):
    sum += data[i].a
for i in range(k, n):
    if(data[i].b > data[i].a) :
        sum += data[i].a
    else:
        sum += data[i].b
print(sum)
