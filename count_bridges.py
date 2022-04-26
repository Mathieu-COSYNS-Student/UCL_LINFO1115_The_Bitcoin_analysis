from Graph import Graph


def count_bridges(graph: Graph) -> int:
    def dfs(graph: Graph, u: int, v: int, bridges_count: int, count: int, pre: list, low: list):
        pre[v] = count
        count += 1
        low[v] = pre[v]

        for w in graph.adj[v]:
            if pre[w] == -1:
                bridges_count, count = dfs(
                    graph, v, w, bridges_count, count, pre, low)
                low[v] = min(low[v], low[w])
                if low[w] == pre[w]:
                    # print(f"{v}-{w} is a bridge")
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
                graph, v, v, bridges_count, count, pre, low)

    return bridges_count
