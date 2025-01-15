import igraph as ig
import networkx as nx


def christofides(graph: ig.Graph):
    msp = graph.spanning_tree(weights=graph.es["weight"])

    odd_degree_vertices = []

    for i in range(graph.vcount()):
        if (len(msp.neighbors(i))%2 == 1):
            odd_degree_vertices.append(i)

    induced_subgraph = graph.induced_subgraph(odd_degree_vertices)
    print(induced_subgraph.vs[5])

    #Encontrar matching perfeito de peso mínimo no grafo induzido
    induced_subgraph_nx = induced_subgraph.to_networkx()
    mwpm_nx = nx.algorithms.matching.min_weight_matching(induced_subgraph_nx, weight="weight")
    print(mwpm_nx)

    #o mwpm_nx é um set que contem as arestas de mwpm
    #preciso então fazer um novo grafo que é a junção da mst com essas novas arestas
    #preciso me atentar a usar o nome dos vertices e não os indices
    #itero sobre o set
        #olho os dois vertices que fazem a aresta, vejo o nome deles, adiciono uma nova aresta
        #no novo grafo com base no nome dos vértices

    #Construir novo multigrafo juntando a msp e o matching perfeito
    multigraph = msp.copy()
    for edge in mwpm_nx:
        v1_name = induced_subgraph_nx.nodes[edge[0]]['name']
        v2_name = induced_subgraph_nx.nodes[edge[1]]['name']
        edge_weight = induced_subgraph_nx[edge[0]][edge[1]]["weight"]
        
        v1_index = graph.vs.find(name=v1_name).index
        
        
        
        


    
    #Problema aqui: quando fiz o grafo induzido acho que perdi os indices originais dos vertices
    #No grafo induzido o nome dos vertices se mantiveram
    #Quando transformou pra nx tbm se mantiveram

    #mwpm = ig.Graph.from_networkx(mwpm_nx)


    #Encontrar circuito euleriano no novo grafo
    #Achar solução pro tsp a partir do circuito euleriano




    #Calcular o tamanho do caminho
    #path_weight = 0
    #for i in range(len(path)):
    #    edge_id = graph.get_eid(path[i], path[(i+1)%len(path)])
    #    path_weight += graph.es[edge_id]["weight"]
#
    #return path_weight







