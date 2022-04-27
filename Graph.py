class Graph:

    def __init__(self) -> None:
        """
        Initializes an empty graph.
        """
        self.V = 0
        self.E = 0
        self.adj = list()
        self.uid_adj = dict()
        self.adj_uid = dict()
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

    def add_edge(self, v: str, w: str) -> None:
        """
        Add an edge v-w in the graph.
        """
        self.add_vertex(v)
        self.add_vertex(w)
        self.adj[self.uid_adj[v]].append(self.uid_adj[w])
        self.adj[self.uid_adj[w]].append(self.uid_adj[v])
        self.E += 1

    def remove_edge(self, v: int, w: int) -> None:
        self.adj[v] = [i for i in self.adj[v] if i != w]
        self.adj[w] = [i for i in self.adj[w] if i != v]
