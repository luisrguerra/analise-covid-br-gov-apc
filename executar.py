import funcoes
import graficos

funcoes.diretorioAtual()

#Gera gráficos de comparação entre casos/óbitos novos e casos/óbitos totais.
def municipioGraficos(ano,municipioEscolhido):
    
    dadosMunicipio =  funcoes.filtrar(funcoes.dadosCovid(ano),"municipio",municipioEscolhido)

    #Lista de cada dado, todos organizados na mesma ordem
    #estado = filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"estado")
    #municipio = filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"municipio")
    #nomeRegiaoSaude = filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"nomeRegiaoSaude")
    data = funcoes.filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"data")
    #populacao = filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"populacao")
    casosAcumulados = funcoes.filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"casosAcumulados")
    casosNovos = funcoes.filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"casosNovos")
    obitosAcumulado = funcoes.filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"obitosAcumulado")
    obitosNovos = funcoes.filtrarEmListaUnica(dadosMunicipio,"municipio",municipioEscolhido,"obitosNovos")

    textoAcumulados = municipioEscolhido + " - Casos Acumulados/Mortes Acumuladas"
    textoNovos =  municipioEscolhido + " - Casos Novos/Mortes Novas "

    graficos.linhaDuplo (textoAcumulados, #título
                       data, # valores de x
                       casosAcumulados, # valores de y1
                       "Casos Acumulados", # nome de y1
                       obitosAcumulado, # valores de y2
                       "Óbitos Acumulados", # nome de y2
                       "Data", # título do eixo x
                       "") # título do eixo y

    graficos.linhaDuplo (textoNovos,
                       data,
                       casosNovos,
                       "Casos Novos",
                       obitosNovos,
                       "Óbitos Novos",
                       "Data",
                       "")

# Gráficos de comparação entre os municípios
def acumuladosComparacao(ano,coluna,municipio1,municipio2,municipio3,municipio4):

    dadosMunicipio1 = funcoes.filtrar(funcoes.dadosCovid(ano),"municipio",municipio1)
    casosAcumuladosMunicipio1 = funcoes.filtrarEmListaUnica(dadosMunicipio1,"municipio",municipio1,coluna)
    dataMunicipio1 = funcoes.filtrarEmListaUnica(dadosMunicipio1,"municipio",municipio1,"data")
    populacaoMunicipio1 = funcoes.filtrarEmListaUnica(dadosMunicipio1,"municipio",municipio1,"populacao")
    proporcaoMunicipio1 = funcoes.dividirListaPorLista(casosAcumuladosMunicipio1,populacaoMunicipio1) #Divir cada valor da lista pelo valor da outra lista
    
    dadosMunicipio2 = funcoes.filtrar(funcoes.dadosCovid(ano),"municipio",municipio2)
    casosAcumuladosMunicipio2 = funcoes.filtrarEmListaUnica(dadosMunicipio2,"municipio",municipio2,coluna)
    dataMunicipio2 = funcoes.filtrarEmListaUnica(dadosMunicipio2,"municipio",municipio2,"data")
    populacaoMunicipio2 = funcoes.filtrarEmListaUnica(dadosMunicipio2,"municipio",municipio2,"populacao")
    proporcaoMunicipio2 = funcoes.dividirListaPorLista(casosAcumuladosMunicipio2,populacaoMunicipio2)
    
    dadosMunicipio3 = funcoes.filtrar(funcoes.dadosCovid(ano),"municipio",municipio3)
    casosAcumuladosMunicipio3 = funcoes.filtrarEmListaUnica(dadosMunicipio3,"municipio",municipio3,coluna)
    dataMunicipio3 = funcoes.filtrarEmListaUnica(dadosMunicipio3,"municipio",municipio3,"data")
    populacaoMunicipio3 = funcoes.filtrarEmListaUnica(dadosMunicipio3,"municipio",municipio3,"populacao")
    proporcaoMunicipio3 = funcoes.dividirListaPorLista(casosAcumuladosMunicipio3,populacaoMunicipio3)

    dadosMunicipio4 = funcoes.filtrar(funcoes.dadosCovid(ano),"municipio",municipio4)
    casosAcumuladosMunicipio4 = funcoes.filtrarEmListaUnica(dadosMunicipio4,"municipio",municipio4,coluna)
    dataMunicipio4 = funcoes.filtrarEmListaUnica(dadosMunicipio4,"municipio",municipio4,"data")
    populacaoMunicipio4 = funcoes.filtrarEmListaUnica(dadosMunicipio4,"municipio",municipio4,"populacao")
    proporcaoMunicipio4 = funcoes.dividirListaPorLista(casosAcumuladosMunicipio4,populacaoMunicipio4)
    
    if coluna == "casosAcumulados":
       tituloGrafico = "Comparação da proporção de casos acumulado entre os municípios de " + municipio1 + ", " + municipio2 + ", " + municipio3 + " e " + municipio4
    elif coluna == "obitosAcumulado":
       tituloGrafico = "Comparação da proporção de óbitos acumulado entre os municípios de " + municipio1 + ", " + municipio2 + ", " + municipio3 + " e " + municipio4
    else:
       tituloGrafico = ""
    
    graficos.linhaQuadruplo(
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