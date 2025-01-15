#computar Arvore geradora minima
#retornar a pre-ordem

import igraph as ig

def twice_around_the_tree(graph: ig.Graph):
    msp = graph.spanning_tree()

    initial_tuple = (0,0)  #(vertice inicial, pai) (pai aqui não faz sentido por isso deixei o mesmo)
    stack = []
    stack.append(initial_tuple)

    path = []

    while(stack):
        current_tuple = stack.pop()
        current_vertice = current_tuple[0]
        father_vertice = current_tuple[1]

        path.append(current_vertice) #O caminho vai ter o indice dos vertices comecando em 0

        neighbors = msp.neighbors(current_vertice)
        for neighbor in neighbors:
            if(neighbor == father_vertice):
                continue
            new_tuple = (neighbor, current_vertice)
            stack.append(new_tuple)

    print(path)

    #Calcular o tamanho do caminho
    path_weight = 0
    for i in range(len(path)):
        edge_id = graph.get_eid(path[i], path[(i+1)%len(path)])
        path_weight += graph.es[edge_id]["weight"]

    return path_weight







