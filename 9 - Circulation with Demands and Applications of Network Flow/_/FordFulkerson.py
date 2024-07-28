"""
    Ford-Fulkerson Method

    Function: Solves the max-flow problem for network flow graphs
    Time Complexity (Worst): O(f*e*v)
    Space Complexity (Auxiliary): O(v+e)

"""

from .AdjacencyList import AdjacencyList
from typing import TypeVar
V = TypeVar('V')

def ford_fulkerson(capacity_network: AdjacencyList, source: V, target: V) -> tuple[int, AdjacencyList]:

    # initialise capacity network vertices and edges
    capacity_network_vertices = capacity_network.get_vertices()
    capacity_network_edges = capacity_network.get_edges()

    # initialises flow network
    flow_network = AdjacencyList(capacity_network_vertices)
    for edge in capacity_network_edges:
        flow_network.add_edge((edge[0], edge[1], 0))
    flow = 0

    # initialises residual network
    residual_network = AdjacencyList(capacity_network_vertices)
    for i in range(len(capacity_network_edges)):
        residual_network.add_edge(capacity_network_edges[i])
        residual_network.add_edge((capacity_network_edges[i][1], capacity_network_edges[i][0], 0))

    # increases flow until no augmenting path exists
    augmenting_path_exists = True
    while augmenting_path_exists:

        # finds augmenting path in residual network
        path = find_path(residual_network, source, target)

        # checks if a augmenting path exists
        if path == []:
            augmenting_path_exists = False
        else:

            # gets path capacity
            path_capacity = float("inf")
            for _, weight in path:
                if weight < path_capacity:
                    path_capacity = weight
            
            # updates flow network
            flow += path_capacity
            for i in range(len(path)):
                if i == 0:
                    flow_network.update_edge(source, path[i][0], flow_network.get_weight(source, path[i][0]) + path_capacity)
                else:
                    if flow_network.check_edge(path[i-1][0], path[i][0]):
                        flow_network.update_edge(path[i-1][0], path[i][0], flow_network.get_weight(path[i-1][0], path[i][0]) +  path_capacity)
                    else:
                        flow_network.update_edge(path[i][0], path[i-1][0], flow_network.get_weight(path[i][0], path[i-1][0]) -  path_capacity)
            
            # updates residual network
            for i in range(len(path)):
                if i == 0:
                    residual_network.update_edge(source, path[i][0], residual_network.get_weight(source, path[i][0]) - path_capacity)
                    residual_network.update_edge(path[i][0], source, residual_network.get_weight(path[i][0], source) + path_capacity)
                else:
                    residual_network.update_edge(path[i-1][0], path[i][0], residual_network.get_weight(path[i-1][0], path[i][0]) - path_capacity)
                    residual_network.update_edge(path[i][0], path[i-1][0], residual_network.get_weight(path[i][0], path[i-1][0]) + path_capacity)

    # returns flow and flow network
    return flow, flow_network

def find_path(graph: AdjacencyList, source: V, target: V, path: list[tuple[V, int]] = None, visited: dict[V, bool] = None) -> list[tuple[V, int]]:

    # initialises path and visited
    if path == None:
        path = []
    if visited == None:
        visited = {vertex: False for vertex in graph.get_vertices()}
    
    # marks source vertex as visited
    visited[source] = True

    # returns path early if target has been visited
    if visited[target] == True:
        return path

    # checks each adjacent vertex of the current vertex
    for adjacent_vertex, weight in graph.adjacent_vertices(source):

        # if the adjacent vertex was not visited and target hasn't been found it continues to search
        if not visited[adjacent_vertex] and visited[target] != True and weight != 0:
            path.append((adjacent_vertex, weight))
            find_path(graph, adjacent_vertex, target, path, visited)

            # removes failed paths
            if visited[target] != True:
                path.remove((adjacent_vertex, weight))

    # returns path of vertices and weights
    return path

if __name__ == '__main__':
    vertices = ['S','A','B','C','D','T']
    edges = [('S','A',3),('S','B',5),('A','C',3),('B','D',5),('C','B',3),('C','T',3),('D','T',5)]
    capacity_network = AdjacencyList(vertices, edges)
    source = 'S'
    target = 'T'
    print(f"Network Capacity:\n{capacity_network}\n")
    flow, flow_network = ford_fulkerson(capacity_network, source, target)
    print(f"Max Flow: {flow}\nMax Flow Network:\n{flow_network}")
