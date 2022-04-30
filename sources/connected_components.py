from Graph import Graph


def connected_components(graph: Graph):
    def dfs(graph: Graph, v: int, ids: dict, count: int):
        ids[v] = count
        for w in graph.adj[v]:
            if w not in ids:
                dfs(graph, w, ids, count)

    ids = dict()
    count = 0

    for v in range(0, len(graph.adj)):
        if v not in ids:
            dfs(graph, v, ids, count)
            count += 1

    return count, ids


def count_connected_components(graph: Graph) -> int:
    count, _ = connected_components(graph)

    return count


def group_connected_components(graph: Graph) -> int:
    _, group = connected_components(graph)

    return group
