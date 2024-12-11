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
                                dbc.Label(
                                    "Enter pattern",
                                    style={"margin": "20px 0px 10px 20px"},
                                ),
                                dbc.Input(
                                    id="pattern",
                                    type="text",
                                    placeholder="like: p..n.",
                                    style={
                                        "width": "90%",
                                        "margin": "0px 0px 0px 20px",
                                    },
                                ),
                            ],
                            width=4,
                        ),
                        dbc.Col(
                            [
                                dbc.Label(
                                    "Enter includes",
                                    style={"margin": "20px 20px 10px 20px"},
                                ),
                                dbc.Input(
                                    id="include",
                                    type="text",
                                    placeholder="like: au",
                                    style={"width": "90%"},
                                ),
                            ],
                            width=4,
                        ),
                        dbc.Col(
                            [
                                dbc.Label(
                                    "Enter excludes",
                                    style={"margin": "20px 20px 10px 0px"},
                                ),
                                dbc.Input(
                                    id="exclude",
                                    type="text",
                                    placeholder="like: xz",
                                    style={"width": "90%"},
                                ),
                            ],
                            width=4,
                        ),
                    ],
                    style={"margin": "20px 0px 20px 0px"},
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dbc.Button(
                                    "Get Options!",
                                    id="get",
                                    color="primary",
                                    className="mt-3",
                                    style={
                                        "width": "98%",
                                        "margin": "20px 0px 10px 22px",
                                    },
                                ),
                            ],
                            width=12,
                            style={
                                "margin": "0 20px 0 0",
                                "display": "center",
                                "text-align": "center",
                                "align-items": "center",
                                "max-width": "96.5%",
                                "flex-direction": "center",
                            },
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                dcc.ConfirmDialog(
                                    id="error_msg",
                                    message="You have to provide a pattern!",
                                ),
                                html.Hr(
                                    style={
                                        "margin": "50px 0px 20px 22px",
                                        "width": "98%",
                                    }
                                ),
                                dcc.Loading(
                                    id="loading-1",
                                    children=[
                                        html.Div(
                                            id="output-container",
                                            style={
                                                "margin": "20px 100px 20px 22px",
                                                "word-wrap": "break-word",
                                                "white-space": "pre-wrap",
                                                "display": "center",
                                                "text-align": "center",
                                            },
                                        )
                                    ],
                                    type="circle",
                                    overlay_style={
                                        "visibility": "visible",
                                        "filter": "blur(2px)",
                                    },
                                ),
                            ],
                            width=12,
                        )
                    ]
                ),
            ],
            fluid=True,
            style={
                "min-height": "100vh",
                "backgroundColor": "#f0f0f0",
                "margin": "-20px 20px 0px 0px",
            },
        )
    ]
)


@app.callback(
    Output("output-container", "children"),
    # Output("error_msg", "children"),
    Output("error_msg", "displayed"),
    [Input("get", "n_clicks")],
    [State("pattern", "value"), State("include", "value"), State("exclude", "value")],
    prevent_initial_calls=True,
)
def update_output(n_clicks, pattern: str, include: str, exclude: str):
    if n_clicks is None:
        return "", False
    if pattern is None:
        # dmc.Notification(message="You have to provide a pattern!", title="שגיאה")

        return "", True  # "You have to provide a pattern!"
    print(f"{pattern}\n{include}\n{exclude}")

    words: str = find_matching_words(pattern, include, exclude)

    return words, False


if __name__ == "__main__":
    app.run_server(debug=True, host="0.0.0.0")

