import numpy as np
from bridges import count_bridges, count_local_bridges
from connected_components import count_connected_components, get_bigest_component_vertices
from Graph import Graph
import sys
import pandas as pd
from plot import plot
from small_world_phenomenon import small_world_phenomenon
import networkx as nx

from triangles import count_triangles


def create_networkx_graph(df) -> nx.Graph:
    graph = nx.DiGraph()

    for _, row in df.iterrows():
        graph.add_edge(row['Source'], row['Target'])

    return graph


def main():
    sys.setrecursionlimit(2000)

    df = pd.read_csv('datasets/Project dataset.csv', index_col=0)

    # median = df['Timestamp'].median(axis=0)
    # graph, df_included, df_excluded = Graph.create(df, task=1)

    # print(count_connected_components(graph))
    # print(count_bridges(graph))
    # print(count_local_bridges(graph))

    # graph, df_included, df_excluded = Graph.create(df, task=2)

    # t, bt, wbt = count_triangles(graph)
    # nt = 0
    # balance_degree = (bt + (2/3 * wbt)) / t

    # new_triangles_over_time = np.array([nt])
    # balance_degree_over_time = np.array([balance_degree])
    # time = np.array([median])

    # for _, row in df_excluded.iterrows():
    #     t0, bt0, wbt0 = count_triangles(
    #         graph, edge=(row['Source'], row['Target']))
    #     graph.add_edge(row['Source'],
    #                    row['Target'],
    #                    meta={'weight': row['Weight']},
    #                    on_conflict=Graph.ON_CONFLICT_OVERRIDE_META)
    #     t1, bt1, wbt1 = count_triangles(
    #         graph, edge=(row['Source'], row['Target']))
    #     t += t1 - t0
    #     bt += bt1 - bt0
    #     wbt += wbt1 - wbt0
    #     nt += t1 - t0
    #     balance_degree = (bt + (2/3 * wbt)) / t
    #     new_triangles_over_time = np.append(new_triangles_over_time, nt)
    #     balance_degree_over_time = np.append(
    #         balance_degree_over_time, balance_degree)
    #     time = np.append(time, row['Timestamp'])

    # t, bt, wbt = count_triangles(graph)
    # balance_degree = (bt + (2/3 * wbt)) / t

    # plot(new_triangles_over_time, time, "Graph of accumulated triadic closure over time,\nstarting at the median timestamp until the end",
    #      "Timestamp", "Accumulated triadic closure", png="images/accumulated_triadic_closure.png", graphics=False)

    # plot(balance_degree_over_time, time, "Graph of the balance degree over time,\nstarting at the median timestamp until the end",
    #      "Timestamp", "Balance degree", png="images/balance_degree_over_time.png", graphics=False)

    graph, df_included, df_excluded = Graph.create(df, task=1)
    vertices = get_bigest_component_vertices(graph)
    print(count_connected_components(graph))
    print(count_bridges(graph))
    print(count_local_bridges(graph))
    print(len(vertices))

    graph, df_included, df_excluded = Graph.create(df, task=4)
    print(count_connected_components(graph))
    print(count_bridges(graph))
    print(count_local_bridges(graph))

    smphen = small_world_phenomenon(graph, vertices)

    plot(smphen, np.arange(1, len(smphen)+1), "Small world phenomenon", "Distances",
         "Number of paths", png="images/small_world_phenomenon.png", graphics=False)


if __name__ == "__main__":
    main()
