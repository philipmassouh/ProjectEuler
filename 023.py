import math
from functools import reduce

def abundant(n):
	return sum(set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))) - n > n

#generate abundants
abundants = []
for x in range(12,28124):
	if (abundant(x)):
		abundants.append(x)

total = 0
# go through all the integers 
for x in range(1,28123):
	add = True
	for y in abundants: 
		if x > y and abundant(x-y):
			add = False
			break
	if add:
		total += x

print(total)