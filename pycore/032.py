"""
We shall say that an n-digit number is pandigital if it
makes use of all the digits 1 to n exactly once; e.g.,
the 5 digit number, 15234, is 1-5 pandigital

The product 7254 is unusual, as the identity, 39x186=7254,
containing multiplicant, multiplier, and the product is 
1 through 9 pandigital

Find the sum of all products whos multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way to be
sure to only include it once in your sum
"""


def mmp_pandigital(a, b):
    combined = str(a) + str(b) + str(a * b)
    return len(set(combined)) == len(combined) == 9 and list(combined).count("0") == 0


products = []
# i might be missing a few, mess with these ranges if wrong
for i in range(0, 1000):
    for j in range(i, 1000):
        if mmp_pandigital(i, j) and products.count(i * j) == 0:
            print(f"{i}x{j}={i*j}")
            products.append(i * j)

print(f"The sum of these values is {sum(products)}")
