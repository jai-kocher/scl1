def isNonZero(row):
    return True if set(row) != {0} else False 

def isAboveZeroRow(k, mat):
    return all(i > mat.index(mat[k]) for i in [j for j in range(len(mat)) if set(mat[j]) == {0}])

def firstNonZero(row):
    for i in row:
        if i != 0:
            return(i)

def checkREF(mat):
    l = len(mat[0])
    nz = len(mat) - mat.count([0] * l)
    c = 0
    for i in range(len(mat)):
        if isNonZero(mat[i]) and firstNonZero(mat[i]) == 1 and isAboveZeroRow(i, mat):
            if i > 0 and mat[i].index(1) > mat[i - 1].index(1):
                c += 1
            elif i == 0:
                c += 1
 
    return True if c == nz else False

def checkRREF(mat):
    l = len(mat[0])
    nz = len(mat) - mat.count([0] * l)
    c = 0
    for i in range(len(mat)):
        if isNonZero(mat[i]) and isAboveZeroRow(i, mat):
            pivInd = mat[i].index(1)
            if mat[i][:pivInd] == [0] * pivInd:
                col = [mat[j][pivInd] for j in range(len(mat))]
                if set(col) == {1, 0} and col.count(1) == 1:
                    c += 1
    
    return True if c == nz else False

mat1 = [[1, 2, 0, 3, 0], 
       [0, 0, 1, 1, 0], 
       [0, 0, 0, 0, 1], 
       [0, 0, 0, 0, 0]]

mat2 = [[1, -7, 5, 5], 
       [0, 1, 3, 2]]

mat3 = [[1, 2, 3, 4, 5],
       [1, 0, 7, 1, 3], 
       [0, 0, 0, 0, 1], 
       [0, 0, 0, 0, 0]]

mat4 = [[1, 2, 3], 
       [0, 0, 1], 
       [0, 0, 0], 
       [0, 0, 0]]

lis = [mat1, mat2, mat3, mat4]
print('\tREF\tRREF')
for i in range(len(lis)):
    print(i + 1, checkREF(lis[i]), checkRREF(lis[i]), sep = '\t')

