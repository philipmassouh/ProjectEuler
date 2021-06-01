import math

sum = 0
A = [int(x) for x in str(2**1000)]
for x in range(0, len(A)):
    sum += A[x]

print(sum)