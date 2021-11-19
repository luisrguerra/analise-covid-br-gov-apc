def diretorioAtual():
    #trocar diretório atual para a pasta do programa
    import os
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

def dadosCovid(ano):

    if ano == "2020": 
       arquivo = open('dados/2020_covid.csv', encoding="utf-8")
    elif ano == "2021":
       arquivo = open('dados/10_09_2021_covid.csv', encoding="utf-8")
    # Biblioteca necessária para ler arquivo .csv
    import csv
    return csv.reader(arquivo, delimiter=';')  

#Função para dividir cada valor de uma lista pelos valores de outra lista, dividindo um por um.
def dividirListaPorLista (lista1,lista2):
  return [ float(i)/float(j) for i,j in zip(lista1,lista2)]

def codigoColuna (nomeColuna):
    if nomeColuna == "estado":
       return 0
    elif nomeColuna == "municipio":
       return 1
    elif nomeColuna == "nomeRegiaoSaude":
       return 2
    elif nomeColuna == "data":
       return 3
    elif nomeColuna == "populacao":
       return 4
    elif nomeColuna == "casosAcumulados":
       return 5
    elif nomeColuna == "casosNovos":
       return 6
    elif nomeColuna == "obitosAcumulado":
       return 7
    elif nomeColuna == "obitosNovos":
       return 8

# Usado para filtrar os dados do município apartir do banco de dados
# Usado para melhorar a perfomance de busca antes de utilizar a função de filtrar em lista única
def filtrar(dados,filtro,busca):

    filtroSelecionado = codigoColuna(filtro)

    linhas = dados

    resultado = []

    contagem = 0 #Contagem da posição
    for linha in linhas:
        if (contagem == 0):
            resultado.append(linha)
        elif (contagem > 0 and linha[filtroSelecionado] == busca):
            resultado.append(linha)
        contagem = contagem + 1 #Próxima posição na contagem

    return resultado

#Retorna uma lista de dados única com dados de uma coluna
def filtrarEmListaUnica(dados,filtro,busca,coluna):

    filtroSelecionado = codigoColuna(filtro)
    colunaSelecionado = codigoColuna(coluna)
    linhas = dados

    resultado = []

    contagem = 0 #Contagem da posição
    for linha in linhas:
        if (contagem > 0 and linha[filtroSelecionado] == busca):
            resultado.append(linha[colunaSelecionado])
        contagem = contagem + 1 #Próxima posição na contagem

    return resultado