"listy skladane macierze vs for"
M = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]

N = [[1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]]

print(M[1])

a = [row[1] for row in M]
print(a)

b = [M[i][i] for i in range(len(M))]
print(b)

c = [M[row][col] * N[row][col] for row in range(3) for col in range(3)]
print(c)

d = [[M[row][col] * N[row][col] for row in range(3)] for col in range(3)]
print(d)

e = [[M[row][col] * N[row][col] for col in range(3)] for row in range(3)]
print(e)

res = []
for row in range(3):
    for col in range(3):
        res.append(M[row][col] * N[row][col])

print(res)

res2 = []
for row in range(3):
    temp = []
    for col in range(3):
        temp.append(M[row][col] * N[row][col])
    res2.append(temp)
print(res2)


