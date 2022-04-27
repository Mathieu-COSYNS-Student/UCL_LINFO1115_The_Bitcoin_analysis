import csv
"""import networkx as nx
from networkx.algorithms.components import number_connected_components
from networkx.algorithms.bridges import bridges, local_bridges"""
import matplotlib.pyplot as plt
from bridges import count_bridges, count_local_bridges, remove_bridges
from connected_components import count_connected_components
from Graph import Graph
from triadic_closure import triadic_closure
import sys


def main():
    sys.setrecursionlimit(1500)

    graph = Graph()
    #networkx_graph = nx.Graph()

    file = open('localbridge.csv')
    csvreader = csv.reader(file)
    next(csvreader)  # skip header

    for row in csvreader:
        graph.add_edge(row[1], row[2])
       # networkx_graph.add_edge(row[1], row[2])

    file.close()
    print('Calculating the triadic closures : ')
    print(triadic_closure(graph))

    """print(count_connected_components(graph))
    print(number_connected_components(networkx_graph))

    print(count_bridges(graph))
    print(len([e for e in bridges(networkx_graph)]))

    print(count_local_bridges(graph))
    print(len([e for e in local_bridges(networkx_graph)]))

    print(count_bridges(remove_bridges(graph)))
    for e in bridges(networkx_graph):
        networkx_graph.remove_edge(*e)
    print(len([e for e in bridges(networkx_graph)]))

    print(count_connected_components(remove_bridges(graph)))
    print(number_connected_components(networkx_graph))

    print(count_local_bridges(remove_bridges(graph)))
    print(len([e for e in local_bridges(networkx_graph)]))"""


def graph_image(networkx_graph):
    options = {
        "font_size": 8,
        "node_size": 200,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 1,
        "width": 1,
    }
    nx.draw_networkx(networkx_graph, **options)

    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
