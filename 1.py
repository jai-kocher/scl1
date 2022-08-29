import numpy as np
import re

# a
# 2x + 3y = 7
# 5x + 7y = 5

# b
# 15x + 3y + 5z = 1
# 12x + 5y + 7z = 2
# 17x + 7y + 9z = 3

def augmentedMatrix(seq):
    seq = [i.replace(' ', '').replace('-', ' -') for i in seq]
    neq = len(seq)
    nvar = max([len(re.findall('[a-zA-z]', i)) for i in seq])
    res = [int(re.sub('[A-Za-z]', '', j)) for k in [re.split(' |\+|\=', i) for i in seq] for j in k if j]
    augMat = np.reshape(res, (neq, nvar + 1))
    return(augMat)

seq = []
while True:
    inp = input("Enter Equation: ")
    if inp == 'xx':
        break
    else:
        seq.append(inp)

print(augmentedMatrix(seq))

