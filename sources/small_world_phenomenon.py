from ast import For
from json.encoder import INFINITY
from typing import Tuple

import numpy as np
from BreadthFirstPaths import BreadthFirstPaths
from Graph import Graph
from connected_components import get_bigest_component_vertexes






def small_world_phenomenon(graph: Graph) -> list():
    vertexes = get_bigest_component_vertexes(graph)
    bfs = BreadthFirstPaths(graph,vertexes)

    
    for v in vertexes:
        if bfs.hasPathTo(v):
            print(f'{}-{}')

    return distances
