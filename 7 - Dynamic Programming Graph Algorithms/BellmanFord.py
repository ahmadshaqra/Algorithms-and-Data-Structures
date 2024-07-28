"""
    Bellman-Ford Algorithm

    Function: Finds the distance of all vertices from a single source of a weighted graph
    Time Complexity (Worst): O(v*e)
    Space Complexity (Auxiliary): O(v)

"""

from _.AdjacencyList import AdjacencyList
from typing import TypeVar
V = TypeVar('V')

def bellman_ford(graph: AdjacencyList, source: V, target: V | None = None, return_predecessor: bool = False) -> dict[V, int] | int | list[V]:
    
    # initialises lists
    vertices = graph.get_vertices()
    edges = graph.get_edges()
    distance = {vertex: float("inf") for vertex in vertices}
    predecessor = {vertex: None for vertex in vertices}

    # processes source vertex
    distance[source] = 0

    # iterates for number of vertices minus one
    for _ in range(len(vertices)-1):

        # loops through every edge
        for edge in edges:

            # checks if distance to vertex can be improved and updates distance and predecessor appropriately
            if distance[edge[0]] + edge[2] < distance[edge[1]]:
                distance[edge[1]] = distance[edge[0]] + edge[2]
                predecessor[edge[1]] = edge[0]

    # checks for negative edge cycles and raises an error if found
    for edge in edges:
        if distance[edge[0]] + edge[2] < distance[edge[1]]:
            raise Exception("Negative Edge Cycle Found in Graph")
    
    # returns based on initial input
    if return_predecessor:
        return predecessor
    elif target == None:
        return distance
    else:
        return distance[target]

def shortest_path(graph: AdjacencyList, source: V, target: V) -> list[V]:

    # gets the predecessor list using dijkstra's algorithm
    predecessor = bellman_ford(graph, source, None, True)

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
    vertices = ['S','T','U','V','X']
    edges = [('S','U',6),('S','V',7),('U','V',8),('U','T',5),('U','X',-4),('T','U',-2),('X','T',7),('V','T',-3),('V','X',9)]
    graph = AdjacencyList(vertices, edges)
    source = 'S'
    target = 'X'
    print(f"Graph:\n{graph}\n")
    print(f"Distance from {source}:\n{bellman_ford(graph, source)}\n")
    print(f"Distance from {source} to {target}:\n{bellman_ford(graph, source, target)}\n")
    print(f"Shortest Path from {source} to {target}:\n{shortest_path(graph, source, target)}\n")
    graph.remove_edge(('U','V',8))
    graph.add_edge(('U','V',4))
    print(f"Graph:\n{graph}\n")
    try:
        print(f"Distance from {source}:\n{bellman_ford(graph, source)}\n")
    except Exception:
        print("Error: Negative Edge Cycle Found in Graph")
    