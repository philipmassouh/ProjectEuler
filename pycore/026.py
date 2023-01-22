"""
A unit fraction contains 1 in the numberator. The decimal
representation of the unit fractions with denominators 2
to 10 are given:
1/2 = 0.5
1/3 = 0.3(3)
1/4 = 0.25
1/5 = 0.2
1/6 = 0.1(6)
1/7 = 0.(142857)
1/8 = 0.125
1/9 = 0.(1)
1/10 = 0.1

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in it's
decimal fraction part
    0.1666
6 | 1.0000
"""


def getSequence(n, d):
    sequence = []
    remainders = []
    while True:
        sequence.append(n // d)
        if remainders.count((n % d)) > 0:
            break
        else:
            remainders.append((n % d))
        n = 10 * (n % d)
    return sequence


if __name__ == "__main__":
    max_seq = 0
    for i in range(1, 1000):
        if len(getSequence(1, i)) > max_seq:
            max_seq = i

    print(f"1/{max_seq} has the largest repeating sequence")
