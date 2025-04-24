import networkx as nx
import heapq

def dijkstra(graph: nx.Graph, start: str) -> dict:
    distances = {node: float("inf") for node in graph.nodes()}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor].get("weight", 1)
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

G = nx.Graph(name="Small city network")

objects = {
    "Train station": (0, 0),
    "Center": (2, 2),
    "Independence square": (4, 2),
    "University": (6, 2),
    "Market": (3, 5),
    "Hospital": (3, 0),
    "Park": (6, 0),
    "Stadium": (8, 4),
    "Residential area1": (1, 1),
    "Residential area2": (1, 1),
}

paths = [
    ("Train station", "Center", 7),
    ("Center", "Independence square", 7),
    ("Independence square", "Market", 11),
    ("Market", "Park", 6),
    ("Park", "University", 6),
    ("University", "Hospital", 6),
    ("Stadium", "Park", 8),
    ("Stadium", "Hospital", 8),
    ("Park", "Residential area1", 8),
    ("Residential area1", "Center", 8),
    ("Center", "Park", 8),
    ("Park", "Hospital", 8),
    ("Stadium", "Residential area2", 8),
    ("Residential area2", "University", 8),
    ("Residential area2", "Hospital", 8),
]

for name, coords in objects.items():
    G.add_node(name, pos=coords)

for u, v, weight in paths:
    G.add_edge(u, v, weight=weight)

all_shortest_paths = {}
for node in G.nodes():
    all_shortest_paths[node] = dijkstra(G, node)

for start, distances in all_shortest_paths.items():
    print(f"\nShortest paths from {start}:")
    for dest, dist in distances.items():
        print(f"  To {dest}: {dist}")
