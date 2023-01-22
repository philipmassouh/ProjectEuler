# read in the file
A = []
f = open("data013.txt", "r")
for line in f:
    A.append(int(line))
f.close()

sum = 0
for x in range(0, len(A)):
    sum += A[x]

print(sum)
