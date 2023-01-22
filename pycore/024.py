import itertools

a = []
for permutations in itertools.permutations("0123456789", 10):
    a.append(int("".join(str(i) for i in ([int(i) for i in permutations]))))
a.sort()
print(a[999999])
