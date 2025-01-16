import igraph as ig
import networkx as nx


def christofides(graph: ig.Graph):
    msp = graph.spanning_tree(weights=graph.es["weight"])

    odd_degree_vertices = []

    for i in range(graph.vcount()):
        if (len(msp.neighbors(i))%2 == 1):
            odd_degree_vertices.append(i)

    induced_subgraph = graph.induced_subgraph(odd_degree_vertices)

    #Encontrar matching perfeito de peso mínimo no grafo induzido
    induced_subgraph_nx = induced_subgraph.to_networkx()
    mwpm_nx = nx.algorithms.matching.min_weight_matching(induced_subgraph_nx, weight="weight")

    #Construir novo multigrafo juntando a msp e o matching perfeito
    multigraph = msp.copy()
    for edge in mwpm_nx:
        v1_name = induced_subgraph_nx.nodes[edge[0]]['name']
        v2_name = induced_subgraph_nx.nodes[edge[1]]['name']
        edge_weight = induced_subgraph_nx[edge[0]][edge[1]]["weight"]
        
        v1_index = graph.vs.find(name=v1_name).index
        v2_index = graph.vs.find(name=v2_name).index

        multigraph.add_edge(v1_index, v2_index)
        edge_id = multigraph.ecount() - 1
        multigraph.es[edge_id]["weight"] = edge_weight
        
    
    #Encontrar circuito euleriano no novo grafo
    multigraph_nx = multigraph.to_networkx()
    eulerian_circuit = nx.eulerian_circuit(multigraph_nx)
    eulerian_vertices = [u for u, v in eulerian_circuit]

    #Achar solução pro tsp a partir do circuito euleriano
    path = []
    for vertice in eulerian_vertices:
        if vertice not in path:
            path.append(vertice)

    
    #Calcular o tamanho do caminho
    path_weight = 0
    for i in range(len(path)):
        edge_id = graph.get_eid(path[i], path[(i+1)%len(path)])
        path_weight += graph.es[edge_id]["weight"]

    return path_weight







