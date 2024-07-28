"""
    Adjacency List

    Function: Creates a representation of a graph
    Space Complexity: O(v+e)

"""

from typing import TypeVar
V = TypeVar('V')

class AdjacencyList:
    
    def __init__(self, vertices: list[V] = None, edges: list[tuple[V, V, int]] = None) -> None:
        """
            Time Complexity: O(v+e)

        """
        
        # initialises inputs
        if vertices == None:
            vertices = []
        if edges == None:
            edges = []

        # initialises graph attributes
        self.list = {}
        
        # initialises graph list based on number of vertices
        self.list = {vertex: [] for vertex in vertices}

        # creates the graph adjacency list from edges
        for edge in edges:
            self.add_edge(edge)
    
    def get_vertices(self) -> list[V]:
        """
            Time Complexity: O(v)

        """

        # returns list of vertices in graph
        return list(self.list.keys())
    
    def get_edges(self) -> list[tuple[V, V, int]]:
        """
            Time Complexity: O(v+e)

        """
        
        # returns list of edges in graph
        edges = []
        for vertex in self.get_vertices():
            for edge in self.list[vertex]:
                edges.append((vertex, edge[0], edge[1]))
        return edges

    def add_vertex(self, vertex: V) -> None:
        """
            Time Complexity: O(1)
        
        """

        # adds vertex to graph
        self.list[vertex] = []

    def add_edge(self, edge: tuple[V, V, int]) -> None:
        """
            Time Complexity: O(1)
        
        """

        # adds edge to graph
        self.list[edge[0]].append((edge[1], edge[2]))

    def remove_vertex(self, vertex: V) -> None:
        """
            Time Complexity: O(e*log(v))
        
        """

        # removes vertex from adjacency list
        del self.list[vertex]
        
        # removes edges to vertex in graph
        for graph_vertex in self.get_vertices():
            for adjacent_vertex, weight in self.adjacent_vertices(graph_vertex):
                if adjacent_vertex == vertex:
                    self.remove_edge((graph_vertex, adjacent_vertex, weight))
    
    def remove_edge(self, edge: tuple[V, V, int]) -> None:
        """
            Time Complexity: O(log(v))
        
        """

        # removes edge from graph
        self.list[edge[0]].remove((edge[1], edge[2]))

    def update_edge(self, vertex_x: V, vertex_y: V, new_weight: int) -> None:
        """
            Time Complexity: O(log(v))
        
        """

        # updates edge weight
        self.remove_edge((vertex_x, vertex_y, self.get_weight(vertex_x, vertex_y)))
        self.add_edge((vertex_x, vertex_y, new_weight))

    def check_edge(self, vertex_x: V, vertex_y: V) -> bool:
        """
            Time Complexity: O(log(v))

        """

        # checks if edge exists between the two given vertices
        for vertex, _ in self.adjacent_vertices(vertex_x):
            if vertex == vertex_y:
                return True
        return False
    
    def get_weight(self, vertex_x: V, vertex_y: V) -> int:
        """
            Time Complexity: O(log(v))
        
        """

        # returns weight of edge from vertex x to vertex y
        if not self.check_edge(vertex_x, vertex_y):
            return 0
        for adjacent_vertex, weight in self.adjacent_vertices(vertex_x):
            if adjacent_vertex == vertex_y:
                return weight

    def adjacent_vertices(self, vertex: V) -> list[tuple[V, int]]:
        """
            Time Complexity: O(1)

        """

        # returns list of adjacent vertices to the given vertex
        return self.list[vertex]

    def __str__(self) -> str:
        """
            Time Complexity: O(v+e)
            
        """
        
        # outputs a formatted adjacency list
        vertices = self.get_vertices()
        output = ""
        for i in range(len(vertices)):
            output += f"{vertices[i]} -> ["
            for j in range(len(self.adjacent_vertices(vertices[i]))):
                output += " "
                if len(str(self.adjacent_vertices(vertices[i])[j][0])) == 1:
                    output += " "
                output += f"{str(self.adjacent_vertices(vertices[i])[j][0])} ("
                if len(str(self.adjacent_vertices(vertices[i])[j][1])) == 1:
                    output += " "
                output += f"{str(self.adjacent_vertices(vertices[i])[j][1])})"
                if j < (len(self.adjacent_vertices(vertices[i])) - 1):
                    output += ","
            output += "]"
            if i < (len(vertices) - 1):
                output += "\n"
        return output

if __name__ == '__main__':
    vertices = ['A','B','C','D','E']
    edges = [('A','B',6),('A','D',4),('B','A',7),('B','C',1),('B','E',5),('C','E',3),('D','B',5),('E','D',3)]
    graph = AdjacencyList(vertices, edges)
    print(f"Graph:\n{graph}\n")
    print(f"Vertices: {graph.get_vertices()}")
    print(f"Edges: {graph.get_edges()}")
    print(f"Edge from B to A: {graph.check_edge('B','A')}")
    print(f"Vertices Adjacent to B: {graph.adjacent_vertices('B')}")
    print("Removing Vertex B")
    graph.remove_vertex('B')
    print("Changing Edge A -> D from 4 to 10")
    graph.update_edge('A','D',10)
    print(f"Vertices: {graph.get_vertices()}")
    print(f"Edges: {graph.get_edges()}\n")
    print(f"Graph:\n{graph}")
