from dash import Dash, html, dcc #? Functions to creating the app and adding elements
from dash.dependencies import Input, Output #? Back-end functions for adding interactivity
import plotly.express as px #? Library for adding Plotly visyals
import pandas as pd #? Library for data prep & ETL

app = Dash(__name__)

app.layout = html.Div([
    "Pick a Country",
    dcc.Dropdown(
        options=["USA", "Brazil", "India", "China", "Indonésia"])
])

if __name__ == "__main__":
    app.run_server(debug=True)
    

