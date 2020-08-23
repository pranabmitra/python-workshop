# Detect cycle in a directed graph using DFS algorithm

adj_list = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": [],
    "D": ["A", "E"],
    "E": []
}

color = {}
parent = {}

for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None


def dfs(u):
    color[u] = "G"

    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            cycle = dfs(v)
            if cycle == True:
                return True
        elif color[v] == "G":
            print("Cycle found!", u, "->", v)
            return True

    color[u] = "B"
    return False


# start
has_cycle = False
for u in adj_list.keys():
    if color[u] == "W":
        has_cycle = dfs(u)
        if has_cycle == True:
            break

print(has_cycle)