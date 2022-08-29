import re
import numpy as np

def augmentedMatrix(seq):
    seq = [i.replace(' ', '').replace('-', ' -') for i in seq]
    neq = len(seq)
    nvar = max([len(re.findall('[a-zA-z]', i)) for i in seq])
    res = [int(re.sub('[A-Za-z]', '', j)) for k in [re.split(' |\+|\=', i) for i in seq] for j in k if j]
    augMat = np.reshape(res, (neq, nvar + 1))
    return(augMat)

a1 = '4x + 1y + 1z = 2'
a2 = '1x + 5y + 2z = -6'
a3 = '1x + 2y + 3z = -4'

b1 = '2x + 5y = 21'
b2 = '1x + 2y = 8'

c1 = '2x + 3y - 1z = 5'
c2 = '3x + 2y + 1z = 10'
c3 = '1x - 5y + 3z = 0'

augMat = augmentedMatrix([c1, c2, c3])
neq = len(augMat)
vars = dict()
rows = dict()
for i in range(neq):
    vars[i] = 0
    rows[i + 1] = augMat[i]

for i in range(20):
    for j in range(neq):
        vars[j] = (rows[j + 1][-1] - sum([rows[j + 1][k] * vars[k] for k in range(neq) if k != j])) / rows[j + 1][j]

for i in range(neq):
    print(f'{chr(i + 120)} = {round(vars[i], 2)}')

