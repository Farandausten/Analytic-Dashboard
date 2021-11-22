#from dash_html_components.H1 import H1
#import plotly.express as px
import pandas as pd
import dash
#import dash_core_components as dcc
import dash_html_components as html
#from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from scipy.special.orthogonal import jacobi
#from statsmodels.stats.anova import anova_lm
import scipy.stats as stats
import dash_table
from dash_table import DataTable 
from app import app #change this line
 
# Data Preprocessing
dg = pd.read_csv('supermarket_sales - Sheet1.csv')
dg = dg.rename(
        columns = {
            "Product line" : "Product_line",
            "Customer type" : "Customer_type"
        })
#1.         
dg_pivot = dg.groupby(['Product_line', 'City']).count()[['Gender']].reset_index()
dg_pivot = dg_pivot.pivot(index = 'Product_line', columns= 'City', values = 'Gender').fillna(0)
chisq1, pvalue1, df, expected = stats.chi2_contingency(dg_pivot)
dg_pivot     



#2. 
dg_pivot1 = dg.groupby(['Product_line', 'Customer_type']).count()[['Gender']].reset_index()
dg_pivot1 = dg_pivot1.pivot(index = 'Product_line', columns= 'Customer_type', values = 'Gender').fillna(0)
chisq2, pvalue2, df, expected = stats.chi2_contingency(dg_pivot1)
dg_pivot1

#3. 
dg_pivot2 = dg.groupby(['Product_line', 'Gender']).count()[['City']].reset_index()
dg_pivot2 = dg_pivot2.pivot(index = 'Product_line', columns= 'Gender', values = 'City').fillna(0)
chisq3, pvalue3, df, expected = stats.chi2_contingency(dg_pivot2)
dg_pivot2

#4.
dg_pivot3 = dg.groupby(['Product_line', 'Payment']).count()[['Gender']].reset_index()
dg_pivot3 = dg_pivot3.pivot(index = 'Product_line', columns= 'Payment', values = 'Gender').fillna(0)
chisq4, pvalue4, df, expected = stats.chi2_contingency(dg_pivot3)
dg_pivot3 

columns = [
    dict(id='Product_line', name='Product Line')
]

data = [
    dict(Product_line='Electronic accessories'),
    dict(Product_line='Fashion accessories'),
    dict(Product_line='Food and beverages'),
    dict(Product_line='Health and beauty'),
    dict(Product_line='Home and lifestyle'),
    dict(Product_line='Sports and travel')
]
#5. 
#6.
# 7.
# 8.
# 9.
# 10.  


layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1(children="CHI SQUARE TESTING"),
                className="mb-2 mt-2"
            )
        ]),
        dbc.Row([
            dbc.Col(
                html.H6(children='Chi2 testing digunakan ketika Anda ingin tahu apakah efeknya nyata atau mungkin tidak. Uji CHI Square digunakan untuk menguji dua kelompok data baik variabel independen maupun dependennya berbentuk kategorik atau dapat juga dikatakan sebagai uji proporsi untuk dua peristiwa atau lebih, sehingga datanya bersifat diskrit'),
                className="mb-4"
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.H6(children='H0 = Di suatu populasi yang sama, dua kategorikal variabel tidak berhubungan'),
                    html.H6(children='H1 = Di suatu populasi yang sama, dua kategorikal variabel berhubungan')
                ],    
                    className="mb-4"
            ))
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Hubungan antara Product Line Dengan City'), 
                    html.P(children='Pada tabel dibawah ini:'),
                ])
            )
        ]), 

        dbc.Row([
            dbc.Col(
                DataTable(
                columns=columns,
                data=data,
                style_cell_conditional=[
                    {
                        'if': {'column_id': 'Product_line'},
                        'width': '10px'
                },
            ],
                ) 
            ),
            dbc.Col( 
                dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in dg_pivot.columns],
                data =dg_pivot.to_dict('records'),
                )       
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Observed chi2: ' + str(chisq1)), 
                    html.P(children='P-value: ' + str(pvalue1)),
                    html.P(children='Yang dapat disimpulkan bahwa menerima h0, yaitu hubungan Product Line dengan city tidak berhubungan erat antar values'),
                ],
                className="mb-4"
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Hubungan antara Product Line Dengan Customer Type'), 
                    html.P(children='Pada tabel dibawah ini:'),
                ],
                className="mt-4")
            )
        ]),  


        dbc.Row([
            dbc.Col(
                DataTable(
                columns=columns,
                data=data,
                style_cell_conditional=[
                    {
                        'if': {'column_id': 'Product_line'},
                        'width': '10px'
                },
            ],
                ) 
            ),
            dbc.Col(
                dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in dg_pivot1.columns],
                data =dg_pivot1.to_dict('records'),
                
                )
            )
        ]),

        dbc.Row([
            
            dbc.Col(
                html.Div(children=[
                    html.P(children='Observed chi2: ' + str(chisq2)), 
                    html.P(children='P-value: ' + str(pvalue2)),
                    html.P(children='Yang dapat disimpulkan bahwa menerima h0, yaitu hubungan Product Line dengan Customer Type tidak berhubungan erat antar values'),
                ],
                className="mb-4"
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Hubungan antara Product Line Dengan Gender'), 
                    html.P(children='Pada tabel dibawah ini:'),
                ],
                className="mt-4")
            )
        ]),  

        dbc.Row([
            dbc.Col(
                DataTable(
                columns=columns,
                data=data,
                style_cell_conditional=[
                    {
                        'if': {'column_id': 'Product_line'},
                        'width': '10px'
                },
            ],
                ) 
            ),
            dbc.Col(
                dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in dg_pivot2.columns],
                data =dg_pivot2.to_dict('records'),
                
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Observed chi2: ' + str(chisq3)), 
                    html.P(children='P-value: ' + str(pvalue3)),
                    html.P(children='Yang dapat disimpulkan bahwa menerima h0, yaitu hubungan Product Line dengan Gender tidak berhubungan erat antar values'),
                ],
                className="mb-4"
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Hubungan antara Product Line Dengan Payment'), 
                    html.P(children='Pada tabel dibawah ini:'),
                ],
                className="mt-4")
            )
        ]),  

        dbc.Row([
            dbc.Col(
                DataTable(
                columns=columns,
                data=data,
                style_cell_conditional=[
                    {
                        'if': {'column_id': 'Product_line'},
                        'width': '10px'
                },
            ],
                ) 
            ),
            dbc.Col(
                dash_table.DataTable(
                columns=[{"name": i, "id": i} for i in dg_pivot3.columns],
                data =dg_pivot3.to_dict('records'),
                
                )
            )
        ]),

        dbc.Row([
            dbc.Col(
                html.Div(children=[
                    html.P(children='Observed chi2: ' + str(chisq4)), 
                    html.P(children='P-value: '+ str(pvalue4)),
                    html.P(children='Yang dapat disimpulkan bahwa menerima h0, yaitu hubungan Product Line dengan Payment tidak berhubungan erat antar values'),
                ],
                className="mb-4"
                )
            )
        ]),
        
        
        ])
    ])
 