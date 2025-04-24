import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph(name="City Infrastructure Network")

locations = {
    "Train Station": (0, 0),
    "City Center": (2, 2),
    "University": (5, 3),
    "Hospital": (4, 0),
    "Stadium": (7, 2),
    "Market": (3, 4),
    "Library": (6, 4),
    "Park": (1, 4),
    "Mall": (6, 1),
    "Residential Area": (1, 1),
}

for name, pos in locations.items():
    G.add_node(name, pos=pos)

roads = [
    ("Train Station", "City Center"),
    ("Train Station", "Hospital"),
    ("City Center", "University"),
    ("City Center", "Market"),
    ("University", "Library"),
    ("Library", "Market"),
    ("Hospital", "Mall"),
    ("Mall", "Stadium"),
    ("Stadium", "University"),
    ("Park", "Market"),
    ("Park", "Residential Area"),
    ("Residential Area", "City Center"),
]

G.add_edges_from(roads)

plt.figure(figsize=(12, 8))
pos = nx.get_node_attributes(G, 'pos')
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightblue', font_size=10, font_weight='bold')
plt.title("City Infrastructure Graph")
plt.savefig("task_1_graph.png")
plt.show()

print("\nGraph Analysis:")
print(f"Graph name: {G.name}")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Average degree: {sum(dict(G.degree()).values()) / G.number_of_nodes():.2f}")
print(f"Average shortest path length: {nx.average_shortest_path_length(G):.2f}")
print(f"Clustering coefficient: {nx.average_clustering(G):.2f}")

print("\nCentrality Measures:")
print("Degree Centrality:")
for node, centrality in nx.degree_centrality(G).items():
    print(f"  {node}: {centrality:.2f}")

print("\nBetweenness Centrality:")
for node, centrality in nx.betweenness_centrality(G).items():
    print(f"  {node}: {centrality:.2f}")

print("\nCloseness Centrality:")
for node, centrality in nx.closeness_centrality(G).items():
    print(f"  {node}: {centrality:.2f}")
