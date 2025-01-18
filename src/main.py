import os
import time
import pandas as pd
import igraph as ig
import tsplib95
import math

from twiceAroundTheTree import twice_around_the_tree
from christofides import christofides
from branch_and_bound import branch_and_bound

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def create_graph_from_tsp(tsp_file_path):
    problem = tsplib95.load(tsp_file_path)
    G = ig.Graph()
    
    coordinates = problem.node_coords
    for i, (node, (x, y)) in enumerate(coordinates.items()):
        G.add_vertex(name=node, x=x, y=y)
    
    for i in range(len(coordinates)):
        for j in range(i + 1, len(coordinates)):
            x1, y1 = coordinates[i + 1]
            x2, y2 = coordinates[j + 1]
            distance = euclidean_distance(x1, y1, x2, y2)
            G.add_edge(i, j, weight=distance)
    
    return G

def benchmark_instance(file_path):
    results = []
    filename = os.path.basename(file_path)
    G = create_graph_from_tsp(file_path)
    
    start_time = time.time()
    tour_length = christofides(G)
    christ_time = time.time() - start_time
    results.append({
        'file': filename,
        'algorithm': 'Christofides',
        'tour_length': tour_length,
        'time': christ_time
    })


    
    return results

def main():
    data_dir = "data/"
    output_file = "benchmark_results_3.csv"
    
    tsp_files = [f for f in os.listdir(data_dir) if f.endswith('.tsp')]
    
    for i, tsp_file in enumerate(tsp_files):
        file_path = os.path.join(data_dir, tsp_file)
        try:
            results = benchmark_instance(file_path)
            df = pd.DataFrame(results)

            df.to_csv(output_file, 
                     mode='a' if i > 0 else 'w',
                     header=True if i == 0 else False, 
                     index=False)
            
            print(f"Processed {tsp_file} and saved to {output_file}")
        except Exception as e:
            print(f"Error processing {tsp_file}: {str(e)}")
    
    print(f"All results saved to {output_file}")

if __name__ == "__main__":
    main()
