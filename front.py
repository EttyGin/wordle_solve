import dash
from dash import Input, Output, State, html, dcc
import dash_bootstrap_components as dbc

from wordle import find_matching_words

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Card(
                                    [
                                        dbc.CardBody(
                                            [
                                                dbc.Label("Enter pattern"),
                                                dbc.Input(
                                                    id="pattern",
                                                    type="text",
                                                    placeholder="like: p..n.",
                                                    style={"width": "100%"},
                                                ),
                                                dbc.Label("Enter includes"),
                                                dbc.Input(
                                                    id="include",
                                                    type="text",
                                                    placeholder="like: au",
                                                ),
                                                dbc.Label("Enter excludes"),
                                                dbc.Input(
                                                    id="exclude",
                                                    type="text",
                                                    placeholder="like: xz",
                                                ),
                                                dbc.Button(
                                                    "Get Options!",
                                                    id="get",
                                                    color="primary",
                                                    className="mt-3",
                                                    style={
                                                        "display": "block",
                                                        "width": "100%",
                                                    },
                                                ),
                                                dbc.Label(
                                                    id="error_msg",
                                                ),
                                            ]
                                        )
                                    ],
                                    style={
                                        "border": "1px solid #ccc",
                                        "border-radius": "5px",
                                        "padding": "20px",
                                        "text-align": "center",
                                        "align-items": "center",
                                        "flex-direction": "center",
                                    },
                                )
                            ],
                            width=12,
                        )
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H3("Your Options Are:", className="text-center"),
                                dcc.Loading(
                                    id="loading-1",
                                    children=[
                                        html.Div(
                                            id="output-container",
                                            style={
                                                "flex-direction": "center",
                                                "align-items": "center",
                                                "min-height": "100vh",
                                                "text-align": "center",
                                                "white-space": "pre-wrap",
                                                "word-wrap": "break-word",
                                            },
                                        )
                                    ],
                                    type="circle",
                                ),
                            ],
                            width=12,
                        )
                    ]
                ),
            ],
            fluid=True,
            style={"height": "100vh", "backgroundColor": "#f0f0f0"},
        )
    ]
)


@app.callback(
    Output("output-container", "children"),
    Output("error_msg", "children"),
    [Input("get", "n_clicks")],
    [State("pattern", "value"), State("include", "value"), State("exclude", "value")],
    prevent_initial_calls=True,
)
def update_output(n_clicks, pattern: str, include: str, exclude: str):
    if n_clicks is None:
        return "", ""
    if pattern is None:
        return "", "You have to provide a pattern!"
    print(f"{pattern}\n{include}\n{exclude}")

    words: str = find_matching_words(pattern, include, exclude)

    return words, ""


if __name__ == "__main__":
    app.run_server(debug=True)
