
def sparsity_pattern(elements, N_n):
    import numpy as np
    matrix = np.zeros((N_n, N_n), dtype=str)
    matrix[:,:] = '0'
    for e in elements:
        for i in e:
            for j in e:
                matrix[i,j] = 'X'
    matrix = matrix.tolist()
    matrix = '\n'.join([' '.join([matrix[i][j]
                                  for j in range(len(matrix[i]))])
                        for i in range(len(matrix))])
    return matrix


print('\nP1 elements, left-to-right numbering')
N_n = 4
elements = [[0,1], [1,2], [2,3]]
print(sparsity_pattern(elements, N_n))

print('\nP1 elements, right-to-left numbering')
elements = [[1,0], [2,1], [3,2]]
print(sparsity_pattern(elements, N_n))

print('\nP2 elements, left-to-right numbering')
N_n = 7
elements = [[0,1,2], [2,3,4], [4,5,6]]
print(sparsity_pattern(elements, N_n))

print('\nP1 elements, right-to-left numbering')
elements = [[2,1,0], [4,3,2], [6,5,4]]
print(sparsity_pattern(elements, N_n))

