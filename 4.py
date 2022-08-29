import re
import numpy as np

def augmentedMatrix(seq):
    seq = [i.replace(' ', '').replace('-', ' -') for i in seq]
    neq = len(seq)
    nvar = max([len(re.findall('[a-zA-z]', i)) for i in seq])
    res = [int(re.sub('[A-Za-z]', '', j)) for k in [re.split(' |\+|\=', i) for i in seq] for j in k if j]
    augMat = np.reshape(res, (neq, nvar + 1))
    return(augMat)

a1 = '1x + 1y + 2z = 8'
a2 = '-1x - 2y + 3z = 1'
a3 = '3x - 7y + 4z = 10'

b1 = '2w - 3x + 4y - 4z = 0'
b2 = '7w + 1x - 8y + 9z = 0'
b3 = '2w - 8x + 1y - 1z = 0'

c1 = '2w - 1x + 3y - 4z = 9'
c2 = '1w + 1x - 2y + 7z = 11'
c3 = '3w - 3x + 1y + 5z = 8'
c4 = '2w + 1x + 4y + 4z = 10'

print(augmentedMatrix([a1, a2, a3]))