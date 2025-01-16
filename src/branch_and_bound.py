import igraph as ig
import networkx as nx
import numpy as np
import heapq



#Manter uma lista ordenada com os nós 
#Cada nó armazena: lower bound, caminho parcial


class node:
    def __init__(self, lb: float, path: list):
        self.lb = lb
        self.path = path
        


def branch_and_bound(graph: ig.Graph):
    best_path_weight = float('inf')
    nodes = []

    #Calcular lb para o nó inicial
    lb = 0
    for vertex in graph.vs:
        edges = []
        neighbors = graph.neighbors(vertex.index)
        
        for neighbor in neighbors:
            edge_id = graph.get_eid(vertex.index, neighbor)
            edge_weight = graph.es[edge_id]['weight']
            edge_tuple = (edge_id, edge_weight)
            edges.append(edge_tuple)

        edges_array = np.array(edges)
        edges_sorted_array = sorted(edges_array, key=lambda x: x[1])
        
        lb += (edges_sorted_array[0][1] + edges_sorted_array[1][1])/2

    current_node = node(lb, [0])
    heapq.heappush(nodes, current_node)


    #Enquanto lista tem nó:
    #Pega o melhor
    #Compara com a melhor solução já encontrada, se puder ser melhor continua:
    #Abre todos os filhos, calcula o lb deles e coloca eles na fila de forma ordenada

    while(nodes):
        current_node = heapq.heappop(nodes)
        if(current_node[0] >= best_path_weight):
            continue

        partial_path = current_node[1]
        new_partial_path = partial_path.copy()
        for vertex in range(graph.vcount()):
            if vertex in partial_path:
                continue
            
            new_partial_path.append(vertex)
            #calcular novo lb
            
            #colocar no na heap

