from matplotlib import pyplot as plt


class Graph:

    ON_CONFLICT_IGNORE = 0
    ON_CONFLICT_OVERRIDE_META = 1

    @staticmethod
    def create(df, task=None, on_conflict=None):
        graph = Graph()

        df = df.sort_values(by='Timestamp')
        df_included = df
        df_excluded = df[0:0]

        if task == 2 or task == 3:
            median = df['Timestamp'].median(axis=0)
            df_included = df[df['Timestamp'] < median]
            df_excluded = df[df['Timestamp'] >= median]

        for _, row in df_included.iterrows():
            graph.add_edge(row['Source'],
                           row['Target'],
                           meta={'weight': row['Weight']},
                           on_conflict=on_conflict)

        return graph, df_included, df_excluded

    def __init__(self) -> None:
        """
        Initializes an empty graph.
        """
        self.V = 0
        self.E = 0
        self.adj = list()
        self.uid_adj = dict()
        self.adj_uid = dict()
        self.edge_meta = dict()
        pass

    def exist_vertex(self, v: str) -> bool:
        """
        Check if vertex v exist in the graph.
        """
        return v in self.uid_adj

    def add_vertex(self, v: str) -> None:
        """
        Add vertex v if v is not already in the graph.
        """
        if self.exist_vertex(v):
            return
        index = len(self.adj)
        self.uid_adj[v] = index
        self.adj_uid[index] = v
        self.adj.append(list())
        self.V += 1

    def exist_edge(self, v: str, w: str) -> None:
        if not self.exist_vertex(v):
            return False
        if not self.exist_vertex(w):
            return False
        return self.uid_adj[w] in self.adj[self.uid_adj[v]]

    def add_edge(self, v: str, w: str, meta=None, on_conflict=None) -> None:
        """
        Add an edge v-w in the graph.
        """
        self.add_vertex(v)
        self.add_vertex(w)
        if on_conflict == Graph.ON_CONFLICT_IGNORE and self.exist_edge(v, w):
            return
        if on_conflict == Graph.ON_CONFLICT_OVERRIDE_META and self.exist_edge(v, w):
            self.edge_meta[f'{v}-{w}'] = meta
            self.edge_meta[f'{w}-{v}'] = meta
            return
        self.adj[self.uid_adj[v]].append(self.uid_adj[w])
        self.adj[self.uid_adj[w]].append(self.uid_adj[v])
        self.edge_meta[f'{v}-{w}'] = meta
        self.edge_meta[f'{w}-{v}'] = meta
        self.E += 1

    def get_edge_meta(self, v: str, w: str):
        return self.edge_meta[f'{v}-{w}']

    def remove_edge(self, v: int, w: int) -> None:
        self.adj[v] = [i for i in self.adj[v] if i != w]
        self.adj[w] = [i for i in self.adj[w] if i != v]


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


def count_triangles(graph: Graph, node: int = None, edge=None, explored_nodes=set()) -> int:

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


def plot(data, time, title=None, xlabel=None, ylabel=None, png=None, graphics=True):

    plt.plot(time, data, "o-")

    plt.title(title)

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # plt.xlim(left=0)
    # plt.ylim(bottom=0)

    plt.grid(True)

    if png != None:
        plt.savefig(png)

    if graphics:
        plt.show()

    plt.close()
