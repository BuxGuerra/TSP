import igraph as ig
import tsplib95
import math

# Função para calcular a distância Euclidiana
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Caminho para o arquivo .tsp
tsp_file_path = "data/burma14.tsp"

# Carregar o problema do TSP usando tsplib95
problem = tsplib95.load(tsp_file_path)

# Criar o grafo no formato igraph
G = ig.Graph()

# Adicionar os nós ao grafo (usando as coordenadas como atributos)
coordinates = problem.node_coords
for i, (node, (x, y)) in enumerate(coordinates.items()):
    G.add_vertex(name=node, x=x, y=y)

# Adicionar as arestas com as distâncias Euclidianas entre os nós
for i in range(len(coordinates)):
    for j in range(i + 1, len(coordinates)):  # Para garantir que as arestas não se repitam
        # Obter as coordenadas dos dois nós
        x1, y1 = coordinates[i + 1]  # índice começa em 1 no TSPLIB
        x2, y2 = coordinates[j + 1]
        
        # Calcular a distância Euclidiana entre os dois nós
        distance = euclidean_distance(x1, y1, x2, y2)
        
        # Adicionar a aresta ao grafo com o peso calculado
        G.add_edge(i, j, weight=distance)

# Verificar a estrutura do grafo
G.add_edge(1, 2)
#edge_id = G.get_eid(1, 2)
edge_id = G.ecount() - 1
print(edge_id)
print(G.es[edge_id]["weight"])
G_nx = G.to_networkx()
print(G_nx.number_of_edges())
#print(G)


#rodar com branch and bound
#rodar com  twice-around-the-tree
#rodar com Christofides

