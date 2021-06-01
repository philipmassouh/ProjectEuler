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


