"""
    Breadth First Search

    Function: Traverses all vertices of an unweighted graph
    Time Complexity (Worst): O(v+e)
    Space Complexity (Auxiliary): O(v)

"""

from AdjacencyList import AdjacencyList
from typing import TypeVar
V = TypeVar('V')

def breadth_first_search(graph: AdjacencyList, source: V) -> list[V]:

    # initialises discovered and visited lists
    discovered = [source]
    order = []

    # traverses the graph until there are no more discovered vertices
    while len(discovered) != 0:

        # sets current vertex to the first vertex in the discovered list
        current_vertex = discovered[0]

        # adds every undiscovered and unvisited adjacent vertex to discovered list
        for adjacent_vertex, _ in graph.adjacent_vertices(current_vertex):
            if adjacent_vertex not in discovered and adjacent_vertex not in order:
                discovered.append(adjacent_vertex)
        
        # removes current vertex from discovered list and adds it to visited list
        order.append(discovered.pop(0))

    # returns ordered list of vertices
    return order

if __name__ == '__main__':
    vertices = ['A','B','C','D','E','F','G','H']
    edges = [('A','B',1),('A','C',1),('B','A',1),('B','E',1),('B','F',1),('C','A',1),('C','D',1),('D','C',1),('E','B',1),
             ('E','G',1),('E','H',1),('F','B',1),('F','G',1),('G','E',1),('G','F',1),('G','H',1),('H','E',1),('H','G',1),]
    graph = AdjacencyList(vertices, edges)
    print(f"Graph:\n{graph}\n")
    print(f"BFS Traversal:\n{breadth_first_search(graph, 'A')}")
    