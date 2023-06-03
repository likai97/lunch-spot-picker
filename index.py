from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

import pandas as pd
from utils import calculate_ranking, count_unique_votes

from app import server
from app import app

from apps import home, vote, reset_dataframe

navbar = dbc.Navbar(
    dbc.Container([
        dbc.Col(width=8),
        dbc.Row([
            dbc.Col([
                html.A(
                    dbc.Col(html.Img(src="/assets/reset-alt.svg", height="30px")),
                    href="/reset_dataframe"
                )
            ]),
            dbc.Col([
                html.A(
                    dbc.Col(html.Img(src="/assets/github.png", height="30px")),
                    href="https://github.com/likai97",
                    target="_blank"
                )
            ]),
            dbc.Col([
                html.A(
                    dbc.Col(html.Img(src="/assets/home.png", height="30px")),
                    href="/home",
                )
            ]),

        ])
    ]),
    color='primary'
)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/restaurantvote':
        return vote.layout
    elif pathname == '/reset_dataframe':
        return reset_dataframe.layout
    else:
        return home.layout


if __name__ == '__main__':
    app.run_server(debug=False)
