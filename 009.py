def sol1():
    x = 0
    y = 0
    z = 0

    while x < 1001:
        y = x + 1
        while y < 1001:
            z = 1000 - x - y
            if -1 < z != y != x and x + y + z == 1000 and x**2 + y**2 == z**2:
                print(x)
                print(y)
                print(z)
                break
            y += 1
        x += 1

def sol2():
    for a in range(3, 1000):
        for b in range(a, 1000):
            c = (a*a+b*b)**0.5
            if c%1==0 and a+b+c==1000:
                print(int(a*b*c))

sol2()



