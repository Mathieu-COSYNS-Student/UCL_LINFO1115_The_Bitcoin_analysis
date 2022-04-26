from Graph import Graph


def count_local_bridges(graph: Graph) -> int:
    def has_long_path_bsf(graph: Graph, u: int, v: int, depth=0) -> bool:
        pass

    explored = dict()
    local_bridges = 0

    for v in graph.adj:
        for w in graph.adj[v]:
            if f'{v}-{w}' not in explored and f'{w}-{v}' not in explored:
                explored[f'{v}-{w}'] = True
                if has_long_path_bsf(graph, v, w):
                    local_bridges += 1

    return local_bridges
