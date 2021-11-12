'''
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six 
red discs, and two discs were taken at random, it can be seen that the probability 
of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue 
discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10^12 = 1,000,000,000,000 discs in 
total, determine the number of blue discs that the box would contain.
'''

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def p_bb_check(blue, red):
    a = blue * (blue - 1)
    b = (blue + red) * (blue + red - 1)
    g = gcd(a,b)
    return a/g == 1 and b/g == 2

def p_bb_decimal(blue, red):
    a = blue * (blue - 1)
    b = (blue + red) * (blue + red - 1)
    return a / b

# def gcheck(x,y):
#     return x+y > 10**12

# #graph the different blue and red values up to 1000
# fig = plt.figure(figsize=(10,6))
# ax1 = fig.add_subplot(111, projection='3d')

# x = np.arange(1000)
# y = np.arange(1000)
# x = np.linspace(0, 10**12, 1000)
# y = np.linspace(0, 10**12, 1000)
# X,Y = np.meshgrid(x, y)
# Z = gcheck(X, Y)

# mycmap = plt.get_cmap('gist_earth')
# surf1 = ax1.plot_surface(X, Y, Z, cmap=mycmap,vmin=0.0, vmax=1.0)
# fig.colorbar(surf1, ax=ax1)

# plt.show()

# we want to start at b=b and r=b/2 which in the case of 10^12 means start at b 2/3 of 10^2 r as 10^12 - b
# we will then go backwards until we either get 0.5 or a value >0.5
# in the latter case we increment b by 1 and go again

# this line is faster analysis so we will use it and if it yields 0.5 we will do a sanity check
# with my function

def traverse(b, r):
    red = r
    while (result:=p_bb_decimal(b,red)) <= 0.5:
        if result == 0.5 and p_bb_check(b, red):
            return b,red
        red -= 1
    return 0,0

stop = False
big = 5
blue = (2*big) // 3 
while True:
    b,r = traverse(blue, blue//2)
    if b+r != 0:
        print(b,r,r/b)
    blue += 1



