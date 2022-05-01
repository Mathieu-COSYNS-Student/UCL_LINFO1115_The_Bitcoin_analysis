from Graph import Graph


def connected_components(graph: Graph):
    def dfs(graph: Graph, v: int, ids: dict, count: int):
        ids[graph.adj_uid[v]] = count
        for w in graph.adj[v]:
            if graph.adj_uid[w] not in ids:
                dfs(graph, w, ids, count)

    ids = dict()
    count = 0

    for v in range(0, len(graph.adj)):
        if graph.adj_uid[v] not in ids:
            dfs(graph, v, ids, count)
            count += 1

    return count, ids


def count_connected_components(graph: Graph) -> int:
    count, _ = connected_components(graph)

    return count


def group_connected_components(graph: Graph) -> dict:
    _, group = connected_components(graph)

    res = {}
    for i, v in group.items():
        res[v] = [i] if v not in res.keys() else res[v] + [i]

    return res


def get_bigest_component_vertices(graph: Graph) -> int:
    groups = group_connected_components(graph)
    bigest_component = None

    for _, group in groups.items():
        if bigest_component is None or len(group) > len(bigest_component):
            bigest_component = group

    return bigest_component
