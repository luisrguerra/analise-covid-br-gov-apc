#Funções basicas para uso geral

def lerCSV (arquivo):
    # Biblioteca necessária para ler arquivo .csv
    import csv
    return csv.reader(arquivo, delimiter=';')

def downloadArquivo (url,nome):
    import requests
    r = requests.get(url, allow_redirects=True)
    open(nome, 'wb').write(r.content)

#Carregar os arquivos CSV no Colab
def baixarArquivosCovid ():
    import os
    #Checar se o arquivo existe na pasta atual. Se não, baixar o arquivo
    if os.path.isfile("2020_covid.csv") == False:
        #URL arquivo 2020_covid.csv:  https://www.dropbox.com/s/rexr8ujc76u5xxh/2020_covid.csv?dl=1
        downloadArquivo('https://www.dropbox.com/s/rexr8ujc76u5xxh/2020_covid.csv?dl=1','2020_covid.csv')
    
    if os.path.isfile("10_09_2021_covid.csv") == False:
        #URL arquivo 10_09_2021_covid.csv:  https://www.dropbox.com/s/5zr6otkwtpv0xvy/10_09_2021_covid.csv?dl=1
        downloadArquivo('https://www.dropbox.com/s/5zr6otkwtpv0xvy/10_09_2021_covid.csv?dl=1','10_09_2021_covid.csv')

def dadosCovid(ano):
    if ano == "2020": 
       arquivo = open('2020_covid.csv', encoding="utf-8")
    elif ano == "2021":
       arquivo = open('10_09_2021_covid.csv', encoding="utf-8")
    # Biblioteca necessária para ler arquivo .csv
    import csv
    return csv.reader(arquivo, delimiter=';')  

#Função para dividir cada valor de uma lista pelos valores de outra lista, dividindo um por um.
#
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
    
#Funções para gerar gráficos

def graficoLinhaBasico (valorX,valorY):
    import plotly.graph_objects as go

    traco1 = go.Scatter(
       x = valorX,
       y = valorY,
       name = "",
    )
    data = [traco1]

    layout = go.Layout(title = "")
    fig = go.Figure(data=data, layout = layout)
    
    fig.update_xaxes(title_text = "")
    fig.update_yaxes(title_text = "")
    fig.show()

def graficoLinhaBasicoTitulo (titulo,valorX,valorY):
    import plotly.graph_objects as go

    traco1 = go.Scatter(
       x = valorX,
       y = valorY,
       name = "",
    )
    data = [traco1]

    layout = go.Layout(title = titulo)
    fig = go.Figure(data=data, layout = layout)
    
    fig.update_xaxes(title_text = "")
    fig.update_yaxes(title_text = "")
    fig.show()

def graficoLinhaDuploBasico (valorX,valorY1,valorY2):
    import plotly.graph_objects as go

    traco1 = go.Scatter(
       x = valorX,
       y = valorY1,
       name = "",
    )
    traco2 = go.Scatter(
       x = valorX,
       y = valorY2,
       name = "",      
    )
    data = [traco1, traco2]

    layout = go.Layout(title = "")
    fig = go.Figure(data=data, layout = layout)
    
    fig.update_xaxes(title_text = "")
    fig.update_yaxes(title_text = "")
    fig.show()

def graficoLinhaQuadruploBasico (titulo,valorX,valorY1,nomeY1,valorY2,nomeY2,valorY3,nomeY3,valorY4,nomeY4):
    import plotly.graph_objects as go

    traco1 = go.Scatter(
       x = valorX,
       y = valorY1,
       name = nomeY1,
    )
    traco2 = go.Scatter(
       x = valorX,
       y = valorY2,
       name = nomeY2,      
    )
    traco3 = go.Scatter(
       x = valorX,
       y = valorY3,
       name = nomeY3,      
    )
    traco4 = go.Scatter(
       x = valorX,
       y = valorY4,
       name = nomeY4,      
    )
    data = [traco1,traco2,traco3,traco4]

    layout = go.Layout(title = titulo)
    fig = go.Figure(data=data, layout = layout)
    
    fig.update_xaxes(title_text = "")
    fig.update_yaxes(title_text = "")
    fig.show()  

def graficoLinhaDuplo (titulo,valorX,valorY1,nomeY1,valorY2,nomeY2,tituloX,TituloY):
    import plotly.graph_objects as go

    traco1 = go.Scatter(
       x = valorX,
       y = valorY1,
       name = nomeY1,
    )
    traco2 = go.Scatter(
       x = valorX,
       y = valorY2,
       name = nomeY2,      
    )
    data = [traco1, traco2]

    layout = go.Layout(title = titulo)
    fig = go.Figure(data=data, layout = layout)
    
    fig.update_xaxes(title_text = tituloX)
    fig.update_yaxes(title_text = TituloY)
    fig.show()

def graficoLinhaQuadruplo (titulo,valorX1,valorY1,nomeY1,valorX2,valorY2,nomeY2,valorX3,valorY3,nomeY3,valorX4,valorY4,nomeY4):
      import plotly.graph_objects as go

      traco1 = go.Scatter(
         x = valorX1,
         y = valorY1,
         name = nomeY1,
      )
      traco2 = go.Scatter(
         x = valorX2,
         y = valorY2,
         name = nomeY2,      
      )
      traco3 = go.Scatter(
         x = valorX3,
         y = valorY3,
         name = nomeY3,      
      )
      traco4 = go.Scatter(
         x = valorX4,
         y = valorY4,
         name = nomeY4,      
      )
      data = [traco1,traco2,traco3,traco4]

      layout = go.Layout(title = titulo)
      fig = go.Figure(data=data, layout = layout)
    
      fig.update_xaxes(title_text = "")
      fig.update_yaxes(title_text = "")
      fig.show()

#Runtime comum para todos os códigos
baixarArquivosCovid();

#Simplificar os endereços das colunas
codigoEstado = 0
codigoMunicipio = 1
codigoRegiaoSaude = 2
codigoData = 3
codigoPopulacao = 4
codigoCasosAcumulados = 5
codigoCasosNovos = 6
codigoObitosAcumulados = 7
codigoObitosNovos = 8

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

#Gera gráficos de comparação entre casos/óbitos novos e casos/óbitos totais.
def municipioGraficos(ano,municipioEscolhido):
    
    dadosMunicipio =  filtrar(dadosCovid(ano),"municipio",municipioEscolhido)

    #Lista de cada dado, todos organizados na mesma ordem
    estado = filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"estado")
    municipio = filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"municipio")
    nomeRegiaoSaude = filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"nomeRegiaoSaude")
    data = filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"data")
    populacao = filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"populacao")
    casosAcumulados = filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"casosAcumulados")
    casosNovos = filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"casosNovos")
    obitosAcumulado = filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"obitosAcumulado")
    obitosNovos = filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"obitosNovos")

    textoAcumulados = municipioEscolhido + " - Casos Acumulados/Mortes Acumuladas"
    textoNovos =  municipioEscolhido + " - Casos Novos/Mortes Novas "

    graficoLinhaDuplo (textoAcumulados, #título
                       data, # valores de x
                       casosAcumulados, # valores de y1
                       "Casos Acumulados", # nome de y1
                       obitosAcumulado, # valores de y2
                       "Óbitos Acumulados", # nome de y2
                       "Data", # título do eixo x
                       "") # título do eixo y

    graficoLinhaDuplo (textoNovos,
                       data,
                       casosNovos,
                       "Casos Novos",
                       obitosNovos,
                       "Óbitos Novos",
                       "Data",
                       "")

# Gráficos de comparação entre os municípios
def acumuladosComparacao(ano,coluna,municipio1,municipio2,municipio3,municipio4):

    dadosMunicipio1 = filtrar(dadosCovid(ano),"municipio",municipio1)
    casosAcumuladosMunicipio1 = filtrarEmListaUnica(dadosMunicipio1,"municipio",municipio1,coluna)
    dataMunicipio1 = filtrarEmListaUnica(dadosMunicipio1,"municipio",municipio1,"data")
    populacaoMunicipio1 = filtrarEmListaUnica(dadosMunicipio1,"municipio",municipio1,"populacao")
    proporcaoMunicipio1 = dividirListaPorLista(casosAcumuladosMunicipio1,populacaoMunicipio1) #Divir cada valor da lista pelo valor da outra lista
    
    dadosMunicipio2 = filtrar(dadosCovid(ano),"municipio",municipio2)
    casosAcumuladosMunicipio2 = filtrarEmListaUnica(dadosMunicipio2,"municipio",municipio2,coluna)
    dataMunicipio2 = filtrarEmListaUnica(dadosMunicipio2,"municipio",municipio2,"data")
    populacaoMunicipio2 = filtrarEmListaUnica(dadosMunicipio2,"municipio",municipio2,"populacao")
    proporcaoMunicipio2 = dividirListaPorLista(casosAcumuladosMunicipio2,populacaoMunicipio2)
    
    dadosMunicipio3 = filtrar(dadosCovid(ano),"municipio",municipio3)
    casosAcumuladosMunicipio3 = filtrarEmListaUnica(dadosMunicipio3,"municipio",municipio3,coluna)
    dataMunicipio3 = filtrarEmListaUnica(dadosMunicipio3,"municipio",municipio3,"data")
    populacaoMunicipio3 = filtrarEmListaUnica(dadosMunicipio3,"municipio",municipio3,"populacao")
    proporcaoMunicipio3 = dividirListaPorLista(casosAcumuladosMunicipio3,populacaoMunicipio3)

    dadosMunicipio4 = filtrar(dadosCovid(ano),"municipio",municipio4)
    casosAcumuladosMunicipio4 = filtrarEmListaUnica(dadosMunicipio4,"municipio",municipio4,coluna)
    dataMunicipio4 = filtrarEmListaUnica(dadosMunicipio4,"municipio",municipio4,"data")
    populacaoMunicipio4 = filtrarEmListaUnica(dadosMunicipio4,"municipio",municipio4,"populacao")
    proporcaoMunicipio4 = dividirListaPorLista(casosAcumuladosMunicipio4,populacaoMunicipio4)
    
    if coluna == "casosAcumulados":
       tituloGrafico = "Comparação da proporção de casos acumulado entre os municípios de " + municipio1 + ", " + municipio2 + ", " + municipio3 + " e " + municipio4
    elif coluna == "obitosAcumulado":
       tituloGrafico = "Comparação da proporção de óbitos acumulado entre os municípios de " + municipio1 + ", " + municipio2 + ", " + municipio3 + " e " + municipio4
    else:
       tituloGrafico = ""
    
    graficoLinhaQuadruplo(
        tituloGrafico, #título
        dataMunicipio1, # valores de x1
        proporcaoMunicipio1, # valores de y1
        municipio1, # nome de x1
        dataMunicipio2, # valores de x2
        proporcaoMunicipio2, # valores de y2
        municipio2, # nome de x2
        dataMunicipio3, # valores de x3
        proporcaoMunicipio3, # valores de y3
        municipio3, # nome de x3
        dataMunicipio4, # valores de x4
        proporcaoMunicipio4, # valores de y4
        municipio4 # nome de x4
        )

acumuladosComparacao("2021","casosAcumulados","Cristalina","Águas Lindas de Goiás","Formosa","Planaltina")

acumuladosComparacao("2021","obitosAcumulado","Cristalina","Águas Lindas de Goiás","Formosa","Planaltina")

municipioGraficos("2021","Cristalina")