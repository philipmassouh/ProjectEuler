"""
The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify that it may incorrectly
believe that 49/48 = 4/8, which is correct, is obtained by 
cancelling the 9s.

We shall consider fractions like 30/50 = 3/5, to be trivial examples

There are exactly four non-trivial examples of this type of fraction,
less that one in value, and containing two digits in the numerator
and denominator.

If the product of these four fractions is given in its lowest 
common terms, find the value of the denominator
"""


def gcd(a, b):
    # fast algo
    pass


def simplify(a, b):
    g = gcd(a, b)
    return a // g, b // g


def isCurious(a, b):
    # get set intersection of string conversion of a and b and if it is not zero
    # remove that intersection from each value and check them with simplified
    # if they both match, it is curious
    pass


a = 1
b = 1
for i in range(0, 100):
    for j in range(i, 100):
        if isCurious(i, j):
            print(f"{i}/{j} is curious")
            a *= i
            b *= j

g = gcd(a, b)
print(f"{a}/{b} simplifies to {a//g}/{b//g}")
