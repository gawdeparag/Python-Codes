matrix01 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]

matrix02 = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

matrixres = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

for i in range (0, 3):
    for j in range (0, 3):
        matrixres[i][j] = matrix01[i][j] - matrix02[i][j]

for res in matrixres:
    print(res)