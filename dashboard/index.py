from dash import Dash, html
import dash_bootstrap_components as dbc
from dashboard.page import reload_page
history_page = reload_page()


def refresh_page() -> html.Div:
    # define layout
    layout = html.Div(
        id="main-div",
        style={"color": "#deb522", "fontColor": "yellow", "backgroundColor": "black"},
        children=[history_page],
    )
    return layout


app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "reddit scraper"

app.layout = refresh_page
