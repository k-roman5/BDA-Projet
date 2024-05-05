import dash
from dash import html
import dash_bootstrap_components as dbc
from pages.sidebar import generate_sidebar

external_stylesheets = [
    dbc.themes.BOOTSTRAP,
]

app = dash.Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True, assets_folder='assets_folder')

app.layout = html.Div(style={'backgroundColor': 'white', 'min-height': '100vh'}, children=[
])

if __name__ == '__main__':
    app.run_server(debug=True)