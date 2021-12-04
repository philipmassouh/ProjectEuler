def getSeqLen(start):
    value = start
    l = 1
    while value > 1:
        value = value / 2 if value % 2 == 0 else 3 * value + 1
        l += 1
    return l

longest = 0
for i in range(1000000):
    candidate = getSeqLen(i)
    if candidate > longest:
        longest = candidate

print(longest)