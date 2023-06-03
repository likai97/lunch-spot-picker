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
                dbc.Card(children=[
                    dcc.Input(id='password-input', type='password', placeholder='Enter password'),
                    dbc.Button("Reset!",
                               id="btn-reset",
                               href="/home",
                               disabled={},
                               class_name="mt-3 d-grid col-6 mx-auto")
                ], body=True, color="dark", outline=True),
                width={"size": 4, "offset": 4}, className="mb-4 mt-5"
            )
        ]),
        html.Div({}, id="dummy")
    ])
])

@app.callback(
    Output("btn-reset", "disabled"),
    Input('password-input', 'value')
)
def disable_reset(password):
    if password == "qwer":
        return False
    else:
        return True


@app.callback(
    Output("dummy", "children"),
    Input('btn-reset', 'n_clicks')
)
def reset_df(n_clicks):
    df = pd.DataFrame(columns=['name', 'restaurant', 'score'])
    df.to_csv('./data/restaurant_votes.csv', index=False)
    return ""
