"""
    Circulation with Demands

    Function: An example of circulation with demands
    Time Complexity (Worst): O(f*e*v)
    Space Complexity (Auxiliary): O(v+e)

"""

from _.AdjacencyList import AdjacencyList
from _.FordFulkerson import ford_fulkerson

def circulation_demands():
    
    # creates initial graph
    vertices = {'v': 2, 'w': 5, 'x': -4, 'y': -3, 'z': 0}
    edges = [('v','w',2), ('w','z',2), ('x','v',3), ('x','y',3), ('y','v',2), ('y','w',3), ('z','y',2)]
    graph = AdjacencyList(list(vertices.keys()), edges)
    print(f"G:\n{graph}\n")

    # creates super graph
    vertices['s'] = None
    vertices['t'] = None
    edges.append(('s','x',-vertices['x']))
    edges.append(('s','y',-vertices['y']))
    edges.append(('v','t',vertices['v']))
    edges.append(('w','t',vertices['w']))
    super_graph = AdjacencyList(list(vertices.keys()), edges)
    print(f"G':\n{super_graph}\n")

    # solves max-flow problem on super graph
    _, solution = ford_fulkerson(super_graph, 's', 't')
    print(f"Max-Flow:\n{solution}\n")

    # turns max flow network into a feasible solution
    solution.remove_vertex('s')
    solution.remove_vertex('t')
    print(f"Solution:\n{solution}")

if __name__ == '__main__':
    circulation_demands()
