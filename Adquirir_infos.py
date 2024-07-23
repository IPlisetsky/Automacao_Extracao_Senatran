from Senatran_webscraper import WebScraper
import time

Scraper = WebScraper()
quantidade_paginas = 4
time.sleep(5)
Scraper.adquirir_dados(quantidade_paginas,check=False)

