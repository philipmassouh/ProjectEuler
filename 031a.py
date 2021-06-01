coins = [1, 2, 5, 10, 20, 50, 100, 200]
perms = [1] + [0] * 200

for coin in coins:
    for x in range(coin, 201):
        perms[x] += perms[x - coin]
print(perms[-1])