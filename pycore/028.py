total = 4
current = 3
gap = 1
numnum = 1
while current < 1001**2:
    if numnum % 4 == 0:
        gap += 2
    current += gap + 1
    total += current
    numnum += 1

print(total)
