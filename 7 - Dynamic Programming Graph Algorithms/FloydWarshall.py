"""
    Floyd-Warshall Algorithm

    Function: Finds the distance between all pairs of vertices in a connected graph
    Time Complexity (Worst): O(v^3)
    Space Complexity (Auxiliary): O(v^2)

"""

from _.AdjacencyList import AdjacencyList
from typing import TypeVar
V = TypeVar('V')

def floyd_warshall(graph: AdjacencyList) -> dict[V, dict[V, int]]:
    
    # initialises vertices
    vertices = graph.get_vertices()

    # initialise distance matrix
    distance = {vertex: {} for vertex in vertices}
    for vertex in vertices:
        distance[vertex] = {child_vertex: float("inf") for child_vertex in vertices}

        # process adjacent edges and vertex itself
        distance[vertex][vertex] = 0
        for adjacent_vertex, weight in graph.adjacent_vertices(vertex):
            distance[vertex][adjacent_vertex] = weight

    # finds the shortest path from vertex j to k considering the intermediate vertex i
    for vertex_i in vertices:
        for vertex_j in vertices:
            for vertex_k in vertices:
                distance[vertex_j][vertex_k] = min(distance[vertex_j][vertex_k], distance[vertex_j][vertex_i] + distance[vertex_i][vertex_k])
    
    # checks for negative edge cycles and raises an error if found
    for vertex in vertices:
        if distance[vertex][vertex] < 0:
            raise Exception("Negative Edge Cycle Found in Graph")
    
    # returns distance matrix
    return distance

if __name__ == '__main__':
    vertices = ['A','B','C','D']
    edges = [('A','C',-2),('B','A',4),('B','C',3),('C','D',2),('D','B',-1)]
    graph = AdjacencyList(vertices, edges)
    print(f"Graph:\n{graph}\n")
    print("Distances:")
    distance = floyd_warshall(graph)
    for vertex in vertices:
        print(f"'{vertex}': {distance[vertex]}")
    graph.remove_edge(('C','D',2))
    graph.add_edge(('C','D',-3))
    try:
        distance = floyd_warshall(graph)
    except Exception:
        print("\nError: Negative Edge Cycle Found in Graph")
