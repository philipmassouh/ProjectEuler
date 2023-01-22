import math

# let d(n) be the sum of all positive integer divisors of n.
# if d(a)=b and d(b)=a where a is not equal to b, a and b are considered 'amicable numbers'


# returns the sum of the factors of n
def d(n):
    s = 0
    for x in range(int(math.ceil(n / 2)), 0, -1):
        if n % x == 0:
            s += x
    return s


total = 0
for a in range(0, 10000):
    b = d(a)
    if a != b and d(b) == a:
        total += (a + b) / 2

print(total)
