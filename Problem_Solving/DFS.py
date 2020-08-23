# Depth First Search

# graph representation in adjacency list format
adj_list = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

# required variables
color = {} # "W" - initial color, "G" - first visit, "B" - fully explored
parent = {}
output = []

# initialization
for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None

# dfs function, u - source vertex
def dfs(u):
    # visited node, change the color to "Grey"
    color[u] = "G"
    output.append(u)

    # visit the child nodes of u
    for v in adj_list[u]:
        # check whether the node is not visited yet
        if color[v] == "W":
            parent[v] = u
            dfs(v)
    # all nodes related to u have been explored        
    color[u] = 'B'

dfs('A')
print(output)
# ['A', 'B', 'D', 'E', 'F', 'C']

