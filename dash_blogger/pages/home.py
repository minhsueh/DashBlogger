import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
    html.H1('Welcome to _______!'),
    html.Div('This is where you can introduce the content of your blog.')
])