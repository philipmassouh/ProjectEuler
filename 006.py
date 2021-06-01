# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum

ssq = 0
sqs = 0
for x in range(1, 101):
    ssq += x**2
    sqs += x

print(sqs**2-ssq)
