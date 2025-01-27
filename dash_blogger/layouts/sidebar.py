from dash import html, dcc
from dash_blogger.layouts.footer import footer
from dash_blogger.layouts.dash_blogger_utils import generate_sidebar_links
from pathlib import Path

page_path = Path(__file__).parent.parent / 'pages'

home_page = [
    dcc.Link(
        'Home',  
        href=f"/", 
        style={
            "color": "white",
            "text-decoration": "none",
            "fontSize": "18px"
        }
    ),
    html.Br(),
]

sidebar = html.Div(
    children= home_page + generate_sidebar_links(page_path, "white") + [footer],
    style={
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "100px",
        "backgroundColor": "#333",
        "padding": "20px",
        "color": "white",
        "text-align": "left",
    },
)
