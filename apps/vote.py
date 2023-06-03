import pandas as pd
from dash import dcc, html, ALL
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate


from app import app

restaurants = [
    "Beets&Roots",
    "Chupenga",
    "Flamingo",
    "Green Rabbit",
    "Hoa Rong",
    "Ishin",
    "Italiener",
    "Mishba",
]



layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col([html.H2(children='Lunch Spot Vote', className='')]
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(
                html.Div([
                    html.P("Name:"),
                    dcc.Input(id="input-name", type="text", placeholder="Max Mustermann", style={'marginRight': '10px'}),
                ]), className="mb-5")
        ]),
        html.Div([
            dbc.Row([
                dbc.Col(
                    [
                        html.P(
                            children=restaurants[i],
                            className=''
                        )
                    ], className="mb-5", width={"size": 3}),
                dbc.Col(
                    [
                        dcc.Slider(id={'role': 'slider', 'index': i},
                                   min=1, max=10, step=1, value=5)
                    ], className="mb-5")
            ]) for i in range(len(restaurants))
        ])
    ]),

    dbc.Row([
        dbc.Col(
            dbc.Button("Abstimmen",
                       id="btn-vote",
                       href="/home",
                       disabled={},
                       class_name="mt-3 d-grid col-6 mx-auto"),
            width={"size": 4, "offset": 4}, className="mb-4"
        )
    ]),

    html.Div(
        children={},
        id='div-1'
    )
])




@app.callback(
    Output('div-1', "children"),
    Input("btn-vote", "n_clicks"),
    State('input-name', 'value'),
    [State({'role': 'slider', 'index': ALL}, 'value')]
)
def save_votes(n_clicks, name, scores):
    if n_clicks is None:
        raise PreventUpdate

    # Update preferences Add logic to update csv, if name already in csv
    df = pd.read_csv('./data/restaurant_votes.csv')

    if df['name'].str.contains(name).any():
        for i, value in enumerate(restaurants):
            df.loc[(df['name'] == name) & (df['restaurant'] == value), 'score'] = scores[i]
    else:
        for i, value in enumerate(restaurants):
            df.loc[len(df.index)] = [name, value, scores[i]]

    # save dataframe
    print('saving')
    df.to_csv('./data/restaurant_votes.csv', index=False)
    print(df.tail())

    return ""


@app.callback(
    Output("btn-vote", "disabled"),
    Input('input-name', 'value')
)
def disable_votes(name):
    if name == "" or name.isspace():
        return True
    else:
        return False



