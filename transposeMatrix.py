inputMatrix = [[1, 2, 3],
            [4, 5, 6]]

matrixTrans = [[0, 0], 
                [0, 0],
                [0, 0]]

for i in range(0, 3):
    for j in range(0, 2):
        matrixTrans[i][j] = inputMatrix[j][i]

for trans in matrixTrans:
   print(trans) 
