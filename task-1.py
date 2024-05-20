import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()


stations = ["Station A", "Station B", "Station C", "Station D", "Station E", "Station F"]
G.add_nodes_from(stations)


edges = [("Station A", "Station B"), ("Station B", "Station C"), 
         ("Station C", "Station D"), ("Station D", "Station E"),
         ("Station E", "Station F"), ("Station B", "Station D")]

G.add_edges_from(edges)


plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')
plt.title("City Metro Network")
plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_of_nodes = dict(G.degree())

print(f"Number of stations (nodes): {num_nodes}")
print(f"Number of connections (edges): {num_edges}")
print("Degree of each station (node):")
for station, degree in degree_of_nodes.items():
    print(f"{station}: {degree}")
