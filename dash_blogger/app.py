from dash import Dash
from dash_blogger.layouts.base import layout

# Initialize the Dash app
app = Dash(
    __name__,
    use_pages=True,  # Enables multi-page support
    suppress_callback_exceptions=True,  # Suppresses callback exceptions for pages
    title="DashBlogger",  # Sets the title of the app
    update_title="Loading...",  # Title displayed during page load
)

# Set the layout for the app
app.layout = layout

# Run the server
if __name__ == "__main__":
    # app.run_server(debug=True) # local
    app.run_server(host='0.0.0.0', port=8050) # expose to public
