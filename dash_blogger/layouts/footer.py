from dash import html

footer = html.Div(
    [
        html.Span("© 2025 "),
        html.A(
            "DashBlogger",
            href="https://github.com/minhsueh/DashBlogger",  # Replace with your GitHub URL
            target="_blank",
            style={"color": "lightblue", "textDecoration": "none"},
        ),
    ],
    style={
        "position": "absolute",
        "bottom": "10px",
        "width": "100%",
        "color": "white",
        "fontSize": "12px",
        "textAlign": "left",
    },
)
