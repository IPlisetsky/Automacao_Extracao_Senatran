from tkinter.filedialog import askdirectory
import Senatran_webscraper
from Senatran_webscraper import WebScraper
import time
import os

quantidade_paginas = 4

def info():
    print("ADQUIRcopy(document.body.innerText);IR INFOS...")
    time.sleep(3)
    Scraper = WebScraper()
    quantidade_paginas = 4
    time.sleep(5)
    Scraper.adquirir_dados(quantidade_paginas,check=False)

def baixa():
    print("BAIXAR CRLVs...")
    time.sleep(5)
    Scraper = WebScraper()
    Scraper.adquirir_crlvs()
    #   Mover para pasta certa
    origem = askdirectory()
    caminho = askdirectory()
    #origem = r"C:\Users\igor.gabriel\OneDrive - JSL SA\Área de Trabalho\CRLV_eu\PDFS"
    #caminho = r"C:\Users\igor.gabriel\OneDrive - JSL SA\Área de Trabalho\CRLV_eu\PDF2"
    lista_arquivos = os.listdir(origem)
    for arquivo in lista_arquivos:
        if ".pdf" in arquivo:
            print(f"\nLENDO {arquivo}...\n")
            os.replace(f"{origem}/{arquivo}", f"{caminho}/{arquivo}")
            print("MOVIDO") 
        else:
            pass
