
queue = []
visited = []


def breadth_first_search(x, y):
    queue.append((x, y))
    visited.append((x, y))
    while queue:
        x, y = queue.pop(0)
        #             right      down      left       up
        neighbors = [(x+1, y), (x, y+1), (x-1, y), (x, y-1)]
        for x, y in neighbors:
            if (x, y) not in visited and matrix[x][y] != 0:
                queue.append((x, y))
                visited.append((x, y))


# matrix of zeros
matrix = [[0, 0, 0, 0, 0, 0],
          [0, 1, 0, 3, 4, 0],
          [0, 5, 6, 7, 8, 0],
          [0, 9, 0, 0, 0, 0],
          [0, 13, 14, 15, 16, 0],
          [0, 0,   0,  0,  0, 0]]

breadth_first_search(1, 1)
print(visited)
for x, y in visited:
    print(matrix[x][y])