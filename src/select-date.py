import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.DatePickerRange(
        id='date-picker-range',
        start_date='2024-01-01',
        end_date='2024-12-31'
    ),
    html.Div(id='output-range')
])

@app.callback(
    Output('output-range', 'children'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date')
)
def update_output(start_date, end_date):
    return f'Selected Range: {start_date} to {end_date}'

if __name__ == '__main__':
    app.run_server(debug=True)
