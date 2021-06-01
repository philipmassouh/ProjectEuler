import math
f = str(math.factorial(100))
sum = 0
for x in range(0, len(f)):
	sum += int(f[x])

print(sum)
