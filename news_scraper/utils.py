# news_scraper/utils.py

from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

# Função que encontra todos os links relacionados à notícia e insere na fila
def process_links(driver, link_queue, original_url):
    num_direct_related_links = 0 # contador para auxiliar no processamento da fila
    
    # Extrai o padrão do link original (até "/noticia/")
    base_url = original_url.split("/noticia/")[0] + "/noticia/"
    
    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        try:
            href = link.get_attribute("href")
            if href:
                # Remove qualquer fragmento (parte após '#')
                href_no_fragment = href.split('#')[0]
                
                # Extrai a substring até "/noticia/" para o link atual
                href_base = href_no_fragment.split("/noticia/")[0] + "/noticia/"

                # Verifica se o link sem fragmento e o original são diferentes
                if href_base == base_url and href_no_fragment != original_url and href_no_fragment not in link_queue.queue:
                    link_queue.put(href_no_fragment)
                    num_direct_related_links += 1

        except StaleElementReferenceException:
            # Tratar casos de StaleElementReferenceException
            # Obs: não entendi muito bem por que precisa disso, mas tava travando sem e precisei gepetar :(
            link = driver.find_element(By.TAG_NAME, "a")
            href = link.get_attribute("href")
            if href:
                href_no_fragment = href.split('#')[0]
                href_base = href_no_fragment.split("/noticia/")[0] + "/noticia/"
                if href_base == base_url and href_no_fragment != original_url and href_no_fragment not in link_queue.queue:
                    link_queue.put(href_no_fragment)
                    num_direct_related_links += 1

    return num_direct_related_links