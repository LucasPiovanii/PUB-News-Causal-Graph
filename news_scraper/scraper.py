# news_scraper/scraper.py

from queue import Queue
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from .news import News
from .utils import process_links

# Função para extrair os dados do site e armazenar na classe
def scrape_news(url, link_queue):
    options = webdriver.SafariOptions()
    driver = webdriver.Safari(options=options)

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "content-head__title"))
        )

        title = driver.find_element(By.CLASS_NAME, "content-head__title").text

        try:
            # Para casos em que a notícia não tem subtítulo
            subtitle = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "content-head__subtitle"))
            ).text
        except TimeoutException:
            subtitle = "Sem subtítulo disponível"

        publication_date = driver.find_element(By.TAG_NAME, "time").text

        # Encontrar todos os links na página e adicionar à fila
        num_direct_related_links = process_links(driver, link_queue, url)

        # Extrair o conteúdo: pegar todos os parágrafos, h2, h3... dentro da área de conteúdo
        content_elements = driver.find_elements(By.CSS_SELECTOR, ".content-text p, .content-text h2, .content-text h3, .content-text blockquote")
        content = "\n".join([element.text for element in content_elements]) # concatenar!

        news = News(id="1", title=title, subtitle=subtitle, url=url, publicationDate=publication_date, content=content, numDirectRelatedLinks=num_direct_related_links)

        return news

    finally:
        driver.quit()