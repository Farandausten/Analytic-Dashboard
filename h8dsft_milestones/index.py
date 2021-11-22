from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
#from dash_html_components.Div import Div
import dash_bootstrap_components as dbc

from miles import h8dsft_mls, h8dsft_test, home, h8dsft_anova, h8dsft_total

from app import app
from app import server

app.layout = html.Div([
    dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Grafik Laju", href = '/miles/h8dsft_mls')),
            dbc.NavItem(dbc.NavLink("Grafik Total", href = '/miles/h8dsft_total')),
            dbc.NavItem(dbc.NavLink("CHI Square Testing", href = '/miles/h8dsft_test')),
            dbc.NavItem(dbc.NavLink("Anova Testing", href = '/miles/h8dsft_anova')),
        ],
        
        
        brand = "Full Bootcamp Data Science",
        brand_href ="/miles/home",
        color= "blue",
        dark = True,
        sticky = 'top'
    ),
    
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[])
])

@app.callback(
    Output(component_id='page-content', component_property='children'),
    [
        Input(component_id='url', component_property='pathname')
])
def display_page(pathname):
    if pathname == '/miles/h8dsft_mls':
        return h8dsft_mls.layout
    elif pathname == '/miles/h8dsft_test':
        return h8dsft_test.layout
    elif pathname == '/miles/h8dsft_anova':
        return h8dsft_anova.layout
    elif pathname == '/miles/h8dsft_total':
        return h8dsft_total.layout            
    else:
        return home.layout

if __name__ == '__main__':
    app.run_server(debug=True)                
