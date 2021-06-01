import math
from functools import reduce

def num_fac(n):
	if n == 0:
		return 0
	return len(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

# generate primes under 1000
primes = []
num = 2
while num < 1000:
	if num_fac(num) == 2:
		primes.append(num)
	num += 1

maxseries = (1, 1, 1)
for a in range(-1000, 1001, 1):
	for b in primes:
		n = 0
		while num_fac(abs(n**2 + a*n + b)) == 2:
			n += 1
		if n > maxseries[0]:
			  maxseries = (n, a, b)

print(maxseries)