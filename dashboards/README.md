<style>
    h1 {
        text-align: center;
        font-size: 50px;
        font-weight: bold;
    }

    section {
        text-align: center;
        font-size: 20px;
        margin: 25px;
        border: 2px solid #d5d3d3;
        border-radius: 5px;
        padding: 25px;
        background-color: #860303
    }
    
    h2 {
        font-size: 40px;
        text-align: center;
        font-weight: bold;
    }
    h3 {
        font-size: 30px;
        font-weight: bold;
    }
    p, span, li {
        font-size: 20px;
    }
    span {
        color: #860303;
        background-color: #d5d3d3;
    }
    span ul, span h3 {
        background-color: #d5d3d3
    }
    img {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

</style>
<h1>Dashboards</h1>
<section>This material is part of a course <a href="https://www.udemy.com/course/python-dashboards-plotly-dash/?kw=Python+Data+Visualization%3A+Dashboards+with+Plotly+%26+Dash&src=sac">Python Data Visualization: Dashboards with Plotly & Dash</a>, created by Chris Bruehl, on Udemy. I'm studing with this course, and here I'm puting my anotations about the course. An excelent course. </section>
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

    app = Dash(__name__) -> this is typically assigned to a variable called "app"

    app.layout = html.Div("Hello Dash!") -> Use the HTML module to specify the visual components and assign in to app.layout

    if __name__ == "__main__":
        app.run_server(debug=True)

</p>
<span>Dash is running on http://127.0.0.1:8050/</span>
<h3>Interactive Elements</h3>
<img src="/assets/interactiveElements.png">
<p> These interactive elements are useless until they are processed in the back-end with <strong style="color: yellow;">callback functions</strong></p>
<h2>Example</h2>
<img src="assets/example01.png">
<p>This dcc.Dropdown() component has three properties:</p>
<ol>
    <li> <strong>options</strong>: contains the contents of the dropdown</li>
    <ul>
        <li>This is a list of strings that populate the dropdown menu;</li>
        <li>The option selected by the user gets passed through the value;</li>
        <li>It's possible to have a user facing label that differs from the value processed in the backend.</li>
    </ul>
    <li><strong>id</strong>: The identifier for the value passed through</li>
    <ul>
        <li>This is the unique identifier for the dropdown</li>
    </ul>
    <li><strong>value</strong>: The option selected</li>
    <ul>
        <li>This helps set a default "starting" value if needed;</li>
        <li>This property changes whenever a user selects a new option.</li>
    </ul>
</ol>
<h3>Callback functions</h3>process user input and update the app accordingly
<ul>
    <li>They are triggered by a change to a property of an HTML component (input)</li>
    <li>They then change the property of another HTML component (output)</li>
</ul>
<img src="assets/example02.png">
<p>Callback functions are defined in the <strong>@app.callback</strong> decorator and have at least two arguments (Output & Input), followed by function itself</p>
<p>
    
    @app.callback(
        Output(component_id, component_property),
        Input(component_id, component_property),
    )
    def function_name(variable):
        #function steps
        return f"Output {variable}"

</p>
<span>The Input & Output arguments of the callback decorator. <strong>(Output goes first!)</strong></span><br>
<span>The id of the html component that triggers (input) or gets modified by (output) the callback function</span><br>
<span>The property of the html component that is passed into (input) or gets modified by (output) the callback function</span><br>
<span>
    <ul>
    <strong>Examples:</strong>
        <li><strong>"children"</strong> for text</li>
        <li><strong>"value"</strong> for interactive elements</li>
        <li><strong>"figure"</strong> for charts</li>
    </ul>
</span>
<h2>Example</h2>
<p>

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
        return f"Country selected: {country}"

</p>
<p>Callback functions run as soon as the app launches by default, but you can add logic to <span>prevent updates</span></p>
<ul>
    <li>This can help avoid errors when interactive elements are in an "empty state"</li>
    <img src="assets/example03.png">
</ul>
<h3>Application Run Options</h3>
<p>Ther're several <span>Application Run Options</span> you can use when running the app:</p>
<ul>
    <li><strong>debug=True</strong>: helps with troubleshooting during development (i.e., better error messages</li>
    <li><strong>host/port</strong>: specify the server address of the app - the default is: http://127.0.0.1:8050/</li>
    <li><strong>mode="inline"</strong>: runs the app in-notebook when using JupyterDash (not an option in Dash)</li>
    <li><strong>height/width</strong>: set the height or width of the app in pixels or a percentage</li>
</ul>
<p>

    if __name__ == "__main__":
        app.run_server(debug=True, host="0.0.0.0", port=8051, mode="inline", height=1000, width=80%)

</p>
<span><h3>PRO TIP:</h3> the <strong>host/port</strong> option became more important when deploying your application; and setting <strong>width</strong> as a percentage is a great way to keep your app proportions consistent </span>
<h3>Interactive Plotly Visuals</h3>
<p>You can add <span>interactive Plotly visuals</span> to Dash apps with these 3 steps: </p>
<ol>
    <li>Create a "prototype" visual Pandas & Plotly without interactivity;</li>
    <li>Indetify the element that changes and define its option in the interactive component;</li>
    <li>Connect the interactive component to the visual using a callback function</li>
</ol>
<h2>Example</h2> | Visualizing the different datasets form Anscombe's Quartet
<img src="assets/example04.png">
<p>

    app.layout = html.Div([
        html.H3("Anscombe's Quartet"),
        dcc.Graph(
            id="visual,
            figure=px.scatter(df.loc[df["dataset"] == "I", [x="x", y="y"]],)
        )
    ])

</p>
<span>You can add a Plotly visual to your app eith the <strong>figure</strong> property of the <strong>dcc.Graph</strong> component.</span>
<p><span>Step 1</span> | Create a "prototype" visual Pandas & Plotly without interactivity</p>
<img src="assets/step1.png">
<a href="https://colab.research.google.com/drive/1yp8nlyHPPxBzzS0nE2fqnvbui7v_0PEx?usp=sharing">Google Colab</a>
<p><span>Step 2</span> | Indetify the element that changes and define its option in the interactive component</p>
<img src="assets/step2.png">
<p><span>Step 3</span> | Connect the interactive component to the visual using a callback function</p>
<img src="assets/step3.png">
