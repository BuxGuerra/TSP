# Problema do Caixeiro Viajante (PCV)

Este repositório contém implementações de três diferentes abordagens para resolver o Problema do Caixeiro Viajante (PCV): uma solução exata usando Branch and Bound e dois algoritmos de aproximação - Twice Around the Tree e Christofides. Este trabalho foi desenvolvido como parte da disciplina de Algoritmos II do DCC-UFMG.

## Visão Geral

O projeto implementa e compara três diferentes soluções para o PCV Euclidiano:
- Branch and Bound (solução exata)
- Twice Around the Tree (algoritmo 2-aproximativo)
- Algoritmo de Christofides (algoritmo 1.5-aproximativo)

## Pré-requisitos

- Python 3.9+
- Pacotes necessários:
  - igraph
  - networkx
  - numpy
  - pandas
  - tsplib95

## Instalação

1. Clone este repositório:
```bash
git clone https://github.com/BuxGuerra/TSP.git
cd TSP
```

2. Instale os pacotes necessários:
```bash
pip install python-igraph networkx numpy pandas tsplib95
```

## Estrutura do Projeto

- `main.py` - Arquivo principal de execução
- `branch_and_bound.py` - Implementação do algoritmo Branch and Bound
- `twiceAroundTheTree.py` - Implementação do algoritmo Twice Around the Tree
- `christofides.py` - Implementação do algoritmo de Christofides

## Como Usar

Execute o arquivo principal passando o diretório contendo as instâncias do problema:

```bash
python main.py
```

O programa irá:
1. Processar todas as instâncias TSP no diretório de dados
2. Executar os três algoritmos para cada instância
3. Gerar um arquivo CSV com os resultados das comparações

## Resultados

Os resultados são salvos em um arquivo CSV contendo:
- Nome do arquivo de entrada
- Algoritmo utilizado
- Comprimento do tour encontrado
- Tempo de execução

## Autores

- Guilherme B. M. Guerra
- Samuel Brum Martins
