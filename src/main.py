import igraph as ig
import tsplib95
import math

from twiceAroundTheTree import twice_around_the_tree
from christofides import christofides

# Função para calcular a distância Euclidiana
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Caminho para o arquivo .tsp
tsp_file_path = "data/att48.tsp"

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
print(f"Numero de nós: {len(G.vs)}")
print(f"Numero de arestas: {len(G.es)}")


#rodar com branch and bound
#rodar com  twice-around-the-tree
print(twice_around_the_tree(G))
#rodar com Christofides
print(christofides(G))

