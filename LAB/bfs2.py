from collections import defaultdict, deque

def construct_graph():
    graph = defaultdict(list)
    vertices, edges = map(int, input("Enter the number of vertices and edges (space-separated): ").split())
    for _ in range(edges):
        u, v = map(int, input("Enter edge (u v): ").split())
        graph[u].append(v)
        graph[v].append(u)  # For undirected graph
    return graph

def bfs_shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node == end:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None

if __name__ == "__main__":
    graph = construct_graph()

    while True:
        source = int(input("Enter the source node: "))
        if source not in graph:
            print("Invalid source node. Please enter a valid one.")
        else:
            break

    while True:
        destination = int(input("Enter the destination node: "))
        if destination not in graph:
            print("Invalid destination node. Please enter a valid one.")
        else:
            break

    shortest_path = bfs_shortest_path(graph, source, destination)

    if shortest_path:
        print(f"Shortest path from {source} to {destination}: {shortest_path}")
    else:
        print(f"No path exists from {source} to {destination}.")

# Enter the number of vertices and edges (space-separated): 5 5
# Enter edge (u v): 0 1
# Enter edge (u v): 0 2
# Enter edge (u v): 0 3
# Enter edge (u v): 1 2
# Enter edge (u v): 2 4
# Enter the source node: 0
# Enter the destination node: 4
# Shortest path from 0 to 4: [0, 2, 4]