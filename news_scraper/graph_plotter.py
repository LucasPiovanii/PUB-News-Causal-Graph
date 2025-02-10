# news_scraper/graph_plotter.py

import os
from igraph import plot

def configure_and_plot_graph(graph, output_file="grafo_teste.png"):
    # Diretório para salvar as imagens
    output_directory = "graph_images"
    
    # Cria o diretório se não existir
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    # Junta o diretório ao nome do arquivo
    output_file_path = os.path.join(output_directory, output_file)
    
    # Configurações do grafo
    graph.vs["label"] = graph.vs.indices
    graph.vs["size"] = [30 for _ in graph.vs]
    graph.vs["color"] = ["lightblue" for _ in graph.vs]
    graph.es["arrow_size"] = 0.5
    graph.es["arrow_width"] = 1
    graph.es["color"] = "gray"
    
    layout = graph.layout("fr")
    
    # Plota o grafo e salva a imagem
    plot(graph, target=output_file_path, 
         vertex_label=graph.vs["label"], 
         bbox=(2000, 2000), 
         margin=100,
         layout=layout,
         vertex_size=graph.vs["size"], 
         vertex_color=graph.vs["color"],
         edge_arrow_size=graph.es["arrow_size"],  
         edge_arrow_width=graph.es["arrow_width"],
         edge_color=graph.es["color"])

    print(f"Graph saved at: {output_file_path}")