import dash_html_components as html
import dash_bootstrap_components as dbc
 
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Welcome to the Hacktiv8 Full Bootcamp Data Science",
                className="text-center"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.H5(children='My name is Farand Austen Mahesa! This is my multiple page dash dashboard!'),
                className="mb-4")
        ]),
 
        dbc.Row([
            dbc.Col(
                html.H5(children='It consists of four main pages: Supermarket Sales, which gives an overview of the SUPERMARKET SALES cashflow Total, taxes and cogs, '
                'and, you get the original dataset and visit my Github page from here'),
                className="mb-5")
        ]),
 
        dbc.Row([
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Get the original dataset here',
                        className="text-center"),
                        dbc.Button("Supermarket Sales",
                        href="https://www.kaggle.com/aungpyaeap/supermarket-sales?select=supermarket_sales+-+Sheet1.csv",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),
 
            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Visit my Github Page',
                        className="text-center"),
                        dbc.Button("GitHub",
                        href="https://github.com/Farandausten",
                        color="primary",
                        className="mt-3"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mb-6"
            ),

            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Visit Kode.id',
                        className="text-center"),
                        dbc.Button("Kode.id",
                        href="https://www.kode.id/",
                        color="primary",
                        className="mt-6"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mt-6"
            ),

            dbc.Col(
                dbc.Card(
                    children=[
                        html.H3(children='Visit Heroku.id',
                        className="text-center"),
                        dbc.Button("Heroku.id",
                        href="https://www.heroku.id/",
                        color="primary",
                        className="mt-6"),
                    ],
                    body=True, color="dark", outline=True
                ),
                width=6, className="mt-6"
            ),
        ], className="mt-5"),
    ])
 
])