import networkx as nx
import matplotlib.pyplot as plt
import heapq

graph = {
    "Director": [("Finance", 2), ("Technology", 1), ("Operations", 3)],
    "Finance": [("Budgeting", 1), ("Accounting", 2)],
    "Technology": [("Software", 2), ("Hardware", 3), ("Cybersecurity", 4)],
    "Operations": [("Logistics", 1), ("Procurement", 2)],
    "Budgeting": [("Planning", 1), ("Audit", 2)],
    "Accounting": [],
    "Software": [("AI Lab", 2), ("Web Development", 3)],
    "Hardware": [("R&D", 2)],
    "Cybersecurity": [],
    "Logistics": [("Domestic", 1), ("International", 2)],
    "Procurement": [("Vendors", 1)],
    "Planning": [],
    "Audit": [],
    "AI Lab": [],
    "Web Development": [],
    "R&D": [],
    "Domestic": [],
    "International": [],
    "Vendors": []
}

heuristic = {
    "Director": 6,
    "Finance": 4,
    "Technology": 3,
    "Operations": 5,
    "Hardware": 2,
    "R&D": 0,
    "Budgeting": 3,
    "Software": 3,
    "Cybersecurity": 4,
    "Accounting": 5,
    "Planning": 5,
    "Audit": 5,
    "AI Lab": 4,
    "Web Development": 3,
    "Logistics": 4,
    "Procurement": 3,
    "Domestic": 4,
    "International": 5,
    "Vendors": 4
}

G = nx.DiGraph()
for node, edges in graph.items():
    for neighbor, cost in edges:
        G.add_edge(node, neighbor, weight=cost)

def uniform_cost_search(graph, start, goal):
    queue = [(0, [start])]
    visited = set()
    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]
        if node == goal:
            return path, cost
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(queue, (cost + edge_cost, path + [neighbor]))
    return None, float("inf")

def a_star(graph, start, goal, heuristic):
    queue = [(heuristic[start], 0, [start])]
    visited = set()
    while queue:
        f, g, path = heapq.heappop(queue)
        node = path[-1]
        if node == goal:
            return path, g
        if node not in visited:
            visited.add(node)
            for neighbor, edge_cost in graph[node]:
                new_g = g + edge_cost
                new_f = new_g + heuristic.get(neighbor, 0)
                heapq.heappush(queue, (new_f, new_g, path + [neighbor]))
    return None, float("inf")

ucs_path, ucs_cost = uniform_cost_search(graph, "Director", "R&D")
a_star_path, a_star_cost = a_star(graph, "Director", "R&D", heuristic)

pos = nx.spring_layout(G, seed=42)
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2500, font_size=9, arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'))

ucs_edges = list(zip(ucs_path, ucs_path[1:]))
a_star_edges = list(zip(a_star_path, a_star_path[1:]))

nx.draw_networkx_edges(G, pos, edgelist=ucs_edges, edge_color="orange", width=3, label="UCS Path")
nx.draw_networkx_edges(G, pos, edgelist=a_star_edges, edge_color="purple", width=2, style="dashed", label="A* Path")

plt.legend()
plt.title("Uniform Cost Search and A* Search Paths")
plt.show()

print("UCS Path:", ucs_path, " | Total Cost:", ucs_cost)
print("A* Path:", a_star_path, " | Total Cost:", a_star_cost)
