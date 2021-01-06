import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
from utils import get_dates, get_state_data, get_city_data, get_given_city_data, \
    get_given_state_data, get_state_data_latest
from plots import line_plot, area_plot, bar_plot, histogram_plot, funnel_plot, scatter_plot

cases_types = ['Active', 'Confirmed', 'Recovered', 'Deceased', 'Tested']
plot_types = ['plot', 'bar', 'histogram', 'area', 'funnel', 'scatter']
bootstrap = "https://stackpath.bootstrapcdn.com/bootswatch/4.5.2/solar/bootstrap.min.css"
app = dash.Dash(__name__, external_stylesheets=[bootstrap])
app.title = "COVID-19 Maps"
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
                id="states_1",
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
                id="plot_types_1",
                options=[{
                    'label': i,
                    'value': i
                } for i in plot_types],
                value='plot'
            ),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='graph1'),
    html.H4(children='A comparison of cases between any two states.', style={'text-align': 'center'}),
    html.Div(
        [
            dcc.Dropdown(
                id="states_2_1",
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
                id="states_2_2",
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
                id="case_types_2",
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
                id="plot_types_2",
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
                id="cities_3_1",
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
                id="cities_3_2",
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
                id="case_types_3",
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
                id="plot_types_3",
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
    html.H4(children='Map Of India on the basis of category of Covid-19 Cases.', style={'text-align': 'center'}),
    html.Div(
        [
            dcc.Dropdown(
                id="case_types_4",
                options=[{
                    'label': i,
                    'value': i
                } for i in cases_types],
                value='Active'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='graph4'),
    html.Br(),
    html.Div(
        [
        html.H4(children='Developed by : Akash Mishra', style={'text-align': 'center'}),
        dcc.Link('Source Code', href='https://github.com/akash19x/covid_19_analysis_app')
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    html.Br(),
    html.Br()
])


@app.callback(
    Output('graph1', 'figure'),
    [Input('states_1', 'value'),
     Input('plot_types_1', 'value')])
def update_state_figures(state, plot_type):
    fig = None
    x = get_dates(state_df)
    y = ['Confirmed', 'Active', 'Recovered', 'Deceased']
    title = "Covid-19 data of state."
    labels = {"x": "Time", "value": "Number of Cases"}
    template = "presentation"
    state = get_given_state_data(state_df, state)
    data = state
    if plot_type == "plot":
        fig = line_plot(data, x, y, title, labels, template)
    if plot_type == "bar":
        fig = bar_plot(data, x, y, title, labels, template)
    if plot_type == "histogram":
        fig = histogram_plot(data, x, y, title, labels, template)
    if plot_type == "area":
        fig = area_plot(data, x, y, title, labels, template)
    if plot_type == "funnel":
        fig = funnel_plot(data, x, y, title, labels, template)
    if plot_type == "scatter":
        fig = scatter_plot(data, x, y, title, labels, template)
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
    [Input('states_2_1', 'value'),
     Input('states_2_2', 'value'),
     Input('case_types_2', 'value'),
     Input('plot_types_2', 'value')])
def compare_two_states(state_a, state_b, case_type, plot_type):
    state1 = get_given_state_data(state_df, state_a)
    state2 = get_given_state_data(state_df, state_b)
    dfresult = state1
    dfresult[state_a] = state1[case_type]
    dfresult[state_b] = state2[case_type]
    data = dfresult
    x = get_dates(state_df)
    y = [state_a, state_b]
    title = "Covid-19 : Cases comparison between %s and %s . " % (state_a, state_b)
    labels = {"x": "Time", "value": "Number of Cases"}
    template = "presentation"
    fig = None
    if plot_type == "plot":
        fig = line_plot(data, x, y, title, labels, template)
    if plot_type == "bar":
        fig = bar_plot(data, x, y, title, labels, template)
    if plot_type == "histogram":
        fig = histogram_plot(data, x, y, title, labels, template)
    if plot_type == "area":
        fig = area_plot(data, x, y, title, labels, template)
    if plot_type == "funnel":
        fig = funnel_plot(data, x, y, title, labels, template)
    if plot_type == "scatter":
        fig = scatter_plot(data, x, y, title, labels, template)

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
    [Input('cities_3_1', 'value'),
     Input('cities_3_2', 'value'),
     Input('case_types_3', 'value'),
     Input('plot_types_3', 'value')])
def compare_two_cities(city_a, city_b, case_type, plot_type):
    city1 = get_given_city_data(city_df, city_a)
    city2 = get_given_city_data(city_df, city_b)
    dfresult = city1
    dfresult[city_a] = city1[case_type]
    dfresult[city_b] = city2[case_type]
    data = dfresult
    x = get_dates(city_df)
    y = [city_a, city_b]
    title = "Covid-19 : Cases comparison between %s and %s . " % (city_a, city_b)
    labels = {"x": "Time", "value": "Number of Cases"}
    template = "presentation"
    fig = None
    if plot_type == "plot":
        fig = line_plot(data, x, y, title, labels, template)
    if plot_type == "bar":
        fig = bar_plot(data, x, y, title, labels, template)
    if plot_type == "histogram":
        fig = histogram_plot(data, x, y, title, labels, template)
    if plot_type == "area":
        fig = area_plot(data, x, y, title, labels, template)
    if plot_type == "funnel":
        fig = funnel_plot(data, x, y, title, labels, template)
    if plot_type == "scatter":
        fig = scatter_plot(data, x, y, title, labels, template)
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
    [Input('case_types_4', 'value')])
def update_map(case_type):
    color_code = {
        'Active' : 'Reds',
        'Confirmed' : 'Blues',
        'Recovered' : 'Greens',
        'Deceased' : 'Blues',
        'Tested' : 'darkmint'
    }
    fig = px.choropleth(
        state_df,
        geojson="https://raw.githubusercontent.com/akash19x/CloroPleth-Maps/main/indian_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color=case_type,
        color_continuous_scale=color_code[case_type]
    )
    fig.update_geos(fitbounds="locations", visible=False)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True,port=8049)
