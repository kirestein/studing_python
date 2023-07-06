<style>
    h1 {
        text-align: center;
        font-size: 50px;
    }

    h2 {
        font-size: 40px;
    }
    h3 {
        font-size: 30px;
    }
    p, span, li {
        font-size: 20px;
    }
    span {
        color: #860303;
        background-color: #d5d3d3;
    }

</style>
<h1>Dashboards</h1>
<h3>Install plotly and dash via conda</h3>
<p>!conda install --yes --prefix {sys.prefix} plotly!</p>
<p>!conda install --yes --prefix {sys.prefix} dash</p>
<h3>Install plotly and dash via terminal</h3>
<p>!pipx install plotly dash</p>
<span><strong>OBS</strong>: It's recommended to update your pip version</span>
<br>
<h3>You can <strong>create a dash application</strong> by following these steps:</h3>
<ol>
    <li>Install the necessary libraries</li>
    <ul>
        <li>dash</li>
        <li>plotly</li>
    </ul>
    <li>Import the necessary libraries</li>
    <li>Create the Dash app</li>
    <ul>
        <li>app = Dash(__name__)</li>
    </ul>
    <li>Set up the HTML layout (This is the front end of the web app)</li>
    <ul>
        <li>app.layout = html.Div([...])</li>
    </ul>
    <li>Add the callback functions (This is the back end of the web app)</li>
    <ul>
        <li>@app.callback(Output(), Input()) <!--* Ties dropdown to chart --><br>
            def interactive_chart(input): <!--* Create a function accepts dropdown value as argument --><br>
            ____   return output <!--* Usually a Plotly chart --></li><br>
    </ul>
    <li>Run the app</li>
    <ul>
        <li>app.run_server(debug=True)</li>
    </ul>
</ol>
<h3>Hello Dash</h3>
<p>
    from dash import Dash, html

    app = Dash(__name__)

    app.layout = html.Div("Hello!")

    if __name__ == "__main__":
        app.run_server(debug=True)
</p>
<span>Dash is running on http://127.0.0.1:8050/</span>