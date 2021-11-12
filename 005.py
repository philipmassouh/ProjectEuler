x = 20
while (not all([x % i == 0 for i in range(2,21)])):
    x += 20
print(x)
