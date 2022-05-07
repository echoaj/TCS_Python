
visited = []
matrix = [[0, 0, 0, 0, 0, 0],
          [0, 1, 0, 3, 4, 0],
          [0, 5, 6, 7, 8, 0],
          [0, 9, 0, 0, 0, 0],
          [0, 13, 14, 15, 16, 0],
          [0, 0,   0,  0,  0, 0]]

solvable = False


def dfs(matrix, x, y):
    global solvable

    if solvable:
        return solvable
    if matrix[x][y] == 16:
        return True
    if matrix[x][y] == 0:
        return False
    if matrix[x][y] in visited:
        return False
    else:
        visited.append(matrix[x][y])

    left =  dfs(matrix, x + 1, y)   # check right neighbor
    right = dfs(matrix, x, y + 1)   # check down neighbor
    down =  dfs(matrix, x + 1, y)   # check left neighbor
    up =    dfs(matrix, x, y - 1)   # check up neighbor

    solvable = left or right or down or up
    return solvable


result = dfs(matrix, 1, 1)
print(result)

print(visited)
