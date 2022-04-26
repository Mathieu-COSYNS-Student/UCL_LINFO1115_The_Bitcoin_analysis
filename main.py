import csv
import networkx as nx
from networkx.algorithms.components import number_connected_components
from networkx.algorithms.bridges import bridges, local_bridges
import matplotlib.pyplot as plt
from count_bridges import count_bridges
from connected_components import count_connected_components
from Graph import Graph
import sys


def main():
    sys.setrecursionlimit(1500)

    graph = Graph()
    networkx_graph = nx.Graph()

    file = open('localbridge.csv')
    csvreader = csv.reader(file)
    next(csvreader)  # skip header

    for row in csvreader:
        graph.add_edge(row[1], row[2])
        networkx_graph.add_edge(row[1], row[2])

    file.close()

    print(count_connected_components(graph))
    print(number_connected_components(networkx_graph))

    print(count_bridges(graph))
    print(len([b for b in bridges(networkx_graph)]))

    print(len([b for b in local_bridges(networkx_graph)]))

    # for b in local_bridges(networkx_graph):
    #    print(b)

    # options = {
    #     "font_size": 10,
    #     "node_size": 300,
    #     "node_color": "white",
    #     "edgecolors": "black",
    #     "linewidths": 2,
    #     "width": 2,
    # }
    # nx.draw_networkx(networkx_graph, **options)

    # ax = plt.gca()
    # ax.margins(0.20)
    # plt.axis("off")
    # plt.savefig("test.png")


if __name__ == "__main__":
    main()
