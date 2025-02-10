# news_scraper/news.py

class News:
    def __init__(self, id, title, subtitle, url, publicationDate, content, numDirectRelatedLinks):
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.url = url
        self.publicationDate = publicationDate
        self.content = content
        self.numDirectRelatedLinks = numDirectRelatedLinks

    def __repr__(self):
        return f"News({self.id}, {self.title}, {self.subtitle}, {self.url}, {self.publicationDate}, {self.content}, {self.numDirectRelatedLinks})"
    
    def print_news(self):
        print(f"ID: {self.id}\n")
        print(f"Título: {self.title}\n")
        print(f"URL: {self.url}\n")
        print(f"Data de Publicação: {self.publicationDate}\n")
        print(f"Conteúdo: {self.content}\n")
        print(f"N° de links diretamente relacionados: {self.numDirectRelatedLinks}\n")
