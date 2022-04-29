from typing import Any

from pyparsing import Literal
from Graph import Graph


def are_neighbors(a: Any, c: Any, graph: Graph):
    return a in graph.adj[c]

def are_already_triadic_closures(a: Any, c: Any, map_of_triadic_closures: dict ):
    return  f'{a}-{c}' in map_of_triadic_closures or f'{c}-{a}' in map_of_triadic_closures

def is_triadic_closure(a: Any, c: Any, graph: Graph, map_of_triadic_closures: dict, closures: Literal):
    if a != c and not are_neighbors(a,c,graph) and not are_already_triadic_closures(a,c,map_of_triadic_closures):
        map_of_triadic_closures[f'{a}-{c}'] = True
    elif are_already_triadic_closures(a,c,map_of_triadic_closures):
        closures+=1
        print(closures)
    return closures


def triadic_closure(graph: Graph):
    number_of_triadic_closure = 0
    map_of_triadic_closures = dict()
    for V in graph.adj:
        for v in V:
            for w in graph.adj[v]:
                for n in graph.adj[v]:
                    number_of_triadic_closure = is_triadic_closure(
                        w, n, graph, map_of_triadic_closures, number_of_triadic_closure)

    return number_of_triadic_closure





"""
1.	Start with graph G=(V,E) with |V|>0 and |E|>0
2.	Choose a random pair of nodes x, y that are non-adjacent and share a common neighbor
3.	If no such pair of nodes x, y exists, then we’re done
4.	Add element {x,y} to set E
5.	Go to step 2
"""