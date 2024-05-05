import dash
from dash import html
import dash_bootstrap_components as dbc

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "10rem",
    "padding": "2rem 1rem",
    "background-color": "grey",  
}
NAV_LINK_STYLE = {
    "color": "white",
}

PAGE_ORDER = ["Home"]


def generate_sidebar(pathname):
    sidebar = html.Div(
        [
            html.H2("Menu", style={"color": "white", "textAlign": "center"}),
            html.Hr(style={"border-color": "white"}),
            dbc.Nav(
                [
                    dbc.NavLink(
                        f"{page['name']}",
                        href=page["relative_path"],
                        id=f"{page['name'].lower()}-link",
                        style={
                            **NAV_LINK_STYLE,
                            "font-size": "1.5rem" 
                        },
                        active={
                            'font-weight': 'bold'
                        } if page["name"].lower() == pathname.strip('/') else {},
                        className="nav-link-hover", 
                    )
                    for page_name in PAGE_ORDER
                    for page in dash.page_registry.values() if page["name"] == page_name and 'location' in page and page['location'] == 'sidebar'
                ],
                vertical=True,
                pills=True,
            ),
        ],
        style=SIDEBAR_STYLE,
    )

    return sidebar