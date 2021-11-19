import dash
from dash import dcc
from dash import html

app = dash.Dash()

app.layout = html.Div(
    children=[
        html.H1(children="Analise de dados Covid",),
        html.P(
            children="Fonte: covid.saude.gov.br",
        ),
    ],
    style = {'font-family':'Helvetica, sans-serif','margin':'1em'}
)

if __name__ == "__main__":
    app.run_server(debug=True)