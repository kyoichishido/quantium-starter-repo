# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'text': '#7FDBFF'
}

columns_name = ['sales', "date", "region"]
df = pd.read_csv("output.csv", names=columns_name)

fig = px.line(df, x="date", y="sales",labels={'date':'Period', 'sales':'Total Sales'})
fig.update_layout(font_color=colors['text'])


app.layout = html.Div(children=[
    html.H1(children="Soul Foods's Sales",
            style={'textAlign': 'center'}),

    html.Div(children='''
        The Sales Data Visualizer.
    ''', style={'textAlign': 'center'}),

    dcc.Graph(
        id='line chart',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
