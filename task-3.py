import networkx as nx
import matplotlib.pyplot as plt
import heapq


G = nx.Graph()
stations = ["Station A", "Station B", "Station C", "Station D", "Station E", "Station F"]
G.add_nodes_from(stations)
edges_with_weights = [("Station A", "Station B", 4), ("Station B", "Station C", 1), 
                      ("Station C", "Station D", 2), ("Station D", "Station E", 5),
                      ("Station E", "Station F", 1), ("Station B", "Station D", 3)]
G.add_weighted_edges_from(edges_with_weights)


pos = nx.spring_layout(G)
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("City Metro Network with Weights")
plt.show()

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

shortest_paths = {station: dijkstra(G, station) for station in stations}

for start in shortest_paths:
    print(f"Shortest paths from {start}:")
    for end in shortest_paths[start]:
        print(f"  to {end}: {shortest_paths[start][end]}")