import math

n = 1000000
A = [True for i in range(1, n + 1)]
for i in range(2, n):
    if A[i]:
        for j in range(i**2, n, i):
            A[j] = False

i = 1
j = 0
while j <= 10001:
    if A[i]:
        j += 1
    i += 1

print(i - 1)
