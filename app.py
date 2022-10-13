from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__)

df = pd.read_csv('updated_csv.csv', parse_dates=['date'])

fig = px.line(df, x="date", y="sales", color="region")

app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Sales'
    ),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)


