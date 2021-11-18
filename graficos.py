#Funções para gerar gráficos

def linhaBasico (valorX,valorY):
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

def linhaBasicoTitulo (titulo,valorX,valorY):
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

def linhaDuploBasico (valorX,valorY1,valorY2):
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

def linhaQuadruploBasico (titulo,valorX,valorY1,nomeY1,valorY2,nomeY2,valorY3,nomeY3,valorY4,nomeY4):
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

def linhaDuplo (titulo,valorX,valorY1,nomeY1,valorY2,nomeY2,tituloX,TituloY):
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

def linhaQuadruplo (titulo,valorX1,valorY1,nomeY1,valorX2,valorY2,nomeY2,valorX3,valorY3,nomeY3,valorX4,valorY4,nomeY4):
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