# Graph Pathfinding with DFS and BFS

## Introduction

This project demonstrates the implementation of Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms to find paths in a graph representing a city's metro network.

## Graph Creation

We created a graph representing a city's metro network with stations as nodes and connections as edges.

![Graph Visualization](graph.png)

## DFS and BFS Implementation

### Depth-First Search (DFS)

DFS explores as far as possible along each branch before backtracking. It is implemented using a recursive approach.

### Breadth-First Search (BFS)

BFS explores all neighbors at the present depth level before moving on to nodes at the next depth level. It is implemented using a queue.

## Pathfinding Results

We compared the paths found by DFS and BFS from "Station A" to "Station E":

- **DFS Path**: ['Station A', 'Station B', 'Station C', 'Station D', 'Station E']
- **BFS Path**: ['Station A', 'Station B', 'Station D', 'Station E']

### Explanation of Results

- **DFS**: This algorithm explores deeper into the graph first. It found a path through 'Station B', 'Station C', and 'Station D' before reaching 'Station E'.
- **BFS**: This algorithm explores the nearest nodes first. It found a shorter path directly from 'Station B' to 'Station D', and then to 'Station E'.

The difference in the paths is due to the nature of each algorithm. DFS is more likely to find longer paths as it explores depth-wise, while BFS finds the shortest path in terms of the number of edges.

## Conclusion

BFS is more suitable for finding the shortest path in terms of the number of edges, while DFS can be useful for exploring all possible paths. The choice of algorithm depends on the specific requirements of the pathfinding task.

## Code

The code for the graph creation, DFS, and BFS implementations is included in this repository.
