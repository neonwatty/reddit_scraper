from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dashboard.data import read_all_rows


def reload_data():
    # read in rows
    rows = read_all_rows()
    
    # create figure
    fig_history = px.line(
            rows,
            x="timestamp",
            y="total_online_count",
            render_mode="markers",
            labels={
                "timestamp": "timestamp",
                "total_online_count": "total_online_count",
            },
            title="reddit total online history",
            hover_data=["reddit_url", "total_member_count", "total_online_count"],
            color=rows["reddit_url"],
    )
    fig_history.update_layout(template="plotly_dark", font=dict(color="yellow"))
    return (
        html.Div([dcc.Graph(figure=fig_history)],
            style={"padding": "20px"},
        ),
    )
    

def reload_page():
    # reload data
    figure = reload_data()
    
    # create page
    history_page = html.Div(
        [
            dbc.Container(
                [
                    dbc.Container(
                            [dbc.Row(figure)],
                            ),
                        ],
                    ),
                ],
                style={"backgroundColor": "black", "minHeight": "100vh"},
            )
    return history_page


