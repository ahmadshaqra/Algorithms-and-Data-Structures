"""
    Topological Sort DFS

    Function: Returns a topological sort of a directed acyclic graph (DAG)
    Time Complexity (Worst): O(v+e)
    Space Complexity (Auxiliary): O(v+e)

"""

from AdjacencyList import AdjacencyList
from typing import TypeVar
V = TypeVar('V')

def topological_sort_dfs(graph: AdjacencyList) -> list[V]:

    # initialises order and visited lists
    order = []
    visited = {vertex: False for vertex in graph.get_vertices()}
    
    # loops through each vertex and checks if it has been visited
    for vertex in graph.get_vertices():
        if not visited[vertex]:

            # runs a depth first search
            dfs(graph, vertex, order, visited)
    
    # reverses are returns the sorted vertices
    order.reverse()
    return order

def dfs(graph: AdjacencyList, source: V, order: list[V], visited: dict[V, bool]) -> None:

    # marks source vertex as visited
    visited[source] = True

    # checks each adjacent vertex of the current vertex
    for adjacent_vertex, _ in graph.adjacent_vertices(source):

        # if the adjacent vertex was not visited a depth first search is called on that vertex
        if not visited[adjacent_vertex]:
            dfs(graph, adjacent_vertex, order, visited)

    # appends source vertex to order list
    order.append(source)

if __name__ == '__main__':
    vertices = ['A','B','C','D','E']
    edges = [('A','B',1),('A','C',1),('B','D',1),('C','D',1),('C','E',1),('E','D',1)]
    graph = AdjacencyList(vertices, edges)
    print(f"Graph:\n{graph}\n")
    print(f"Topological Sort:\n{topological_sort_dfs(graph)}")
    