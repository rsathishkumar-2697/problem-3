n = int(input())
result = []
f = 1
k = 0
if n%2 == 0:
    for i in range(n-1):
        f += k
        result.append(f)
        k = 2
else:
    for i in range(n):
        f += k
        result.append(f)
        k = 2

print(*result)