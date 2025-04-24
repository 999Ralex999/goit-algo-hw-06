import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.Graph(name="City Network")

locations = {
    "Train Station": (0, 0),
    "City Center": (2, 2),
    "Independence Square": (4, 2),
    "University": (6, 2),
    "Market": (3, 5),
    "Hospital": (3, 0),
    "Park": (6, 0),
    "Stadium": (8, 4),
    "Residential Area": (1, 1),
    "Library": (7, 5),
    "Mall": (6, -2)
}

edges = [
    ("Train Station", "City Center"),
    ("City Center", "Independence Square"),
    ("Independence Square", "Market"),
    ("Market", "Park"),
    ("Park", "University"),
    ("University", "Hospital"),
    ("Stadium", "Park"),
    ("Stadium", "Hospital"),
    ("Park", "Residential Area"),
    ("Residential Area", "City Center"),
    ("University", "Library"),
    ("Hospital", "Mall"),
    ("Stadium", "Mall"),
]

G.add_nodes_from(locations)
G.add_edges_from(edges)

def dfs_path(graph, start, goal):
    visited = set()
    path = []

    def dfs(v):
        if v in visited:
            return False
        visited.add(v)
        path.append(v)
        if v == goal:
            return True
        for neighbor in graph[v]:
            if dfs(neighbor):
                return True
        path.pop()
        return False

    dfs(start)
    return path

def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited and neighbor not in [p[0] for p in queue]:
                queue.append((neighbor, path + [neighbor]))
    return []

start_node = "Train Station"
goal_node = "Library"

dfs_result = dfs_path(G, start_node, goal_node)
bfs_result = bfs_path(G, start_node, goal_node)

print("DFS path:", " -> ".join(dfs_result))
print("BFS path:", " -> ".join(bfs_result))

pos = locations
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_weight='bold')

if dfs_result:
    dfs_edges = [(dfs_result[i], dfs_result[i+1]) for i in range(len(dfs_result)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color='red', width=2)

if bfs_result:
    bfs_edges = [(bfs_result[i], bfs_result[i+1]) for i in range(len(bfs_result)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color='green', width=2, style='dashed')

plt.title(f'DFS (red) and BFS (green dashed) from "{start_node}" to "{goal_node}"')
plt.tight_layout()
plt.savefig("task2_graph_paths.png")
plt.show()
