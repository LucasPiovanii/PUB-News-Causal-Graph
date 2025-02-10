# main.py

from queue import Queue
from news_scraper.scraper import scrape_news
from news_scraper.graph_builder import create_graph
from news_scraper.graph_plotter import configure_and_plot_graph

url = "https://g1.globo.com/mundo/noticia/2024/10/15/a-estrategia-dos-eua-no-oriente-medio-pressionar-israel-enfraquecer-o-hezbollah-e-eleger-novo-presidente-libanes.ghtml"

# Fila para armazenar os links presentes na página
link_queue = Queue()

# Obtém os dados da notícia
news = scrape_news(url, link_queue)

# Cria o grafo de relação entre as notícias
graph = create_graph(news, link_queue)

# Plota o grafo numa imagem
# TO-DO: encontrar melhor forma de salvar o grafo
configure_and_plot_graph(graph)

graph.write_graphml("meu_grafo.graphml") # ou .gml