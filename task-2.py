import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


G = nx.Graph()
stations = ["Station A", "Station B", "Station C", "Station D", "Station E", "Station F"]
G.add_nodes_from(stations)
edges = [("Station A", "Station B"), ("Station B", "Station C"), 
         ("Station C", "Station D"), ("Station D", "Station E"),
         ("Station E", "Station F"), ("Station B", "Station D")]
G.add_edges_from(edges)


def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path)
            if new_path:
                return new_path
    return None


def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        elif node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    return None


plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')
plt.title("City Metro Network")
plt.show()


start_node = "Station A"
end_node = "Station E"

dfs_path = dfs(G, start_node, end_node)
bfs_path = bfs(G, start_node, end_node)

print("DFS path:", dfs_path)
print("BFS path:", bfs_path)
