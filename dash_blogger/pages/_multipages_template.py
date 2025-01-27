# These are the required dependencies and code for DashBlogger. Please do not modify!
import dash
from dash_blogger.layouts.dash_blogger_utils import get_url_path
dash.register_page(__name__, path=get_url_path(__file__))


# If you want DashBlogger to automatically create pages that layout all pages in the /pages/topic1/ directory, 
# use the following portion of code.
from dash import html
from dash_blogger.layouts.dash_blogger_utils import generate_content_links, get_page_path

layout = html.Div(
    [
        html.H1('This is an example of a multi-page setup.')
    ] + 
    generate_content_links(get_page_path(__file__), "black")
)


# Otherwise, you can comment out the above code portion, and import or create your own 'layout' object here.
