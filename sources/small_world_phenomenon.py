from Graph import Graph


def small_world_phenomenon(graph: Graph, vertices) -> list():

    def bfs(graph: Graph, vertex) -> None:
        marked = set()
        distTo = dict()

        queue = []
        distTo[vertex] = 0
        marked.add(vertex)
        queue.append(vertex)

        while len(queue):
            v = queue.pop(0)
            for w in graph.adj[v]:
                if w not in marked:
                    distTo[w] = distTo[v] + 1
                    marked.add(w)
                    queue.append(w)

        marked.remove(vertex)
        del distTo[vertex]

        return distTo

    distances = dict()

    for v in vertices:
        v_distances = bfs(graph, graph.uid_adj[v])

        for dist in v_distances.values():
            if dist not in distances:
                distances[dist] = 0
            distances[dist] += 1

    max_key = max(distances.keys())

    distances_list = [0] * max_key

    for dist, count in distances.items():
        distances_list[dist-1] = count

    return distances_list
