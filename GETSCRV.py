import re

def has_numbers(inputString):
    print(inputString)
    return any(char.isdigit() for char in inputString)

def getRenavam(string):
    pattern = 'CÓDIGO RENAVAM'
    lines_number  = []
    for m in re.finditer(pattern, string):
        start = m.start()
        lineno = string.count('\n', 0, start)
        lines_number.append(lineno)
        break

    for l in lines_number:
        #print("Renavam extraido.....:"+string.split('\n')[l+1])
        return(string.split('\n')[l+1])

def getCOR(string):
    pattern = 'COR PREDOMINANTE'
    lines_number  = []
    try:
        for m in re.finditer(pattern, string):
            start = m.start()
            lineno = string.count('\n', 0, start)
            lines_number.append(lineno)
            break
        for l in lines_number: 
            if (string.split('\n')[l+6]) =="COMBUSTÍVEL":
                #print ("Cor encontrada......:"+string.split('\n')[l+2])
                return (string.split('\n')[l+2])
            elif (string.split('\n')[l+6]) =="CATEGORIA":
                #print ("Cor encontrada......:"+string.split('\n')[l+1])
                return (string.split('\n')[l+1])
            elif has_numbers(string.split('\n')[l+6])==True:
                #print ("Cor encontrada......:"+string.split('\n')[l+6])
                return (string.split('\n')[l+1])    
        else:
            #print ("Cor encontrada......:"+string.split('\n')[l+6])
            return(string.split('\n')[l+2])
    except:
        return "Erro na leitura"        

def getCombustivel(string):
    pattern = 'COMBUSTÍVEL'
    lines_number  = []
    for m in re.finditer(pattern, string):
        start = m.start()
        lineno = string.count('\n', 0, start)
        lines_number.append(lineno)
        break

    for l in lines_number:
        #print("Combustivel Extraido....:"+string.split('\n')[l+4])
        return(string.split('\n')[l+4])                      

def getAnoModelo(string):
    pattern = 'ANO MODELO'
    lines_number  = []
    for m in re.finditer(pattern, string):
        start = m.start()
        lineno = string.count('\n', 0, start)
        lines_number.append(lineno)
        break

    for l in lines_number:
        #print("AnoModelo Extraido....:"+string.split('\n')[l+1])
        return(string.split('\n')[l+1])

def getCategoria(string):
    pattern = 'CATEGORIA'
    lines_number  = []
    for m in re.finditer(pattern, string):
        start = m.start()
        lineno = string.count('\n', 0, start)
        lines_number.append(lineno)
        break

    for l in lines_number:
        #print("Categoria Extraida...:"+string.split('\n')[l+1])
        return(string.split('\n')[l+1])

def getCarroceria(string):
    pattern = 'CARROCERIA'
    lines_number  = []
    for m in re.finditer(pattern, string):
        start = m.start()
        lineno = string.count('\n', 0, start)
        lines_number.append(lineno)
        break

    for l in lines_number:
        #print("Carroceria Extraida...:"+string.split('\n')[l+1])
        return(string.split('\n')[l+1])

def getNome(string):
    pattern = 'NOME'
    lines_number  = []
    for m in re.finditer(pattern, string):
        start = m.start()
        lineno = string.count('\n', 0, start)
        lines_number.append(lineno)
        break

    for l in lines_number:
        #print("Nome extraido......:"+string.split('\n')[l+1])
        return(string.split('\n')[l+1])

def getLocal(string):
    pattern = 'LOCAL'
    lines_number  = []
    for m in re.finditer(pattern, string):
        start = m.start()
        lineno = string.count('\n', 0, start)
        lines_number.append(lineno)
        break
    for l in lines_number: 
        if (string.split('\n')[l+2]) =="CPF / CNPJ":
            #print ("Local encontrado......:"+string.split('\n')[l+7])
            return (string.split('\n')[l+7])
        elif (string.split('\n')[l+2]) =="PESO BRUTO TOTAL":
            #print ("Local encontrado......:"+string.split('\n')[l+21])
            return (string.split('\n')[l+21])
    else:
        #print ("Local encontrado......:"+string.split('\n')[l+2])
        return(string.split('\n')[l+2])        

def getData(string):
    pattern = 'DATA'
    lines_number  = []
    for m in re.finditer(pattern, string):
        start = m.start()
        lineno = string.count('\n', 0, start)
        lines_number.append(lineno)
        break
    for l in lines_number:
        if (string.split('\n')[l+4]) == "ASSINADO DIGITALMENTE PELO DETRAN":
            #print("Data extraida......:"+string.split('\n')[l+2])
            return(string.split('\n')[l+2])
        else:
            #print("Data extraida......:"+string.split('\n')[l+4])
            return(string.split('\n')[l+4])

def getDataRE(test_string):        
    res = re.findall(r'[0-2][0-9]/[0-10][0-9]/[0-9][0-9][0-9][0-9]',test_string)
    if res == []:
        return getData(test_string)
                
    else:
        #print("Data extraida......:"+str(res))
        return res

def getCRV(string):
    pattern = 'NÚMERO DO CRV'
    lines_number  = []
    for m in re.finditer(pattern, string):
        start = m.start()
        lineno = string.count('\n', 0, start)
        lines_number.append(lineno)
        break
    for l in lines_number:
        #print("CRV extraido.......:"+string.split('\n')[l+1])
        return(string.split('\n')[l+1])

def getTipo(string):
    pattern = 'ESPÉCIE / TIPO'
    lines_number  = []
    for m in re.finditer(pattern, string):
        start = m.start()
        lineno = string.count('\n', 0, start)
        lines_number.append(lineno)
        break
    for l in lines_number:
        #print("Tipo extraido......:"+string.split('\n')[l+2])
        return(string.split('\n')[l+2])

def getCNPJ(string):
    pattern = 'CPF / CNPJ'
    lines_number  = []
    for m in re.finditer(pattern, string):
        start = m.start()
        lineno = string.count('\n', 0, start)
        lines_number.append(lineno)
        break
    for l in lines_number:
        #print("CNPJ encontrado......:"+string.split('\n')[l+1])
        return(string.split('\n')[l+1])

def getChassi(string):
    pattern = 'CHASSI'
    lines_number  = []
    for m in re.finditer(pattern, string):
        start = m.start()
        lineno = string.count('\n', 0, start)
        lines_number.append(lineno)
        break
    for l in lines_number:
        #print("Chassi encontrado.......:"+string.split('\n')[l+5])
        return(string.split('\n')[l+5])

def getPlaca(string):
    pattern = 'PLACA'
    lines_number  = []
    for m in re.finditer(pattern, string):
        start = m.start()
        lineno = string.count('\n', 0, start)
        lines_number.append(lineno)
        break
    for l in lines_number:
        #print("Placa encontrada.......:"+string.split('\n')[l+1])
        return(string.split('\n')[l+1])        

def getModelo(string):
    pattern = 'MARCA / MODELO'
    lines_number  = []
    for m in re.finditer(pattern, string):
        start = m.start()
        lineno = string.count('\n', 0, start)
        lines_number.append(lineno)
        break
    for l in lines_number: 
        if (string.split('\n')[l+2]) =="CAT":
            #print ("Modelo encontrado......:"+string.split('\n')[l+6])
            return (string.split('\n')[l+6])
    else:
        #print ("Modelo encontrado......:"+string.split('\n')[l+2])
        return(string.split('\n')[l+2])        
def getFab(string):
    pattern = 'ANO FABRICAÇÃO'
    lines_number  = []
    for m in re.finditer(pattern, string):
        start = m.start()
        lineno = string.count('\n', 0, start)
        lines_number.append(lineno)
        break
    for l in lines_number: 
            #print ("Ano Fabricação encontrado......:"+string.split('\n')[l+1])
            return (string.split('\n')[l+1])
    

def getExerc(string):
  global ano
  pattern = 'EXERCÍCIO'
  lines_number = []
  for m in re.finditer(pattern, string):
    start = m.start()
    lineno = string.count('\n', 0, start)
    lines_number.append(lineno)
    break
  for l in lines_number: 
    print ("Ano Fabricação encontrado......:"+string.split('\n')[l+1])
    ano = string.split('\n')[l+1]
    return (string.split('\n')[l+1])

def GetChassiRe(i):
  test_string = ""
  lista = []
  test_string = i 
  res = re.findall(r"\b[A-Z0-9]{17}\b",test_string)
  for i in res: 
    if i not in lista:
        lista.append(i)
  if lista:
    return lista
  #print("Nenhum chassi encontrado!")
  return   

def get_placa_RE(i):
    pattern = r'\b[A-Z]{3}[0-9]{4}\b'
    placas = re.findall(pattern, i)
    return placas
