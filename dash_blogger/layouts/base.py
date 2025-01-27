from dash import html, dcc, page_container
from dash_blogger.layouts.sidebar import sidebar

layout = html.Div(
    [
        # Sidebar
        sidebar,
        
        # Main content area
        html.Div(
            children=[
                page_container,  # This will render the content of each page
            ],
            style={
                "marginLeft": "200px",  # Adjust margin to make room for the sidebar
                "padding": "20px",
            },
        )
    ]
)
