import math
from functools import reduce

def factors(n):
	return len(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

A = [1]
i = 2
done = True

while done:
	A.append(A[-1]+i)
	i += 1
	done = factors(A[-1]) < 500

print(A[-1])
