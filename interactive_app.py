from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd


app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('updated_csv.csv', parse_dates=['date'])


app.layout = html.Div(children=[
    html.H1(
        children='Pink Morsel Sales'
    ),

    dcc.Graph(
        id='my-graph'
    ),
    dcc.RadioItems(
        ['north', 'south', 'east', 'west','all'], 'all', id='region'
    )
])


@app.callback(
    Output('my-graph', 'figure'),
    Input('region', 'value'))
def update_graph(region_value):
    dff = df[df['region'] == region_value]
    fig = px.line(dff, x='date', y='sales', color='region')
    fig1 = px.line(df, x='date', y='sales', color='region')
    if region_value == 'all':
        return fig1
    else:
        return fig


if __name__ == '__main__':
    app.run_server(debug=True)

