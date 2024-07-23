from tkinter import filedialog 
import TEXTOPDF as topdf
from GETSCRV import *
from get_pdfs import pdfGet
import pandas as pd
import datetime
import os

def ini_crlv_pdf(imprimir=False): # Ativado por botão em "gui_novo.py"
    if not os.path.exists('Planilhas'):
        os.makedirs('Planilhas') # Se não existir pasta "Planilhas", será criada
    contador = 0
    text = ""
    df_final = pd.DataFrame() # Cria um dataframe final
    dia_atual = str(datetime.datetime.now()).split()[0] # Pega a data atual
    Lista_pdfs = "" 
    dt_erro = pd.DataFrame() # Cria um dataframe para erro
    diretorio = filedialog.askdirectory() 
    #diretorio = r"C:\Users\igor.gabriel\OneDrive - JSL SA\Área de Trabalho\IGOR"
    d = diretorio.split('/')
    #nome_planilha = d[-1]
    Lista_pdfs = pdfGet(diretorio) # Le os arquivos da pasta "diretorio" usando o Get_pdfs.py
    total = len(Lista_pdfs) # Conta quantos arquivos tem em "Lista_pdfs"
    print ("".join(["\nEncontrada os seguintes pdfs: ",str(Lista_pdfs)]))
    print ("".join(["\nTotal de ",str(total)," pdfs encontrados"]))
    print ("\nIniciando Processo de leitura de pdfs...")

    for i in (Lista_pdfs):
        try:
            ##### SEPARAR DOCUMENTO POR PAGINAS, PRA LER INDIVIDUALMENTE, DOCUMENTO DE PAGINA 08/07
            print(diretorio)
            print(i)
            print("".join([str(diretorio),'/',str(i)]))
            
            #text = topdf.convert_pdf_to_string((str(diretorio)+'/'+str(i)))

            text = topdf.convert_pdf_to_string("".join([str(diretorio),'/',str(i)])) 
            if imprimir==True:
                print(text)
                return
        #if a :
            #cnpj_vamos = getCNPJ(text)#
            #cor_extraida = getCOR(text)#
            #renavam_extraido = getRenavam(text)#
            #combustivel_extraido =  getCombustivel(text)#
            #ano_modelo_extraido = getAnoModelo(text)#
            #categoria_extraida = getCategoria(text)#
            #carroceria_extraida= getCarroceria(text)#
            #nome_extraido = getNome(text)#
            #local_extraido= getLocal(text)#
            #data_extraida =getDataRE(text)#
            #crv_extraido =getCRV(text)#
            #tipo_extraido =getTipo(text)#
            #cnpj_extraido =getCNPJ(text)
            #placa = getPlaca(text)#
            #chassi_extraido=GetChassiRe(text)#
            #ano_fab_extraido = getFab(text)#
            #modelo_extraido=getModelo(text)#

            dados = {"Arquivo":i,"Cnpj Vamos":getCNPJ(text),"Chassi":GetChassiRe(text),"Placa":getPlaca(text),"Renavam":getRenavam(text),"Cor":getCOR(text),"Combustivel":getCombustivel(text),"Ano Modelo":getAnoModelo(text),"Ano Fabricacao":getFab(text),"Categoria":getCategoria(text),"Carroceria":getCarroceria(text),"Nome":getNome(text),"Local":getLocal(text),"Data":getData(text),"CRV":getCRV(text),"Tipo":getTipo(text),"Modelo":getModelo(text)}
            print(dados)
            df_temp = pd.DataFrame(dados)
            df_final = pd.concat([df_final,df_temp])
            
            contador+=1
            progresso = round((contador/total)*100,2)
            print("".join([str(contador)," de ",str(total),"  ",str(progresso),"% concluido"]))
            if contador % 500 == 0:
                #print(df_final)
                print("#############################SALVANDO##############################")
                try:
                    df_final.to_excel('Planilhas/'+dia_atual+f'.xlsx')
                except:
                    pass

        except Exception as e:
            contador+=1
            print("".join(["ERRO NO ARQUIVO '",str(i),f"': {e}, continuando."]))
            df_temp = pd.DataFrame()
            df_temp["Arquivo"] = [i]
            dt_erro = pd.concat([dt_erro,df_temp])
            progresso = round((contador/total)*100,2)
            if contador % 500 == 0:
                try:
                    df_final.to_excel('Planilhas/'+dia_atual+f'.xlsx')
                except:
                    pass
            print("".join([str(contador)," de ",str(total),"  ",str(progresso),"% concluido"]))
    dt_erro.to_excel('Planilhas/'+dia_atual+'-Erros.xlsx')     
    df_final.to_excel('Planilhas/'+dia_atual+'-Final.xlsx')