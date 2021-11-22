import plotly.express as px
import pandas as pd
 
#import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
 
from app import app #change this line
 
# Data Preprocessing
dg = pd.read_csv('supermarket_sales - Sheet1.csv')
dg = dg.rename(
        columns = {
            "Product line" : "Product_line",
            "Customer type" : "Customer_type"
        })
    
       
 
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Grafik Total Pada Supermarket Sales"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Memvisualisasikan grafik Pie Chart'),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Dropdown(
                    id='City',
                    options=[
                       {"label" : City, "value" : City} for City in dg.City.unique()
                       
                    ],
                    value='Mandalay',
            
                ),
                className="mb-4"
            )
        ]),
        dbc.Row([
            dbc.Col(
                dcc.Graph(
                    id='the_graph'
                )
            )
        ])
    ])
])
 

@app.callback(
    Output('the_graph', 'figure'),
    Input('City', 'value')
)
def update_graph(City):
   d3 = dg.groupby(['Product_line', 'City'])[['Total']].sum().reset_index()
   d4 = d3[d3['City'] == City]
   piechart = px.pie(d4, names = 'Product_line', values = 'Total', height=600, title=f'Total dari Product Line Dan Gender')

   return piechart    