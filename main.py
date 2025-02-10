# main.py

from queue import Queue
from news_scraper.scraper import scrape_news
from news_scraper.graph_builder import create_graph
from news_scraper.graph_plotter import configure_and_plot_graph
from news_scraper.graph_builder import create_graph, convert_igraph_to_networkx
import pickle

url = "https://g1.globo.com/mundo/noticia/2024/10/15/a-estrategia-dos-eua-no-oriente-medio-pressionar-israel-enfraquecer-o-hezbollah-e-eleger-novo-presidente-libanes.ghtml"

# Fila para armazenar os links presentes na página
link_queue = Queue()

# Obtém os dados da notícia
news = scrape_news(url, link_queue)

# Cria o grafo de relação entre as notícias
graph_igraph = create_graph(news, link_queue)

# Plota o grafo numa imagem (apenas para visualização)
configure_and_plot_graph(graph_igraph)

# Converte o grafo para networkx para salvar em .gpickle
graph_networkx = convert_igraph_to_networkx(graph_igraph)

output_file = "grafo.gpickle"
with open(output_file, "wb") as f:
    pickle.dump(graph_networkx, f)
print(f"Grafo salvo com sucesso em {output_file}")