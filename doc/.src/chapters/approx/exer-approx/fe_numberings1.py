# P1 elements
# Left to right numbering
"""
elements: |--0--|--1--|--2--|
nodes:    0     1     2     3
"""

nodes    = [0, 1, 1.2, 2]
elements = [[0,1], [1,2], [2,3]]

# Right to left numbering
"""
elements: |--2--|--1--|--0--|
nodes:    3     2     1     0
"""

nodes    = [2, 1.2, 1, 0]
elements = [[1,0], [2,1], [3,2]]


# P2 elements

# Left to right numbering
"""
elements: |--0--|--1--|--2--|
nodes:    0  1  2  3  4  5  6
"""

nodes = [0, 0.5, 1, 1.1, 1.6, 2]
elements = [[0,1,2], [2,3,4], [4,5,6]]

# Right to left numbering
"""
elements: |--2--|--1--|--0--|
nodes:    6  5  4  3  2  1  0
"""

nodes = [2, 1.6, 1.2, 1.1, 1, 0.5, 0]
elements = [[2,1,0], [4,3,2], [6,5,4]]
