"""
    Dijkstra's Algorithm

    Function: Finds the distance of all vertices from a single source of a weighted graph (non-negative)
    Time Complexity (Worst): O(e*log(v))
    Space Complexity (Auxiliary): O(v+e)

"""

from _.AdjacencyList import AdjacencyList
from heapq import heappush, heappop
from typing import TypeVar
V = TypeVar('V')

def dijkstra(graph: AdjacencyList, source: V, target: V | None = None, return_predecessor: bool = False) -> dict[V, int] | int | list[V]:

    # initialises lists
    distance = {vertex: float("inf") for vertex in graph.get_vertices()}
    queue = []
    predecessor = {vertex: None for vertex in graph.get_vertices()}

    # processes source vertex
    distance[source] = 0

    # sets up queue
    for vertex in graph.get_vertices():
        heappush(queue, (distance[vertex], vertex))
    
    # loops until queue is empty
    while len(queue) != 0:

        # gets next closest vertex
        key, current_vertex = heappop(queue)
        if distance[current_vertex] == key:
                
            # checks every adjacent vertex of current vertex
            for adjacent_vertex, weight in graph.adjacent_vertices(current_vertex):
                
                # checks if current distance is greater than actual distance from vertex
                if distance[adjacent_vertex] > (distance[current_vertex] + weight):
                    
                    # updates distance of adjacent vertex and sets current vertex as predecessor of adjacent vertex
                    distance[adjacent_vertex] = distance[current_vertex] + weight
                    predecessor[adjacent_vertex] = current_vertex
                    heappush(queue, (distance[adjacent_vertex], adjacent_vertex))
        
    # returns based on initial input
    if return_predecessor:
        return predecessor
    elif target == None:
        return distance
    else:
        return distance[target]

def shortest_path(graph: AdjacencyList, source: V, target: V) -> list[V]:

    # gets the predecessor list using dijkstra's algorithm
    predecessor = dijkstra(graph, source, None, True)

    # initialises path list
    path = [target]

    # sets current vertex to target
    current_vertex = target

    # traverses graph backwards from target until source is reached
    while current_vertex != source:

        # appends predeccessor of current to path and sets current to predecessor
        path.append(predecessor[current_vertex])
        current_vertex = predecessor[current_vertex]

    # reverses and returns path list
    path.reverse()
    return path

if __name__ == '__main__':
    vertices = ['A','B','C','D','E']
    edges = [('A','B',10),('A','C',5),('B','C',2),('B','D',1),('C','B',3),('C','D',9),('C','E',2),('D','E',4),('E','D',6)]
    graph = AdjacencyList(vertices, edges)
    source = 'A'
    target = 'D'
    print(f"Graph:\n{graph}\n")
    print(f"Distance from {source}:\n{dijkstra(graph, source)}\n")
    print(f"Distance from {source} to {target}:\n{dijkstra(graph, source, target)}\n")
    print(f"Shortest Path from {source} to {target}:\n{shortest_path(graph, source, target)}")
    