import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from utils import get_dates, get_state_data, get_city_data, get_given_city_data, \
    get_given_state_data, get_state_data_latest


cases_types = ['Active', 'Confirmed', 'Recovered', 'Deceased', 'Tested']
plot_types = ['plot', 'bar', 'histogram', 'area', 'funnel', 'scatter']
bootstrap = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/solar/bootstrap.min.css"
app = dash.Dash(__name__, external_stylesheets=[bootstrap])
server = app.server
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
city_df = get_city_data()[0]
state_df = get_state_data()[0]
state_df_latest = get_state_data_latest()
app.layout = html.Div([
    html.H1(children='COVID-19 Analysis Project', style={'text-align': 'center'}),
    html.Div(children='''
        This is a COVID-19 analysis project made on Python Dash framework using data analysis libraries like pandas,plotly and APIs.
        It is made for educational purposes only and we have used https://api.covid19india.org to get the dataset for analysis.
    ''', style={'text-align': 'center'}),
    html.Br(),
    html.Div(
        [
            dcc.Dropdown(
                id="sta1",
                options=[{
                    'label': i,
                    'value': i
                } for i in get_state_data()[1]],
                value='Uttar Pradesh'),
        ],
        style={'width': '25%',
               'display': 'inline-block'},
    ),
    html.Div(
        [
            dcc.Dropdown(
                id="input2",
                options=[{
                    'label': i,
                    'value': i
                } for i in plot_types],
                value='plot'
            ),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='graph-with-slider'),
    html.H4(children='A comparison of cases between any two states.', style={'text-align': 'center'}),
    html.Div(
        [
            dcc.Dropdown(
                id="input3",
                options=[{
                    'label': i,
                    'value': i
                } for i in get_state_data()[1]],
                value='Uttar Pradesh'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    html.Div(
        [
            dcc.Dropdown(
                id="input4",
                options=[{
                    'label': i,
                    'value': i
                } for i in get_state_data()[1]],
                value='Bihar'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    html.Div(
        [
            dcc.Dropdown(
                id="input5",
                options=[{
                    'label': i,
                    'value': i
                } for i in cases_types],
                value='Active'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    html.Div(
        [
            dcc.Dropdown(
                id="input21",
                options=[{
                    'label': i,
                    'value': i
                } for i in plot_types],
                value='plot'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    html.Br(),
    html.Br(),
    dcc.Graph(id='graph2'),
    html.H4(children='A comparison of cases between any two cities.', style={'text-align': 'center'}),
    html.Div(
        [
            dcc.Dropdown(
                id="input6",
                options=[{
                    'label': i,
                    'value': i
                } for i in get_city_data()[1]],
                value='Lucknow'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    html.Div(
        [
            dcc.Dropdown(
                id="input7",
                options=[{
                    'label': i,
                    'value': i
                } for i in get_city_data()[1]],
                value='Ghaziabad'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    html.Div(
        [
            dcc.Dropdown(
                id="input8",
                options=[{
                    'label': i,
                    'value': i
                } for i in cases_types],
                value='Active'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    html.Div(
        [
            dcc.Dropdown(
                id="input31",
                options=[{
                    'label': i,
                    'value': i
                } for i in plot_types],
                value='plot'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    html.Br(),
    html.Br(),
    dcc.Graph(id='graph3', style={"color": "#FFF"}),
    html.Br(),
    html.Br(),
    html.H4(children='Map Of India on the casis of Category of Covid -19 Cases.', style={'text-align': 'center'}),
    html.Div(
        [
            dcc.Dropdown(
                id="input9",
                options=[{
                    'label': i,
                    'value': i
                } for i in cases_types],
                value='Active'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),

    html.Br(),
    html.Br(),
    dcc.Graph(id='graph4')
])


@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('sta1', 'value'),
     Input('input2', 'value')])
def update_figure(sta1, input2):
    fig = None
    state = get_given_state_data(state_df, sta1)
    if input2 == 'plot':
        fig = px.line(state, x=get_dates(state_df), y=['Confirmed', 'Active', 'Recovered', 'Deceased'],
                      title="Covid-19 data of state.",
                      labels={
                "x": "Time",
                "value": "Number of Cases"}, template="presentation")

    if input2 == 'bar':
        fig = px.bar(state, x=get_dates(state_df), y=['Confirmed', 'Active', 'Recovered', 'Deceased'],
                     title="Covid-19 data of state.",
                     labels={
                        "x": "Time",
                        "value": "Number of Cases"},
                     template="presentation")
    if input2 == 'area':
        fig = px.area(state, x=get_dates(state_df), y=['Confirmed', 'Active', 'Recovered', 'Deceased'],
                      title="Covid-19 data of state.",
                      labels={
                "x": "Time",
                "value": "Number of Cases"}, template="presentation")
    if input2 == 'histogram':
        fig = px.histogram(state, x=get_dates(state_df), y=['Confirmed', 'Active', 'Recovered', 'Deceased'],
                     title="Covid-19 data of state.",
                     labels={
                        "x": "Time",
                        "value": "Number of Cases"},
                     template="presentation")
    if input2 == 'funnel':
        fig = px.funnel(state, x=get_dates(state_df), y=['Confirmed', 'Active', 'Recovered', 'Deceased'],
                      title="Covid-19 data of state.",
                      labels={
                "x": "Time",
                "value": "Number of Cases"}, template="presentation")
    if input2 == 'scatter':
        fig = px.scatter(state, x=get_dates(state_df), y=['Confirmed', 'Active', 'Recovered', 'Deceased'],
                      title="Covid-19 data of state.",
                      labels={
                "x": "Time",
                "value": "Number of Cases"}, template="presentation")
    fig.update_layout(
        font_family="Courier New",
        font_color="blue",
        title_font_family="Times New Roman",
        title_font_color="red",
        legend_title_font_color="green",
        transition_duration=500
    )
    return fig


@app.callback(
    Output('graph2', 'figure'),
    [Input('input3', 'value'),
     Input('input4', 'value'),
     Input('input5', 'value'),
     Input('input21','value')])
def update2(input3, input4, input5, input21):
    state1 = get_given_state_data(state_df, input3)
    state2 = get_given_state_data(state_df, input4)
    dfresult = state1
    dfresult[input3] = state1[input5]
    dfresult[input4] = state2[input5]
    fig = None
    if input21 == "plot":
        fig = px.line(dfresult, x=get_dates(state_df), y=[input3, input4],
                     title="Covid-19 : Cases comparison between %s and %s . " % (input3, input4),
                     labels={
                         "x": "Time",
                         "value": "Number of Cases"},
                     template="presentation"
                     )
    if input21 == "bar":
        fig = px.bar(dfresult, x=get_dates(state_df), y=[input3, input4],
                     title="Covid-19 : Cases comparison between %s and %s . " % (input3, input4),
                     labels={
                         "x": "Time",
                         "value": "Number of Cases"},
                     template="presentation"
                     )
    if input21 == "histogram":
        fig = px.histogram(dfresult, x=get_dates(state_df), y=[input3, input4],
                     title="Covid-19 : Cases comparison between %s and %s . " % (input3, input4),
                     labels={
                         "x": "Time",
                         "value": "Number of Cases"},
                     template="presentation"
                     )
    if input21 == "area":
        fig = px.area(dfresult, x=get_dates(state_df), y=[input3, input4],
                     title="Covid-19 : Cases comparison between %s and %s . " % (input3, input4),
                     labels={
                         "x": "Time",
                         "value": "Number of Cases"},
                     template="presentation"
                     )
    if input21 == "funnel":
        fig = px.funnel(dfresult, x=get_dates(state_df), y=[input3, input4],
                     title="Covid-19 : Cases comparison between %s and %s . " % (input3, input4),
                     labels={
                         "x": "Time",
                         "value": "Number of Cases"},
                     template="presentation"
                     )
    if input21 == "scatter":
        fig = px.scatter(dfresult, x=get_dates(state_df), y=[input3, input4],
                     title="Covid-19 : Cases comparison between %s and %s . " % (input3, input4),
                     labels={
                         "x": "Time",
                         "value": "Number of Cases"},
                     template="presentation"
                     )

    fig.update_layout(
        font_family="Courier New",
        font_color="blue",
        title_font_family="Times New Roman",
        title_font_color="red",
        legend_title_font_color="green",
        transition_duration=500
    )
    return fig


@app.callback(
    Output('graph3', 'figure'),
    [Input('input6', 'value'),
     Input('input7', 'value'),
     Input('input8', 'value'),
     Input('input31', 'value')])
def update3(input6, input7, input8, input31):
    city1 = get_given_city_data(city_df, input6)
    city2 = get_given_city_data(city_df, input7)
    dfresult = city1
    dfresult[input6] = city1[input8]
    dfresult[input7] = city2[input8]
    fig = None
    if input31 == 'plot':
        fig = px.line(dfresult, x=get_dates(city_df), y=[input6, input7],
                      title="Covid-19 : Cases comparison between %s and %s . " % (input6, input7),
                      labels={
                          "x": "Time",
                          "value": "Number of Cases"}, template="presentation")
    if input31 == 'bar':
        fig = px.bar(dfresult, x=get_dates(city_df), y=[input6, input7],
                      title="Covid-19 : Cases comparison between %s and %s . " % (input6, input7),
                      labels={
                          "x": "Time",
                          "value": "Number of Cases"}, template="presentation")
    if input31 == 'histogram':
        fig = px.histogram(dfresult, x=get_dates(city_df), y=[input6, input7],
                      title="Covid-19 : Cases comparison between %s and %s . " % (input6, input7),
                      labels={
                          "x": "Time",
                          "value": "Number of Cases"}, template="presentation")
    if input31 == 'area':
        fig = px.area(dfresult, x=get_dates(city_df), y=[input6, input7],
                      title="Covid-19 : Cases comparison between %s and %s . " % (input6, input7),
                      labels={
                          "x": "Time",
                          "value": "Number of Cases"}, template="presentation")
    if input31 == 'funnel':
        fig = px.funnel(dfresult, x=get_dates(city_df), y=[input6, input7],
                      title="Covid-19 : Cases comparison between %s and %s . " % (input6, input7),
                      labels={
                          "x": "Time",
                          "value": "Number of Cases"}, template="presentation")
    if input31 == 'scatter':
        fig = px.scatter(dfresult, x=get_dates(city_df), y=[input6, input7],
                      title="Covid-19 : Cases comparison between %s and %s . " % (input6, input7),
                      labels={
                          "x": "Time",
                          "value": "Number of Cases"}, template="presentation")
    fig.update_layout(
        font_family="Courier New",
        font_color="blue",
        title_font_family="Times New Roman",
        title_font_color="red",
        legend_title_font_color="green",
        transition_duration=500
    )
    return fig

@app.callback(
    Output('graph4', 'figure'),
    [Input('input9', 'value')])
def update_map(input9):
    color_code = {
        'Active' : 'Reds',
        'Confirmed' : 'Blues',
        'Recovered' : 'Greens',
        'Deceased' : 'Blues',
        'Tested' : 'darkmint'
    }
    fig = px.choropleth(
        state_df,
        geojson="https://raw.githubusercontent.com/akash19x/covid_19_analysis_app/master/indian_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color=input9,
        color_continuous_scale=color_code[input9]
    )
    fig.update_geos(fitbounds="locations", visible=False)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
