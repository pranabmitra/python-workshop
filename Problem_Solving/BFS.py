# Breadth First Search

from queue import Queue

# graph representation with adjacency list
adj_list = {
    "A": ["B", 'D'],
    "B": ["A", "C"],
    "C": ["B"],
    "D": ["A", "E", "F"],
    "E": ["D", "F", "G"],
    "F": ["D", "E", "H"],
    "G": ["E", "H"],
    "H": ["F", "G"]    
}

# required dictionaries/list
visited = {} # True/False
parent = {}
level = {} # distance
output = []
queue = Queue()

# initialization
for node in adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

# main BFS function
def bfs(u):
    visited[u] = True
    level[u] = 0
    queue.put(u)

    # loop until the queue is empty
    while not queue.empty():
        u = queue.get()
        output.append(u)

        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                level[v] = level[u] + 1
                parent[v] = u
                queue.put(v)
    

bfs('A')
print("BFS Output: ")
print(output)
# ['A', 'B', 'D', 'C', 'E', 'F', 'G', 'H']

# --------------- #
# shortest distance of all nodes from the source node
print("Shortest distance of all node from the source node A: ")
print(level)
# {'A': 0, 'B': 1, 'C': 2, 'D': 1, 'E': 2, 'F': 2, 'G': 3, 'H': 3}
# single one
print("Shortest distance G from the source node A: ")
print(level["G"])
# 3

# --------------- #
# shortest path of any node from the source node
target = "G" # path from "A" to "G"
path =[]

while target is not None:
    path.append(target)
    target = parent[target]

path.reverse()
print("Shortest path from A to G: ")
print(path)
# ['A', 'D', 'E', 'G']