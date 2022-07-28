

graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "G"],
    "C": ["A", "E", "H"],
    "D": ["A", "E"],
    "E": ["C", "D", "F", "H", "I"],
    "F": ["E"],
    "G": ["B"],
    "H": ["C", "E", "J"],
    "I": ["E"],
    "J": ["H"]
}

visited = []
path = []


def dfs(node):
    visited.append(node)
    for n in graph[node]:
        if n not in visited:
            dfs(n)


def dfs_mod(node, end):
    path.append(node)
    if node == end:
        return True
    for n in graph[node]:
        if n not in path:
            if dfs_mod(n, end):
                return True

"""
dfs("A")
print(visited)

solvable = dfs_mod("A", "D")
print(path)
print(solvable)
"""