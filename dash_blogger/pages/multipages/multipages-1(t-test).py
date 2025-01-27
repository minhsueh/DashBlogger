# These are the required dependencies and code for DashBlogger. Please do not modify!
import dash
from dash_blogger.layouts.dash_blogger_utils import get_url_path
dash.register_page(__name__, path=get_url_path(__file__))


# Import your required dependencies
from dash import html, dcc, Input, Output, callback
import numpy as np
import plotly.express as px


# Define your customized layout and callback here.
# Note: The 'layout' object is required for the Dash application.
layout = html.Div([
    html.H2("T-Test Example", style={'text-align': 'center'}),
    html.Label("Population Mean:"),
    dcc.Input(id='t-test-pop-mean', type='number', value=5, step=0.1, style={"width": "40px"}),
    html.Label(" "),
    html.Label("Sample Mean:"),
    dcc.Input(id='t-test-mean', type='number', value=5, step=0.1, style={"width": "40px"}),
    html.Label(" "),
    html.Label("Sample Standard Deviation:"),
    dcc.Input(id='t-test-std', type='number', value=1, step=0.1, style={"width": "40px"}),
    html.Label(" "),
    html.Label("Sample Size:"),
    dcc.Input(id='t-test-size', type='number', value=30, step=1, style={"width": "40px"}),
    html.Div(id='t-test-result', style={'margin-top': '20px'}),
    dcc.Graph(id='t-test-plot', style={'margin-top': '20px'})
])

@callback(
    [Output('t-test-result', 'children'),
     Output('t-test-plot', 'figure')],
    [Input('t-test-mean', 'value'),
     Input('t-test-pop-mean', 'value'),
     Input('t-test-std', 'value'),
     Input('t-test-size', 'value')]
)
def perform_t_test(sample_mean, pop_mean, sample_std, sample_size):
   
    # Perform T-Test calculation
    t_statistic = (sample_mean - pop_mean) / (sample_std / np.sqrt(sample_size))
    critical_value = 1.96  # Assuming alpha = 0.05, two-tailed

    result = "Reject Null Hypothesis" if abs(t_statistic) > critical_value else "Fail to Reject Null Hypothesis"
    
    # Plot data
    x = np.linspace(pop_mean - 4*sample_std, pop_mean + 4*sample_std, 100)
    y = (1 / (np.sqrt(2 * np.pi) * sample_std)) * np.exp(-0.5 * ((x - pop_mean) / sample_std)**2)
    fig = px.line(x=x, y=y, title="T-Test Distribution")
    fig.add_vline(x=pop_mean + critical_value, line_dash="dash", line_color="red", annotation_text="Critical Region")
    fig.add_vline(x=pop_mean - critical_value, line_dash="dash", line_color="red", annotation_text="Critical Region")

    return result, fig
