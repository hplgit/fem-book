# P1 elements
# Left to right numbering
"""
elements: |--0--|--1--|--2--|
vertices: 0     1     2     3
dofs:     0     1     2     3
"""
# elements:   0   1   2
# vertices: 0   1   2   3

vertices = [0, 1, 1.2, 2]
cells    = [[0,1], [1,2], [2,3]]
dof_map  = [[0,1], [1,2], [2,3]]

# Right to left numbering
"""
elements: |--2--|--1--|--0--|
vertices: 3     2     1     0
dofs:     3     2     1     0
"""

vertices = [2, 1.2, 1, 0]
cells    = [[1,0], [2,1], [3,2]]
dof_map  = [[1,0], [2,1], [3,2]]


# P2 elements

# Left to right numbering
# elements:   0   1   2
"""
elements: |--0--|--1--|--2--|
vertices: 0     1     2     3
dofs:     0  1  2  3  4  5  6
"""

vertices = [0, 1, 1.2, 2]
cells    = [[0,1], [1,2], [2,3]]
dof_map  = [[0,1,2], [2,3,4], [4,5,6]]

# Right to left numbering
# elements:   2   1   0
"""
elements: |--2--|--1--|--0--|
vertices: 3     2     1     0
dofs:     6  5  4  3  2  1  0
"""

vertices = [2, 1.2, 1, 0]
cells    = [[1,0], [2,1], [3,2]]
dof_map  = [[2,1,0], [4,3,2], [6,5,4]]

