import pandas as pd
from dash import html, dcc
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State

import pandas as pd
from utils import calculate_ranking, count_unique_votes
from app import app

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1("Herzlich Willkommen zum OW DNA Berlin Lunch Spots Picker", className="text-center"),
                className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='Da wir ja jeden Mittag 10min diskutieren wo wir zum Lunch gehen, hier mal ein '
                                     'Tool wo jeder seine Präferenzen angeben kann!',
                            className=''),
                    className="mb-2")
        ]),

        dbc.Row([
            dbc.Col(
                html.P(
                    children='Es funktioniert folgendermaßen:'),
                className="mb-1"),
            html.Ol([
                html.Li('Klickt unten auf VOTE!!!'),
                html.Li('Gibt für jedes Restaurant einen Score von 1-10 an'),
                html.Li('Das Restaurant mit dem höchsten durchschnittlichen Score ist der Gewinner!'),
            ])
        ], className="mb-3"),
        dbc.Row([
            dbc.Col(
                html.P(
                    children='Wenn ihr eure Praeferenzen updaten wollt, stimmt nochmal unter dem gleichen Namen ab!'),
                className="mb-1"),
        ], className="mb-3"),

        dbc.Row([
            dbc.Col(
                dbc.Card(children=[
                    html.H3(children='Für Lunch Spots abstimmen',
                            className="text-center"),
                    dbc.Button("VOTE!!!",
                               href="/restaurantvote",
                               class_name="mt-3 d-grid col-6 mx-auto")
                ],
                    body=True, color="dark", outline=True)
                , width={"size": 4, "offset": 4}, className="mb-4"),
        ], className="mb-5"),
        dbc.Row([
            dbc.Col(),
        ], className="mb-3"),
        dbc.Row([
            dbc.Col(
                html.H4({}, id='html-votes')
            ),
        ], className="mb-2"),
        dbc.Row([
            dbc.Col(
                html.Div({}, id='table-ranking')
            ),
        ], className="mb-5"),

    ])
])


@app.callback(
    Output('table-ranking', "children"),
    Output('html-votes', "children"),
    [Input('url', 'pathname')])

def display_page(pathname):
    df = pd.read_csv('./data/restaurant_votes.csv')
    lunch_ranking = calculate_ranking(df)
    unique_votes = count_unique_votes(df)

    return  dbc.Table.from_dataframe(lunch_ranking, striped=True, bordered=True, hover=True), \
      'Current Ranking ({} Vote(s)):'.format(unique_votes)


