from typing import Tuple
from Graph import Graph


def count_triangles(graph: Graph, node: int = None, edge: Tuple[str, str] = None, explored_nodes=set()) -> int:

    triangles = 0
    balanced_triangles = 0
    weakly_balanced_triangles = 0

    if node != None:
        explored = set([node])
        for v in graph.adj[node]:
            explored.add(v)
            t, bt, wbt = count_triangles(
                graph, edge=(graph.adj_uid[node], graph.adj_uid[v]), explored_nodes=explored)
            triangles += t
            balanced_triangles += bt
            weakly_balanced_triangles += wbt

        return triangles, balanced_triangles, weakly_balanced_triangles
    elif edge != None:
        if not graph.exist_edge(edge[0], edge[1]):
            return 0, 0, 0
        e0_index = graph.uid_adj[edge[0]]
        e1_index = graph.uid_adj[edge[1]]
        edge_sign_negative = True if graph.get_edge_meta(edge[0], edge[1])[
            'weight'] < 0 else False
        for w in graph.adj[e0_index]:
            if w in explored_nodes:
                continue
            w_uid = graph.adj_uid[w]
            v_to_w_sign_negative = True if graph.get_edge_meta(edge[0], w_uid)[
                'weight'] < 0 else False
            if w in graph.adj[e1_index]:
                node_to_w_sign_negative = True if graph.get_edge_meta(edge[1], w_uid)[
                    'weight'] < 0 else False
                triangles += 1
                if (edge_sign_negative, v_to_w_sign_negative, node_to_w_sign_negative) == (False, False, False) \
                        or (edge_sign_negative, v_to_w_sign_negative, node_to_w_sign_negative) == (False, True, True) \
                        or (edge_sign_negative, v_to_w_sign_negative, node_to_w_sign_negative) == (True, False, True) \
                        or (edge_sign_negative, v_to_w_sign_negative, node_to_w_sign_negative) == (True, True, False):
                    balanced_triangles += 1
                if (edge_sign_negative, v_to_w_sign_negative, node_to_w_sign_negative) == (True, True, True):
                    weakly_balanced_triangles += 1
        return triangles, balanced_triangles, weakly_balanced_triangles
    else:
        explored = set()
        for V in graph.adj:
            for v in V:
                if v not in explored:
                    explored.add(v)
                    t, bt, wbt = count_triangles(graph, node=v)
                    triangles += t
                    balanced_triangles += bt
                    weakly_balanced_triangles += wbt

    return int(triangles / 3), int(balanced_triangles / 3), int(weakly_balanced_triangles / 3)
