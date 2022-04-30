import networkx as nx
from networkx.algorithms.components import number_connected_components
from networkx.algorithms.bridges import bridges, local_bridges
import matplotlib.pyplot as plt
import numpy as np
from bridges import count_bridges, count_local_bridges, remove_bridges
from connected_components import count_connected_components
from Graph import Graph
import sys
import pandas as pd
from plot import plot

from triangles import count_triangles


def create_networkx_graph(df, task=2) -> nx.Graph:
    graph = nx.Graph()

    for _, row in df.iterrows():
        graph.add_edge(row['Source'], row['Target'])

    return graph


def main():
    sys.setrecursionlimit(1500)

    df = pd.read_csv('datasets/Project dataset.csv', index_col=0)

    median = df['Timestamp'].median(axis=0)
    graph, df_included, df_excluded = Graph.create(
        df, task=3, on_conflict=Graph.ON_CONFLICT_OVERRIDE_META)
    networkx_graph = create_networkx_graph(df)

    t, bt, wbt = count_triangles(graph)
    nt = 0
    balance_degree = (bt + (2/3 * wbt)) / t

    new_triangles_over_time = np.array([nt])
    balance_degree_over_time = np.array([balance_degree])
    time = np.array([median])

    for _, row in df_excluded.iterrows():
        t0, bt0, wbt0 = count_triangles(
            graph, edge=(row['Source'], row['Target']))
        graph.add_edge(row['Source'],
                       row['Target'],
                       meta={'weight': row['Weight']},
                       on_conflict=Graph.ON_CONFLICT_OVERRIDE_META)
        t1, bt1, wbt1 = count_triangles(
            graph, edge=(row['Source'], row['Target']))
        t += t1 - t0
        bt += bt1 - bt0
        wbt += wbt1 - wbt0
        nt += t1 - t0
        balance_degree = (bt + (2/3 * wbt)) / t
        new_triangles_over_time = np.append(new_triangles_over_time, nt)
        balance_degree_over_time = np.append(
            balance_degree_over_time, balance_degree)
        time = np.append(time, row['Timestamp'])

    t, bt, wbt = count_triangles(graph)
    balance_degree = (bt + (2/3 * wbt)) / t

    plot(new_triangles_over_time, time, "Graph of accumulated triadic closure over time,\nstarting at the median timestamp until the end",
         "Timestamp", "Accumulated triadic closure", png="images/accumulated_triadic_closure.png", graphics=False)

    plot(balance_degree_over_time, time, "Graph of the balance degree over time,\nstarting at the median timestamp until the end",
         "Timestamp", "Balance degree", png="images/balance_degree_over_time.png", graphics=False)

    print(count_connected_components(graph))
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
    print(len([e for e in local_bridges(networkx_graph)]))


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