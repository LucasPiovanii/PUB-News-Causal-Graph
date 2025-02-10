# NewsCausalGraphLearning

## Organização do Diretório

```bash
NewsCausalGraphLearning/
│
├── main.py
├── news_scraper/
│   ├── news.py            # Define a classe News
│   ├── scraper.py         # Contém a lógica de scraping
│   ├── graph_builder.py   # Funções para construção do grafo
│   ├── graph_plotter.py   # Funções para configuração e plotagem do grafo
│   └── utils.py           # Funções utilitárias como o process_links
└── requirements.txt       # Dependências do projeto (Selenium, igraph etc.)
```

Obs: O Selenium está configurado para o driver do Safari

## Instruções para execução local

### 1. Criação do Ambiente Virtual

É recomendável criar um ambiente virtual para isolar as dependências:

```bash
python3 -m venv venv
source venv/bin/activate  # Para macOS/Linux
venv\Scripts\activate     # Para Windows
```

### 2. Instalação das Dependências

Instale as dependências do projeto a partir do arquivo requirements.txt

```bash
pip install -r requirements.txt
```

### 3. Execução da Aplicação

Após a configuração, execute a aplicação com o comando:

```bash
python3 main.py
```

### 4. Desativação do Ambiente Virtual

```bash
deactivate
```