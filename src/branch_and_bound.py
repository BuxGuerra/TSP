import igraph as ig
import networkx as nx
import numpy as np
import heapq


#Manter uma heap ordenada com os nós 
#Cada nó armazena: lower bound, caminho parcial

class node:
    def __init__(self, lb: float, path: list):
        self.lb = lb
        self.path = path

    def __lt__(self, other):
        return self.lb < other.lb
        


def branch_and_bound(graph: ig.Graph):
    best_path_weight = float('inf')
    nodes = []

    #Calcular lb para o nó inicial
    lb = 0
    smallest_edges = np.empty(graph.vcount(), dtype=object)
    
    for vertex in graph.vs:
        edges = []
        neighbors = graph.neighbors(vertex.index)
        
        for neighbor in neighbors:
            edge_id = graph.get_eid(vertex.index, neighbor)
            edge_weight = graph.es[edge_id]['weight']
            edge_tuple = (edge_id, edge_weight)
            edges.append(edge_tuple)

        edges_sorted_array = sorted(edges, key=lambda x: x[1])
        
        lb += (edges_sorted_array[0][1] + edges_sorted_array[1][1])/2
        smallest_edges[vertex.index] = (edges_sorted_array[0][1], edges_sorted_array[1][1])

    current_node = node(lb, [0])
    heapq.heappush(nodes, current_node)


    #Enquanto lista tem nó:
    #Pega o melhor
    #Compara com a melhor solução já encontrada, se puder ser melhor continua:
    #Abre todos os filhos, calcula o lb deles e coloca eles na fila de forma ordenada

    while(nodes):
        current_node = heapq.heappop(nodes)
        partial_path = current_node.path
        lb = current_node.lb

        #Se o nó deve ser cortado
        if(lb >= best_path_weight):
            continue

        #Se o nó é folha
        if(len(partial_path) == graph.vcount()):
            #calcular tamanho do caminho
            first_vertex = partial_path[0]
            last_vertex = partial_path[-1]
            edge_id = graph.get_eid(first_vertex, last_vertex)
            edge_weight = graph.es[edge_id]['weight']

            path_weight = lb - (smallest_edges[last_vertex][0] + smallest_edges[first_vertex][0])/2
            path_weight += edge_weight

            #verficar se é melhor que o melhor que já temos
            if path_weight < best_path_weight:
                best_path_weight = path_weight

            continue


        #Abre os vértices filhos
        new_partial_path = partial_path.copy()

        for vertex in range(graph.vcount()):
            if vertex in partial_path:
                continue
            
            new_partial_path.append(vertex)
            #calcular novo lb
            edge_id = graph.get_eid(new_partial_path[-2], vertex)
            edge_weight = graph.es[edge_id]['weight']
            
            #Quando o elemento é o segundo precisa fazer de um jeito levemente diferente
            if(len(new_partial_path) == 2):
                new_lb = lb - (smallest_edges[vertex][1] + smallest_edges[new_partial_path[-2]][1])/2
                new_lb += edge_weight
            else:
                new_lb = lb - (smallest_edges[vertex][1] + smallest_edges[new_partial_path[-2]][0])/2
                new_lb += edge_weight
            
            new_node = node(new_lb, new_partial_path)
            heapq.heappush(nodes, new_node)


    return best_path_weight
    