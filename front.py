import dash
from dash import Input, Output, State, html
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
                                                    type="התבנית שלך",
                                                    placeholder="like: xz",
                                                ),
                                                dbc.Button(
                                                    "Get Options!",
                                                    id="get",
                                                    style={
                                                        "margin": "auto",
                                                        "padding": "20px",
                                                        "display": "block",  # מוסיף display: block עבור מיקום מדויק יותר
                                                        "width": "100%",
                                                    },  # מרכז את הכפתור
                                                ),
                                            ]
                                        ),
                                    ],
                                    style={"display": "block"},
                                ),
                            ],
                            style={
                                "flex-direction": "center",
                                "align-items": "center",
                                "min-height": "100vh",
                                
                                "padding": "50px",
                                "background-color": "#D9E7FF",
                            },
                        ),  # קבע את רוחב העמודה של הטופס ל-6 מתוך 12
                        dbc.Col(
                            [
                                html.H3(
                                    "Your Options Are:",
                                    style={
                                        "padding": "50px",
                                        "text-align": "center",
                                        "background-color": "#99FFDD",
                                    },
                                ),
                                html.Div(
                                    id="output-container",
                                    style={
                                        "flex-direction": "center",
                                        "align-items": "center",
                                        "min-height": "100vh",
                                        "text-align": "center",
                                        "background-color": "#99FFDD",
                                    },
                                ),
                            ],
                        ),
                    ]
                )
            ]
        )
    ]
)


@app.callback(
    Output("output-container", "children"),
    [Input("get", "n_clicks")],
    [State("pattern", "value"), State("include", "value"), State("exclude", "value")],
    prevent_initial_calls=True,
)
def update_output(n_clicks, pattern: str, include: str, exclude: str):
    if n_clicks is None:
        return ""

    print(f"{pattern}\n{include}\n{exclude}")
    words: str = find_matching_words(pattern, include, exclude)

    return words


if __name__ == "__main__":
    app.run_server(debug=True)
