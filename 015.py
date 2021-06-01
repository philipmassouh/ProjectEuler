# this is a simple nCr
# 40 choose 20 is the answer

import math
n = 40
r = 20
print(math.factorial(n)/(math.factorial(n-r)*math.factorial(r)))