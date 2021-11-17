def sol1():
    sum = 0
    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

def sol2():
    return sum([i for i in range(1000) if i%3==0 or i%5==0])

print(sol2())
