"""
Завдання 1
Створіть граф за допомогою бібліотеки networkX для моделювання певної реальної мережі 
(наприклад, транспортної мережі міста, соціальної мережі, інтернет-топології).
Візуалізуйте створений граф, проведіть аналіз основних характеристик (наприклад, 
кількість вершин та ребер, ступінь вершин).

Завдання 2
Напишіть програму, яка використовує алгоритми DFS і BFS для знаходження шляхів у графі,
який було розроблено у першому завданні.
Далі порівняйте результати виконання обох алгоритмів для цього графа, висвітлить різницю 
в отриманих шляхах. Поясніть, чому шляхи для алгоритмів саме такі.

Завдання 3
Реалізуйте алгоритм Дейкстри для знаходження найкоротшого шляху в розробленому графі: 
додайте у граф ваги до ребер та знайдіть найкоротший шлях між всіма вершинами графа.
"""

import networkx as nx
from get_subway_info import get_subway_info
from dfs_search import dfs_recursive
from bfs_search import bfs_recursive
from collections import deque
import matplotlib.pyplot as plt



if __name__ == "__main__":
    
    # task 1 - create graph data - Kyiv subway
    G = nx.Graph()
    stations, edges, color_map = get_subway_info("subway.txt")
    weighted_edges = [(edge[0], edge[1], {"weight": edge[2]}) for edge in edges]
    G.add_nodes_from(stations)
    G.add_edges_from(weighted_edges)

    # Visualization
    pos = nx.spring_layout(G)
    #pos = nx.shell_layout(G) 
    edge_labels = nx.get_edge_attributes(G, 'weight')
    node_colors = [color_map[node] for node in G.nodes()]
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000, edge_color="gray", font_size=8)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Київський метрополітен")
    plt.show()

    # Graph data analyziz
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    degrees = dict(G.degree())
    avg_degree = sum(degrees.values()) / num_nodes

    print(f"Number of Nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")
    print(f"Degrees: {degrees}")
    print(f"Average degree: {avg_degree:.2f}")

    weights = nx.get_edge_attributes(G, 'weight')
    total_weight = sum(weights.values())
    print(f"Edges weights: {weights}")
    print(f"Total edges weight: {total_weight}")


    # task 2
    print("Breadth First Search:")
    dfs_recursive(G, "Героїв Дніпра")

    print("Depth First Search:")
    bfs_recursive(G, deque(["Героїв Дніпра"]))

    # task 3
    shortest_paths = {}
    for node in G.nodes():
        shortest_paths[node] = nx.single_source_dijkstra_path_length(G, node, weight='weight')

    for source, targets in shortest_paths.items():
        for target, distance in targets.items():
            print(f"The shortest way from {source} to {target} takes {distance} min")

    # Shortest path between requested stations
    source = "Почайна"
    target="Вокзальна"
    shortest_path = nx.shortest_path(G, source=source, target=target, weight='weight')
    shortest_path_length = nx.shortest_path_length(G, source=source, target=target, weight='weight')
    print(f"The shortest way from {source} to {target}: {shortest_path}")
    print(f"Time of the shortest way (minutes): {shortest_path_length}")