"""
    Shortest Path BFS

    Function: Finds the distance of all vertices from a single source of an unweighted graph
    Time Complexity (Worst): O(v+e)
    Space Complexity (Auxiliary): O(v)

"""

from AdjacencyList import AdjacencyList
from typing import TypeVar
V = TypeVar('V')

def shortest_path_bfs(graph: AdjacencyList, source: V) -> dict[V, int]:

    # initialises lists
    distance = {vertex: float("inf") for vertex in graph.get_vertices()}
    queue = []
    predeccessor = {vertex: None for vertex in graph.get_vertices()}

    # processes source vertex
    distance[source] = 0
    queue.append(source)

    # traverses the graph until no more vertices
    while len(queue) != 0:

        # sets current vertex to first vertex in queue
        current_vertex = queue.pop(0)

        # checks every adjacent vertex and proccesses undiscovered vertices
        for adjacent_vertex, _ in graph.adjacent_vertices(current_vertex):
            if distance[adjacent_vertex] == float("inf"):

                # assigns adjacent vertex distance of current vertex plus one
                distance[adjacent_vertex] = distance[current_vertex] + 1

                # stores the vertex that discovered adjacent vertex
                predeccessor[adjacent_vertex] = current_vertex

                # adds adjacent vertex to queue
                queue.append(adjacent_vertex)

    # returns dictionary of vertices and their distances from source
    return distance

if __name__ == '__main__':
    vertices = ['A','B','C','D','E','F','G','H']
    edges = [('A','B',1),('A','C',1),('B','A',1),('B','E',1),('B','F',1),('C','A',1),('C','D',1),('D','C',1),('E','B',1),
             ('E','G',1),('E','H',1),('F','B',1),('F','G',1),('G','E',1),('G','F',1),('G','H',1),('H','E',1),('H','G',1),]
    graph = AdjacencyList(vertices, edges)
    print(f"Graph:\n{graph}\n")
    print(f"Distance from A:\n{shortest_path_bfs(graph, 'A')}")
    