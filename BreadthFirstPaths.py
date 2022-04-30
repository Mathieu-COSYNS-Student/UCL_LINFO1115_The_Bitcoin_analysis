from asyncio.windows_events import NULL
from Graph import Graph
from json.encoder import INFINITY


class BreadthFirstPaths:

    marked = []
    distTo = []
    edgeTo = []

    def bfs(graph:Graph,vertexes,distTo,marked,edgeTo):
        queue = []
        for vertex in vertexes:
            marked[vertex] = True
            distTo[vertex] = 0
            queue.append(vertex)
        
        while len(queue):
            v = queue.pop(0)
            for w in graph.adj[v]:
                if not marked[w]:
                    edgeTo[w] = v
                    distTo[w] = distTo[v] + 1
                    marked[w] = True
                    queue.append(w)

    def __init__(self,graph:Graph,vertexes) -> None:
        marked = [False for i in vertexes]
        distTo = [0 for i in vertexes]
        edgeTo = [0 for i in vertexes]
        for i in vertexes:
            distTo[i] = INFINITY
        self.bfs(graph,vertexes,distTo,marked,edgeTo)
        pass


    def hasPathTo(self,v):
        return self.marked[v]

    def distanceTo(self,v):
        return self.distTo[v]

    
        



    
    