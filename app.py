import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

graph = {
    "Director": ["Finance", "Technology", "Operations"],
    "Finance": ["Budgeting", "Accounting"],
    "Technology": ["Software", "Hardware", "Cybersecurity"],
    "Operations": ["Logistics", "Procurement"],
    "Budgeting": ["Planning", "Audit"],
    "Accounting": [],
    "Software": ["AI Lab", "Web Development"],
    "Hardware": ["R&D"],
    "Cybersecurity": [],
    "Logistics": ["Domestic", "International"],
    "Procurement": ["Vendors"],
    "Planning": [],
    "Audit": [],
    "AI Lab": [],
    "Web Development": [],
    "R&D": [],
    "Domestic": [],
    "International": [],
    "Vendors": []
}

G = nx.DiGraph()
for node, neighbors in graph.items():
    for n in neighbors:
        G.add_edge(node, n)

pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2500, font_size=10, arrows=True)
plt.show()

def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

bfs_path = bfs(graph, "Director", "R&D")
dfs_path = dfs(graph, "Director", "R&D")

print("BFS Path:", bfs_path)
print("DFS Path:", dfs_path)

bfs_edges = list(zip(bfs_path, bfs_path[1:]))
dfs_edges = list(zip(dfs_path, dfs_path[1:]))

plt.figure(figsize=(10,6))
nx.draw(G, pos, with_labels=True, node_color="lightgray", node_size=2500, arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color="green", width=2)
plt.title("BFS Path")
plt.show()

plt.figure(figsize=(10,6))
nx.draw(G, pos, with_labels=True, node_color="lightgray", node_size=2500, arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color="red", width=2)
plt.title("DFS Path")
plt.show()
