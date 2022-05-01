class Graph:

    TYPE_UNDIRECTED = 0
    TYPE_DIRECTED = 1

    ON_CONFLICT_IGNORE = 0
    ON_CONFLICT_OVERRIDE_META = 1

    @staticmethod
    def create(df, task=None):
        graph = Graph(type=Graph.TYPE_DIRECTED if task ==
                      4 else Graph.TYPE_UNDIRECTED)

        df = df.sort_values(by='Timestamp')
        df_included = df
        df_excluded = df[0:0]
        on_conflict = None

        if task == 2 or task == 3:
            median = df['Timestamp'].median(axis=0)
            df_included = df[df['Timestamp'] < median]
            df_excluded = df[df['Timestamp'] >= median]

        if task == 2 or task == 4:
            on_conflict = Graph.ON_CONFLICT_IGNORE
        if task == 3:
            on_conflict = Graph.ON_CONFLICT_OVERRIDE_META

        for _, row in df_included.iterrows():
            graph.add_edge(row['Source'],
                           row['Target'],
                           meta={'weight': row['Weight']},
                           on_conflict=on_conflict)

        return graph, df_included, df_excluded

    def __init__(self, type=TYPE_UNDIRECTED) -> None:
        """
        Initializes an empty graph.
        """
        self.type = type
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
            if self.type == Graph.TYPE_UNDIRECTED:
                self.edge_meta[f'{w}-{v}'] = meta
            return
        self.adj[self.uid_adj[v]].append(self.uid_adj[w])
        if self.type == Graph.TYPE_UNDIRECTED:
            self.adj[self.uid_adj[w]].append(self.uid_adj[v])
        self.edge_meta[f'{v}-{w}'] = meta
        if self.type == Graph.TYPE_UNDIRECTED:
            self.edge_meta[f'{w}-{v}'] = meta
        self.E += 1

    def get_edge_meta(self, v: str, w: str):
        return self.edge_meta[f'{v}-{w}']

    def remove_edge(self, v: int, w: int) -> None:
        self.adj[v] = [i for i in self.adj[v] if i != w]
        if self.type == Graph.TYPE_UNDIRECTED:
            self.adj[w] = [i for i in self.adj[w] if i != v]
