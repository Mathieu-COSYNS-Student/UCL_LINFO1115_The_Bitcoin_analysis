from collections import deque
from copy import deepcopy
from Graph import Graph


def count_bridges(graph: Graph, remove=False) -> int:
    def dfs(graph: Graph, u: int, v: int, remove: bool, bridges_count: int, count: int, pre: list, low: list):
        pre[v] = count
        count += 1
        low[v] = pre[v]

        for w in graph.adj[v]:
            if pre[w] == -1:
                bridges_count, count = dfs(
                    graph, v, w, remove, bridges_count, count, pre, low)
                low[v] = min(low[v], low[w])
                if low[w] == pre[w]:
                    # print(f"{v}-{w} is a bridge")
                    if remove:
                        graph.remove_edge(v, w)
                    bridges_count += 1
            elif w != u:
                low[v] = min(low[v], pre[w])

        return bridges_count, count

    bridges_count = 0
    count = 0
    pre = list()
    low = list()

    for _ in range(0, len(graph.adj)):
        pre.append(-1)
        low.append(-1)

    for v in range(0, len(graph.adj)):
        if pre[v] == -1:
            bridges_count, count = dfs(
                graph, v, v, remove, bridges_count, count, pre, low)

    return bridges_count


def remove_bridges(graph: Graph) -> int:
    new_graph = deepcopy(graph)
    count_bridges(new_graph, remove=True)

    return new_graph


def count_local_bridges(graph: Graph) -> int:
    def has_long_path_bsf(graph: Graph, u: int, v: int, limit, depth=0) -> bool or None:
        if u == v:
            return False
        elif depth == limit:
            return True
        else:
            cutoff_occurred = False
            for w in graph.adj[u]:
                if v == w and depth == 0:
                    continue
                result = has_long_path_bsf(graph, w, v, limit, depth + 1)
                if result:
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return True if cutoff_occurred else None

    explored = dict()
    local_bridges = 0

    for V in graph.adj:
        for v in V:
            for w in graph.adj[v]:
                if f'{v}-{w}' not in explored and f'{w}-{v}' not in explored:
                    explored[f'{v}-{w}'] = True
                    if has_long_path_bsf(graph, v, w, limit=2) != False:
                        local_bridges += 1

    return local_bridges
