# news_scraper/graph_builder.py

import igraph as ig
import networkx as nx
import pickle
from .scraper import scrape_news

# Função que processa a fila de links e a transforma num grafo direcionado com relação entre as notícias
def create_graph(initial_news, link_queue):
    graph = ig.Graph(directed=True)
    
    url_to_vertex = {} # Dicionário para mapear URLs a IDs de vértices no grafo
    processed_urls = set() # Conjunto para rastrear URLs já processadas

    # Adiciona o primeiro vértice (notícia inicial) com seus atributos
    graph.add_vertex(
        id=initial_news.id,
        name=initial_news.url,
        title=initial_news.title,
        subtitle=initial_news.subtitle,
        publication_date=initial_news.publicationDate,
        content=initial_news.content
    )
    url_to_vertex[initial_news.url] = 0 # Primeiro link = id 0
    processed_urls.add(initial_news.url) # Marca a URL inicial como processada

    current_vertex = 1  
    max_vertices = 100 # Limite para teste

    # Fila auxiliar para controlar a sequência de processamento
    pending_news = [(initial_news, 0)] # Par com a notícia e o índice do vértice no grafo

    while not link_queue.empty() and current_vertex < max_vertices:
        # Pega a próxima notícia a ser processada
        current_news, current_news_vertex_id = pending_news.pop(0)

        # Processa os próximos links da fila
        for _ in range(current_news.numDirectRelatedLinks):
            if link_queue.empty() or current_vertex >= max_vertices:
                break
            
            next_url = link_queue.get()
            
            # Verifica se o URL já foi processada
            if next_url in processed_urls:
                continue
            
            news = scrape_news(next_url, link_queue)
            
            # Adiciona a nova notícia como vértice no grafo com atributos, incluindo o id
            graph.add_vertex(
                id=news.id,
                name=news.url,
                title=news.title,
                subtitle=news.subtitle,
                publication_date=news.publicationDate,
                content=news.content
            )
            url_to_vertex[news.url] = current_vertex
            processed_urls.add(news.url) # Marca a nova URL como processada
            
            # Cria uma aresta apontando para a notícia atual
            graph.add_edge(current_news_vertex_id, current_vertex)
            
            # Adiciona a nova notícia para ser processada depois
            pending_news.append((news, current_vertex))
            
            current_vertex += 1

    return graph

# Função que converte um grafo igraph para networkx
# Converte-se para que seja possível armazenar em um arquivo .gpickle
def convert_igraph_to_networkx(igraph_graph):
    nx_graph = nx.DiGraph()

    for v in igraph_graph.vs:
        nx_graph.add_node(v.index, **v.attributes())

    for e in igraph_graph.es:
        nx_graph.add_edge(e.source, e.target)

    return nx_graph
