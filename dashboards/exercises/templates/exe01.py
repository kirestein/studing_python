from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

"""
    SIMPLE DASH APP
    Create a dash app with the following front-end components
    1. A text title "Select a State to Analyze."
    2. A dropdown menu with the following options: "São Paulo", "Rio de Janeiro", "Distrito Federal", "Bahia", "Paraná", "Rio Grande do Sul", "Minas Gerais", "Espirito Santo", "Rio Grande do Norte", "Goiás", "Mato Grosso" 
    3. Text "State Selected: X" where X is the selected state in the dropdown menu.
    
    You'll need to build a callback function that takes the sekected state and return output text based on the value selected in the dropdown menu.
"""

states = ["São Paulo", "Rio de Janeiro", "Distrito Federal", "Bahia", "Paraná", "Rio Grande do Sul", "Minas Gerais", "Espirito Santo", "Rio Grande do Norte", "Goiás", "Mato Grosso"]

app = Dash(__name__)

app.layout = html.Div([
    "Select a State to Analyze.",
    dcc.Dropdown(
        # options = ["São Paulo", "Rio de Janeiro", "Distrito Federal", "Bahia", "Paraná", "Rio Grande do Sul", "Minas Gerais", "Espirito Santo", "Rio Grande do Norte", "Goiás", "Mato Grosso"],
        options = [state for state in states],
        id = "state-input",
    ),
    html.Div(id = "state-output"),
])

@app.callback(
    Output("state-output", "children"), 
    Input("state-input", "value")
)
def selected_state(value):
    if value:
        return f"State Selected: {value}"

if __name__ == "__main__":
    app.run_server(debug=True, port=8080)