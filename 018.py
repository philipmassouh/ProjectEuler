# read in the file
A = []
f = open('data018.txt', 'r')
for line in f:
    A.append(list(map(int, line.split(' '))))
f.close()

# normalize text input into a square
l = len(A[-1])
for x in range(0, len(A)):
    while len(A[x]) < l:
        A[x].append(0)

# start at second from bottom row
for x in range(-2, -len(A)-1, -1):
    for y in range(0, len(A[0])-1):
        if A[x][y] != 0:
            if A[x+1][y] < A[x+1][y+1]:
                A[x][y] += A[x+1][y+1]
            else:
                A[x][y] += A[x+1][y]

print(A[0])