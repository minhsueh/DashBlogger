# These are the required dependencies and code for DashBlogger. Please do not modify!
import dash
from dash_blogger.layouts.dash_blogger_utils import get_url_path
dash.register_page(__name__, path=get_url_path(__file__))

# Import your required dependencies
from dash import html

# Define your customized layout and callback here.
# Note: The 'layout' object is required for the Dash application.
layout = html.Div(
    [
        html.H1('This is an example of a single-page setup.'),
    ]
)