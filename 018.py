def sol1():
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

triangle = [
    75,
    95, 64,
    17, 47, 82,
    18, 35, 87, 10,
    20,  4, 82, 47, 65,
    19,  1, 23, 75,  3, 34,
    88,  2, 77, 73,  7, 63, 67,
    99, 65,  4, 28,  6, 16, 70, 92,
    41, 41, 26, 56, 83, 40, 80, 70, 33,
    41, 48, 72, 33, 47, 32, 37, 16, 94, 29,
    53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,
    70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,
    91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,
    63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,
     4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23,
]

# put this into a 2d array for easier calculation
triangle2d = [[]]
row = 0
for v in triangle:
    if len(triangle2d[row]) > row:
        triangle2d.append([])
        row += 1
    triangle2d[row].append(v)

def sol2():
    # row up, col left
    def left(l,row,col):
        validRow = -1 < row - 1 < len(l)
        if validRow and -1 < (col-1) < len(l[row-1]):
            return l[row-1][col-1]
        return None

    # row up, same col
    def right(l,row,col):
        validRow = -1 < row - 1 < len(l)
        if validRow and -1 < (col) < len(l[row-1]):
            return l[row-1][col]
        return None


    for i,row in enumerate(triangle2d):
        for j,v in enumerate(row):
            l = left(triangle2d,i,j)
            r = right(triangle2d,i,j)

            l = l if l is not None else r
            r = r if r is not None else l

            if l is not None:
                triangle2d[i][j] = v+l if l > r else v+r

    print(max(triangle2d[-1]))
        

def sol3(t):
    for i in range(1,len(t)):
        for j in range(len(t[i])):
            parents = []
            if -1 < j < len(t[i-1]):
                parents.append(t[i-1][j])
            if -1 < j-1 < len(t[i-1]):
                parents.append(t[i-1][j-1])
            if len(parents) > 0:
                t[i][j] += max(parents)

sol3(triangle2d)
print(max(triangle2d[-1]))
