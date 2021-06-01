def pal():
    for x in range(998001, 9999, -1):
        if (int(str(x)[::-1])) == x:
            for y in range(999, 100, -1):
                if x % y == 0 and 99 < x / y < 1000:
                    return x


print(pal())
