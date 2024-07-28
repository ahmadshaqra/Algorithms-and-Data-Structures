"""
    Transitive Closure

    Function: Finds all paths that are possible between two vertices in a graph
    Time Complexity (Worst): O(v^3)
    Space Complexity (Auxiliary): O(v^2)

"""

from _.AdjacencyList import AdjacencyList
from typing import TypeVar
V = TypeVar('V')

def transitive_closure(graph: AdjacencyList) -> dict[V, dict[V, int]]:

    # initialises vertices
    vertices = graph.get_vertices()

    # initialise transitive matrix
    transitive = {vertex: {} for vertex in vertices}
    for vertex_i in vertices:
        transitive[vertex_i] = {vertex_j: False for vertex_j in vertices}

        # process adjacent edges
        for vertex_j in vertices:
            if graph.check_edge(vertex_i, vertex_j) or vertex_i == vertex_j:
                transitive[vertex_i][vertex_j] = True

    # finds if a path from vertex j to k is possible considering the intermediate vertex i
    for vertex_i in vertices:
        for vertex_j in vertices:
            for vertex_k in vertices:
                transitive[vertex_j][vertex_k] = transitive[vertex_j][vertex_k] or (transitive[vertex_j][vertex_i] and transitive[vertex_i][vertex_k])
                
    # returns transitive matrix
    return transitive

if __name__ == '__main__':
    vertices = ['S','U','T','V','X']
    edges = [('S','V',1),('U','V',1),('T','U',1),('V','X',1)]
    graph = AdjacencyList(vertices, edges)
    print(f"Graph:\n{graph}\n")
    print("Transitivity Matrix:")
    transitive = transitive_closure(graph)
    for vertex in vertices:
        print(f"'{vertex}': {transitive[vertex]}")
