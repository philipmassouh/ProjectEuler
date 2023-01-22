# read in the file and sort
f = open("data022.txt", "r")
for line in f:
    names = eval("[" + line + "]")
f.close()
names.sort()

# problem implicitly wants arrays indexed at 1.
names.insert(0, "foo")

net_total = 0
for x in range(1, len(names)):
    letter_sum = 0
    for y in range(0, len(names[x])):
        letter_sum += ord(names[x][y]) - 64
    net_total += x * letter_sum

print(net_total)
