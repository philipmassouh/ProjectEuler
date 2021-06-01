coin_values = [2, 5, 10, 20, 50, 100, 200]
change_goal = 1
total_perms = 0
while(change_goal < 201):
    a = [1]
    for coin_value in coin_values:
        if change_goal - coin_value > 1:
            a.append(change_goal - coin_value + 1)
        else:
            a.append(a[-1])
    print(a)
    change_goal += 1
