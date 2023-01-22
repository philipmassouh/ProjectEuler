def orderedset(element, list):
    if list.count(element) == 0:
        x = 0
        while x < len(list):
            if element < list[x]:
                break
            x += 1
        list.insert(x, element)


l = []
for a in range(2, 101):
    for b in range(2, 101):
        orderedset(a**b, l)

print(len(l))
