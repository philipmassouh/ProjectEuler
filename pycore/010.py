import math

n = 2000001
A = [True for i in range(1, n + 1)]

for i in range(2, int(math.ceil(n**0.5))):
    if A[i]:
        for j in range(i**2, n, i):
            A[j] = False

s = 0
for k in range(2, n):
    if A[k]:
        s += k

print(s)
