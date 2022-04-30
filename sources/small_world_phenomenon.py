from typing import Tuple

import numpy as np
from Graph import Graph
from connected_components import get_bigest_component_vertexes


def small_world_phenomenon(graph: Graph) -> list():
    distances = [0, 0]
    explored = dict()

    vertexes = get_bigest_component_vertexes(graph)

    for v in vertexes:
        pass

    return distances
