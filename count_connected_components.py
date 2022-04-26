from Graph import Graph


def count_connected_components(graph):
    def dfs(graph: Graph, v: int, marked: dict):
        marked[v] = True
        for w in graph.adj[v]:
            if w not in marked:
                dfs(graph, w, marked)

    marked = dict()
    count = 0

    for v in range(0, len(graph.adj)):
        if v not in marked:
            dfs(graph, v, marked)
            count += 1

    return count
