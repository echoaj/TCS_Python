from Ryan_Maluf.Queue.Queue import Queue

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


queue = Queue()
visited = []


def bfs(node):
    queue.push(node)
    visited.append(node)
    while not queue.is_empty():
        node = queue.pop()
        for n in graph[node]:
            if n not in visited:
                queue.push(n)
                visited.append(n)


tracer = {}                         # extra
path = []                           # extra


def bfs_mod(node, end):
    queue.push(node)
    visited.append(node)
    while not queue.is_empty():
        node = queue.pop()
        if node == end:
            return True
        for n in graph[node]:
            if n not in visited:
                queue.push(n)
                visited.append(n)
                tracer[n] = node    # extra  (set n to parent)
    return False


# Extra
def get_path(node):
    path.insert(0, node)
    if node in tracer:
        get_path(tracer[node])

"""
bfs("A")
print(visited)
visited.clear()

solvable = bfs_mod("A", "J")
print(solvable)
print(visited)

# Extra
get_path("J")
print(tracer)
print(path)


tracer = {}

tracer.update({"val": "key"})
tracer["val2"] = "key2"
"""