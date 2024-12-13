import dash
from dash import Input, Output, html
import dash_core_components as dcc

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Button('הצג הודעת שגיאה', id='show-error'),
    dcc.ConfirmDialog(
        id='confirm',
        message='התרחשה שגיאה!',
        displayed=False
    )
])

@app.callback(
    Output('confirm', 'displayed'),
    [Input('show-error', 'n_clicks')]
)
def display_confirm(n_clicks):
    if n_clicks:
        return True
    return False

if __name__ == '__main__':
    app.run_server(debug=True)