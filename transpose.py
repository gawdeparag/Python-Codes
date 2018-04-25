matrix01 = [[1, 2, 3],
            [4, 5, 6]]

matrixtrans = [[0, 0], 
                [0, 0],
                [0, 0]]

for i in range(0, 3):
    for j in range(0, 2):
        matrixtrans[i][j] = matrix01[j][i]

for trans in matrixtrans:
   print(trans) 
