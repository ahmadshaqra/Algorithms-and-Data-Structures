"""
    Prim's Algorithm

    Function: Builds a minimum spanning tree of a weighted graph
    Time Complexity (Worst): O(e*log(v))
    Space Complexity (Auxiliary): O(v)

"""

from _.AdjacencyList import AdjacencyList
from heapq import heappush, heappop
from typing import TypeVar
V = TypeVar('V')

def prim(graph: AdjacencyList, source: V) -> AdjacencyList:
    
    # initialises lists and mst
    distance = {vertex: float("inf") for vertex in graph.get_vertices()}
    queue = []
    parent = {vertex: None for vertex in graph.get_vertices()}
    mst = AdjacencyList([None])

    # processes source vertex
    distance[source] = 0

    # sets up queue
    for vertex in graph.get_vertices():
        heappush(queue, (distance[vertex], vertex))

    # loops until queue is empty
    while len(queue) != 0:

        # gets next closest vertex and adds it to mst
        key, current_vertex = heappop(queue)
        if distance[current_vertex] == key:
            mst.add_vertex(current_vertex)
            if parent[current_vertex] == None:
                mst.add_edge((parent[current_vertex], current_vertex, 0))
            else:
                mst.add_edge((parent[current_vertex], current_vertex, graph.get_weight(parent[current_vertex], current_vertex)))

            # checks every adjacent vertex of current vertex
            for adjacent_vertex, weight in graph.adjacent_vertices(current_vertex):
                
                # updates distance of adjacent vertex and sets current vertex as parent of adjacent vertex
                if adjacent_vertex not in mst.get_vertices() and distance[adjacent_vertex] > weight:
                    distance[adjacent_vertex] = weight
                    parent[adjacent_vertex] = current_vertex
                    heappush(queue, (distance[adjacent_vertex], adjacent_vertex))

    # removes null vertex from mst and returns mst
    mst.remove_vertex(None)
    return mst

if __name__ == '__main__':
    vertices = ['A','B','C','D','E']
    edges = [('A','B',10),('A','C',5),('B','C',3),('B','D',1),('C','D',9),('C','E',2),('D','E',4),
             ('B','A',10),('C','A',5),('C','B',3),('D','B',1),('D','C',9),('E','C',2),('E','D',4),]
    graph = AdjacencyList(vertices, edges)
    source = 'A'
    target = 'D'
    print(f"Graph:\n{graph}\n")
    print(f"Minimum Spanning Tree:\n{prim(graph, 'A')}")
    