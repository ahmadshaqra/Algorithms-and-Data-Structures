"""
    Union Find

    Function: Creates a union find data structure
    Space Complexity: O(v)

"""

from _.AdjacencyList import AdjacencyList
from typing import TypeVar
V = TypeVar('V')

class UnionFind:

    def __init__(self, graph: AdjacencyList) -> None:

        # initialises map array and sets
        self.map_array = {graph.get_vertices()[i]: i for i in range(len(graph.get_vertices()))}
        self.sets = [{vertex} for vertex in graph.get_vertices()]
        
    def find(self, vertex: V) -> int:
        """
            Time Complexity (Worst): O(1)
        
        """

        # returns set index of vertex
        return self.map_array[vertex]
    
    def union(self, i: int, j: int) -> None:
        """
            Time Complexity (Worst): O(x)
        
        """
        
        # merges sets i and j
        for vertex in self.sets[i]:
            self.map_array[vertex] = j
        self.sets[j].update(self.sets[i])
        self.sets[i].clear()

if __name__ == '__main__':
    vertices = ['A','B','C','D','E']
    graph = AdjacencyList(vertices)
    unionfind = UnionFind(graph)
    print(f"Sets: {unionfind.sets}")
    print(f"Set IDs: {unionfind.map_array}")
    print(f"Set ID of A: {unionfind.find('A')}")
    unionfind.union(0,1)
    unionfind.union(1,4)
    print("\nMerging Sets 0, 1, and 4:")
    print(f"Sets: {unionfind.sets}")
    print(f"Set IDs: {unionfind.map_array}")
    