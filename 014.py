# longest collatz sequence
# consider evens
max = (0, 0)
start = 0
for n in range(0, 1000000):
    start = n
    i = 0
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        i += 1
    if i > max[0]:
        max = (i, start)

print(max)
