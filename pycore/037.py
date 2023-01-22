import math


def isprime(n):
    if n == 1:
        return False
    top = math.ceil(n**0.5) + 1
    for x in range(2, top):
        if n % x == 0 and x != n:
            return False
    return True


def istrunc(n):
    valid = isprime(n)
    # remove from left side
    temp = str(n)
    while len(temp) > 1 and valid:
        temp = temp[1:]
        valid = isprime(int(temp))
    # remove from right side
    temp = str(n)
    while len(temp) > 1 and valid:
        temp = temp[:-1]
        valid = isprime(int(temp))
    return valid


trunc = 0
n = 11
total = 0
while trunc < 11:
    if istrunc(n):
        print(n)
        total += n
        trunc += 1
    n += 1

print(total)
