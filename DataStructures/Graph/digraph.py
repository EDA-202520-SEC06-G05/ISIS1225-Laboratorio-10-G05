from DataStructures.Map import map_linear_probing as lp
from DataStructures.Graph import vertex as vt

def new_graph(order):
    graph = {
        "vertices": lp.new_map(order, 0.7, None),
        "num_edges": 0
    }
    return graph

def insert_vertex(my_graph, key_u, info_u):
    vertex = vt.new_vertex(key_u, info_u)
    lp.put(my_graph["vertices"], key_u, vertex)
    return my_graph

