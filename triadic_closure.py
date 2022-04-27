from Graph import Graph


def triadic_closure(graph: Graph):
    number_of_triadic_closure = 0
    visited = dict()

    for V in graph.adj:
        for v in V:
            for w in graph.adj[v]:
                for n in graph.adj[v]:
                    if n != w and n not in graph.adj[w] and f'{n}-{w}' not in visited and f'{w}-{n}' not in visited:
                        number_of_triadic_closure += 1
                        visited[f'{w}-{n}'] = True
    return number_of_triadic_closure


"""
1.	Start with graph G=(V,E) with |V|>0 and |E|>0
2.	Choose a random pair of nodes x, y that are non-adjacent and share a common neighbor
3.	If no such pair of nodes x, y exists, then we’re done
4.	Add element {x,y} to set E
5.	Go to step 2
"""