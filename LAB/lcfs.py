import heapq

def shortest_path(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def main():
    num_nodes, num_edges = map(int, input("Enter the number of nodes and edges: ").split())

    graph = {node: {} for node in range(1, num_nodes + 1)}

    for _ in range(num_edges):
        start, end, weight = map(int, input("Enter edge (start end weight): ").split())
        graph[start][end] = weight

    start_node = int(input("Enter the start node: "))

    result = shortest_path(graph, start_node)

    for node, distance in result.items():
        print(f"Shortest distance from {start_node} to {node}: {distance}")

if __name__ == "__main__":
    main()

# Enter the number of nodes and edges: 4 5
# Enter edge (start end weight): 1 2 1
# Enter edge (start end weight): 1 3 4
# Enter edge (start end weight): 2 3 2
# Enter edge (start end weight): 2 4 5
# Enter edge (start end weight): 3 1 7
# Enter the start node: 1
# Shortest distance from 1 to 1: 0
# Shortest distance from 1 to 2: 1
# Shortest distance from 1 to 3: 3
# Shortest distance from 1 to 4: 6