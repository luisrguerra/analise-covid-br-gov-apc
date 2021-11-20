import dash
from dash import dcc
from dash import html

import analiseDash

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.H1(children="Analise de dados Covid",),
        html.P(
            children="Fonte: covid.saude.gov.br",
        ),
        dcc.Graph(figure = analiseDash.acumuladosComparacao("2021","obitosAcumulado","Cristalina","Águas Lindas de Goiás","Formosa","Planaltina") ),
        dcc.Graph(figure = analiseDash.municipioGraficos("2021","Cristalina","novos") ),
        dcc.Graph(figure = analiseDash.municipioGraficos("2021","Cristalina","acumulados") ),
    ],
    style = {'font-family':'Helvetica, sans-serif','margin':'1em'}
)
#figure = stock_prices()
if __name__ == "__main__":
    app.run_server(debug=False)