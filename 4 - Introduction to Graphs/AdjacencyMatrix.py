"""
    Adjacency Matrix

    Function: Creates a representation of a graph (non-zero edges)
    Space Complexity: O(v^2)

"""

from typing import TypeVar
V = TypeVar('V')

class AdjacencyMatrix:

    def __init__(self, vertices: list[V] = None, edges: list[tuple[V, V, int]] = None) -> None:
        """
            Time Complexity: O(v^2)

        """
        
        # initialises inputs
        if vertices == None:
            vertices = []
        if edges == None:
            edges = []

        # initialises graph attributes
        self.matrix = {}

        # initialises graph matrix based on number of vertices
        for vertex in vertices:
            self.matrix[vertex] = {vertex: (0, False) for vertex in vertices}

        # creates the graph adjacency matrix from edges
        for edge in edges:
            self.add_edge(edge)

    def get_vertices(self) -> list[V]:
        """
            Time Complexity: O(v)

        """

        # returns list of vertices in graph
        return list(self.matrix.keys())
    
    def get_edges(self) -> list[tuple[V, V, int]]:
        """
            Time Complexity: O(v^2)
        
        """

        # returns list of edges in graph
        edges = []
        for vertex_x in self.get_vertices():
            for vertex_y in self.get_vertices():
                if self.check_edge(vertex_x, vertex_y):
                    edges.append((vertex_x, vertex_y, self.get_weight(vertex_x, vertex_y)))
        return edges

    def add_vertex(self, vertex: V) -> None:
        """
            Time Complexity: O(v)
        
        """

        # adds vertex to graph
        self.matrix[vertex] = {}
        for graph_vertex in self.get_vertices():
            self.matrix[vertex][graph_vertex] = (0, False)
            self.matrix[graph_vertex][vertex] = (0, False)

    def add_edge(self, edge: tuple[V, V, int]) -> None:
        """
            Time Complexity: O(1)
        
        """

        # adds edge to graph
        self.matrix[edge[0]][edge[1]] = (edge[2], True)

    def remove_vertex(self, vertex: V) -> None:
        """
            Time Complexity: O(v)
        
        """

        # removes vertex from graph
        del self.matrix[vertex]
        for graph_vertex in self.get_vertices():
            del self.matrix[graph_vertex][vertex]

    def remove_edge(self, edge: tuple[V, V, int]) -> None:
        """
            Time Complexity: O(1)
        
        """

        # removes edge from graph
        self.matrix[edge[0]][edge[1]] = (0, False)
    
    def update_edge(self, vertex_x: V, vertex_y: V, new_weight: int) -> None:
        """
            Time Complexity: O(1)
        
        """

        # updates edge weight
        self.add_edge((vertex_x, vertex_y, new_weight))

    def check_edge(self, vertex_x: V, vertex_y: V) -> bool:
        """
            Time Complexity: O(1)

        """

        # checks if edge exists between the two given vertices
        return self.matrix[vertex_x][vertex_y][1]
    
    def get_weight(self, vertex_x: V, vertex_y: V) -> int:
        """
            Time Complexity: O(1)
        
        """

        # returns weight of edge from vertex x to vertex y
        return self.matrix[vertex_x][vertex_y][0]
    
    def adjacent_vertices(self, vertex: V) -> list[tuple[V, int]]:
        """
            Time Complexity: O(v)

        """

        # returns list of adjacent vertices to the given vertex
        adjacent_vertices = []
        for adjacent_vertex in self.matrix[vertex]:
            if self.matrix[vertex][adjacent_vertex][1]:
                adjacent_vertices.append((adjacent_vertex, self.get_weight(vertex, adjacent_vertex)))
        return adjacent_vertices

    def __str__(self) -> str:
        """
            Time Complexity: O(v^2)
            
        """

        # outputs a formatted adjacency matrix
        vertices = self.get_vertices()
        output = "     "
        for vertex in vertices:
            if len(str(vertex)) == 1:
                output += " "
            output += f"{vertex}  "
        output += "\n"
        for i in range(len(vertices)):
            if len(str(vertices[i])) == 1:
                output += " "
            output += f"{vertices[i]} ["
            for j in range(len(self.matrix)):
                output += " "
                if not self.matrix[vertices[i]][vertices[j]][1]:
                    output += " ."
                else:
                    if len(str(self.matrix[vertices[i]][vertices[j]][0])) == 1:
                        output += " "
                    output += str(self.matrix[vertices[i]][vertices[j]][0])
                if j < (len(vertices) - 1):
                    output += " "
            output += "]"
            if i < (len(vertices) - 1):
                output += "\n"
        return output

if __name__ == '__main__':
    vertices = ['A','B','C','D','E']
    edges = [('A','B',6),('A','D',4),('B','A',7),('B','C',1),('B','E',5),('C','E',3),('D','B',5),('E','D',3)]
    graph = AdjacencyMatrix(vertices, edges)
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
