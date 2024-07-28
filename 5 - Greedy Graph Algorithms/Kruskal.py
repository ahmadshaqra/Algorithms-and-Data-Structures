"""
    Kruskal's Algorithm

    Function: Builds a minimum spanning tree of a weighted graph
    Time Complexity (Worst): O(e*log(v))
    Space Complexity (Auxiliary): O(v+e)

"""

from _.AdjacencyList import AdjacencyList
from heapq import heappush, heappop
from UnionFind import UnionFind
from typing import TypeVar
V = TypeVar('V')

def kruskal(graph: AdjacencyList) -> AdjacencyList:

    # sets up edge queue
    edges = []
    for edge in graph.get_edges():
        heappush(edges, (edge[2], edge))

    # initialises forest and mst
    forest = UnionFind(graph)
    mst = AdjacencyList(graph.get_vertices())

    # loops until all edges have been checked
    while len(edges) != 0:

        # gets the next lightest edge
        edge = heappop(edges)[1]

        # checks if vertices are in the same set
        if forest.find(edge[0]) != forest.find(edge[1]):

            # adds edge to mst and merges sets in forest
            forest.union(forest.find(edge[0]), forest.find(edge[1]))
            mst.add_edge(edge)
    
    # returns mst
    return mst

if __name__ == '__main__':
    vertices = ['A','B','C','D','E']
    edges = [('A','B',10),('A','C',5),('B','C',3),('B','D',1),('C','D',9),('C','E',2),('D','E',4),
             ('B','A',10),('C','A',5),('C','B',3),('D','B',1),('D','C',9),('E','C',2),('E','D',4),]
    graph = AdjacencyList(vertices, edges)
    source = 'A'
    target = 'D'
    print(f"Graph:\n{graph}\n")
    print(f"Minimum Spanning Tree:\n{kruskal(graph)}")
    