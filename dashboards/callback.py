from dash import Dash, html, dcc #? Functions to creating the app and adding elements
from dash.dependencies import Input, Output #? Back-end functions for adding interactivity
import plotly.express as px #? Library for adding Plotly visyals
import pandas as pd #? Library for data prep & ETL

app = Dash(__name__)

app.layout = html.Div([
    "Pick a Country",
    dcc.Dropdown(
        options=["Brazil", "China", "India", "Indonésia", "USA"],
        id="country-input",
        value="Brazil"
    ),
    html.Div(id="country-output"),
])

@app.callback(Output("country-output", "children"), Input("country-input", "value"))
def update_output_div(country):
    return f"I live in: {country}"

if __name__ == "__main__":
    app.run_server(debug=True)
    

