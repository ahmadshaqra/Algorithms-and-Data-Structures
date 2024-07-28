"""
    Depth First Search

    Function: Traverses all vertices of an unweighted graph
    Time Complexity (Worst): O(v+e)
    Space Complexity (Auxiliary): O(v+e)

"""

from AdjacencyList import AdjacencyList
from typing import TypeVar
V = TypeVar('V')

def depth_first_search(graph: AdjacencyList, source: V, order: list[V] = None, visited: dict[V, bool] = None) -> list[V]:

    # initialises order and visited
    if order == None:
        order = []
    if visited == None:
        visited = {vertex: False for vertex in graph.get_vertices()}
    
    # adds source vertex to the order list
    order.append(source)
    visited[source] = True

    # checks each adjacent vertex of the current vertex
    for adjacent_vertex, _ in graph.adjacent_vertices(source):
        
        # if the adjacent vertex was not visited a depth first search is called on that vertex
        if not visited[adjacent_vertex]:
            depth_first_search(graph, adjacent_vertex, order, visited)

    # returns ordered list of vertices
    return order

if __name__ == '__main__':
    vertices = ['A','B','C','D','E','F','G','H']
    edges = [('A','B',1),('A','C',1),('B','A',1),('B','E',1),('B','F',1),('C','A',1),('C','D',1),('D','C',1),('E','B',1),
             ('E','G',1),('E','H',1),('F','B',1),('F','G',1),('G','E',1),('G','F',1),('G','H',1),('H','E',1),('H','G',1),]
    graph = AdjacencyList(vertices, edges)
    print(f"Graph:\n{graph}\n")
    print(f"DFS Traversal:\n{depth_first_search(graph, 'A')}")
    