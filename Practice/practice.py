

graph = {'A': ['B', 'C', 'D'],
         'B': ['A', 'G'],
         'G': ['B'],
         'C': ['A', 'E', 'H'],
         'D': ['A', 'E'],
         'E': ['C', 'D', 'F', 'H', 'I'],
         'F': ['E'],
         'H': ['C', 'E', 'J'],
         'I': ['E'],
         'J': ['H']
        }

visted = []


# create a dfs recursive function
def dfs(node):
    visted.append(node)
    for n in graph[node]:
        if n not in visted:
            dfs(n)


# 1) stop recursion when node is reached
# 2) return true if solvable else return false
def dfs_modified(node, end):
    if node == end:
        visted.append(node)
        return True
    visted.append(node)
    for n in graph[node]:
        if n not in visted:
            solved = dfs_modified(n, end)
            if solved:
                return True
    return False


dfs('A')
print(visted)
visted.clear()
solvable = dfs_modified('A', 'F')
print(visted)
print(solvable)
