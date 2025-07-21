# NewsCausalGraphLearning

O seguinte repositório contém o código fonte do projeto de iniciação científica "Mineração de
Redes de Eventos com _Graph Neural Networks_", desenvolvido por Lucas Piovani Ferreira (Nusp 13836813)
sob a orientação do Prof. Dr. Ricardo Marcondes Marcacini, do Instituto de Ciências Matemáticas e de
Computação da Universidade de São Paulo (ICMC USP).

## Introdução

Eventos representam ocorrências específicas associadas a um momento e local
determinados, sendo frequentemente extraídos de fontes como redes sociais e portais de notícias
para análises em diferentes áreas, como epidemias, conflitos e relações econômicas. Métodos
computacionais têm sido desenvolvidos para analisar essas informações, permitindo detectar
padrões e antecipar tendências.

Apesar dos avanços, a tarefa de representar eventos de maneira adequada para algoritmos
de classificação continua sendo um desafio. Muitas abordagens tradicionais focam apenas no
texto, o que pode limitar a captura das relações complexas entre eventos, como conexões
temporais, espaciais e causais. Além disso, essas representações são frequentemente criticadas
pela falta de uma estrutura semântica rica e pela dificuldade de interpretar o significado dos
eventos de forma contextualizada. Por isso, há um crescente interesse no uso de técnicas mais
avançadas, como aprendizado de máquina e redes neurais de grafos, para modelar essas relações
de forma mais expressiva e eficaz.

## Objetivo

O objetivo deste projeto é aprimorar a mineração de redes de eventos a partir de fontes de
notícias, como o G1, para construir um grafo rico em relações entre diferentes acontecimentos. A
partir da extração e estruturação de notícias, busca-se modelar conexões temporais, espaciais e
semânticas entre eventos, permitindo uma análise mais aprofundada das dinâmicas que os regem.

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