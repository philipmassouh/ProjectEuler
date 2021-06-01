import math
# find the smallest number that is divisible by 1-20


def div():
    x = 20
    while x < math.factorial(20):
        valid = True
        for y in range(20, 1, -1):
            if x % y != 0:
                valid = False
                y = 22
        if valid:
            return x
        x += 20


print(div())
