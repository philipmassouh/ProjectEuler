# read in the file
A = []
f = open('data011.txt', 'r')
for line in f:
    A.append(list(map(int, line.split(' '))))
f.close()

# maximum value
mx = 0

# check right diagonal
z = 0
while z < len(A[0]) - 3:
    k = 0
    while k < len(A) - 3:
        temp = A[z][k] * A[z+1][k+1] * A[z+2][k+2] * A[z+3][k+3]
        if temp > mx:
            mx = temp
        k += 1
    z += 1

# check right horizontal
for x in range(0, len(A)):
    i = 0
    while i < len(A[x]) - 3:
        temp = A[x][i] * A[x][i+1] * A[x][i+2] * A[x][i+3]
        if temp > mx:
            mx = temp
        i += 1


# flip horizontally
for x in range(0, len(A)):
    A[x].reverse()

# check left diagonal
z = 0
while z < len(A[0]) - 3:
    k = 0
    while k < len(A) - 3:
        temp = A[z][k] * A[z+1][k+1] * A[z+2][k+2] * A[z+3][k+3]
        if temp > mx:
            mx = temp
        k += 1
    z += 1

# check left horizontal
for x in range(0, len(A)):
    i = 0
    while i < len(A[x]) - 3:
        temp = A[x][i] * A[x][i+1] * A[x][i+2] * A[x][i+3]
        if temp > mx:
            mx = temp
        i += 1

# check vertical lines going down
for y in range(0, len(A[0])):
    j = 0
    while j < len(A) - 3:
        temp = A[y][j] * A[y][j+1] * A[y][j+2] * A[y][j+3]
        if temp > mx:
            mx = temp
        j += 1

# flip vertically
A.reverse()

# check vertical lines going up
for y in range(0, len(A[0])):
    j = 0
    while j < len(A) - 3:
        temp = A[y][j] * A[y][j+1] * A[y][j+2] * A[y][j+3]
        if temp > mx:
            mx = temp
        j += 1

print(mx)
