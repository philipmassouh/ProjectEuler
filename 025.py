a = 1
b = 2
c = 0
index = 0
while True:
	c = a + b
	a = b
	b = c
	index += 1
	if len(str(c)) > 1000:
		break

print(index-2)
