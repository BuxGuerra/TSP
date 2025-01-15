import igraph as ig


def christofides(graph: ig.Graph):
    msp = graph.spanning_tree(weights=graph.es["weight"])

    odd_degree_vertices = []

    for i in range(graph.vcount()):
        if (len(msp.neighbors(i))%2 == 1):
            odd_degree_vertices.append(i)

    induced_subgraph = graph.induced_subgraph(odd_degree_vertices)






    #Calcular o tamanho do caminho
    path_weight = 0
    for i in range(len(path)):
        edge_id = graph.get_eid(path[i], path[(i+1)%len(path)])
        path_weight += graph.es[edge_id]["weight"]

    return path_weight







