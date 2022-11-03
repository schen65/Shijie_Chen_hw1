from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import datetime as dt
import random

app = Dash('profect_folder_2')

def serve_layout():
    df = pd.DataFrame({
    'City':['NY','Sea','knox'],
    'Value':[random.randint(1,10),
             random.randint(1,100),
             random.randint(1,50)]
    })

    fig = px.bar(df, x='City', y= 'Value')


    return html.Div(children=[
        html.H1(children='Dynamic Dash App'),

        html.Div(children= 'This data is retrieved at' + str(dt.datetime.now())),

        dcc.Graph(
        id ='example-graph',
        figure =fig
    )
])

app.layout = serve_layout()
app.run_server(debug = True)