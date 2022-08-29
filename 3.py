#import numpy as np

# mat = [[0, 3, -6, 6, 4, -5], [3, -7, 8, -5, 8, 9], [3, -9, 12, -9, 6, 15]]
# mat = [[1, 1, 1, 6], [2, -1, 1, 3], [1, 0, 1, 4]]
# mat = [[1, 3, 4, 7], [2, 4, 6, 8], [3, 6, 9, 12]]
# mat = [[0, 1, -2, 3], [1, -3, 4, -6]]
# mat = [[1, -3, 7, 1], [0, 1, 4, 0], [0, 0, 0, 1]]
mat = [[1, 1, 1, 8], [-1, -2, 3, 1], [3, -7, 4, 10]]

n = len(mat[0]) - 1
for i in range(n):
    if mat[i][i] == 0:
        print('No Solution!')
        break

    for j in range(n):
        if i != j:
            ratio = mat[j][i] / mat[i][i]

            for k in range(n + 1):
                mat[j][k] = round(mat[j][k] - ratio * mat[i][k], 2)

for i in mat:
    print(i)
