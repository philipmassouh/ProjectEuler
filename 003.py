# find the largest prime factor of 600851475143
import math

n = int(math.ceil(600851475143**0.5))
A = [True for i in range(1, n+1)]
for i in range(2, int(math.ceil(n))):
    if A[i]:
        for j in range(i**2, n, i):
            A[j] = False

for x in range(len(A)-1, 1, -1):
    if A[x] and 600851475143 % x == 0:
        break

print(x)

