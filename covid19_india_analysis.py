import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import io
import requests
url="https://api.covid19india.org/csv/latest/states.csv"
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')),parse_dates = ["Date"],index_col="Date",dayfirst = True)
df1 = c
df = df1["2020-06-01":]
df['Tested'].fillna(0,inplace=True)
conv_dict = {
    'Recovered' : int,
    'Deceased' : int,
    'Confirmed' : int,
    'Tested' : int
}
df = df.astype(conv_dict)
df['Active'] = df['Confirmed']-df['Recovered']-df['Deceased']
all_states = df['State'].unique()
type_list = ['Active','Confirmed','Recovered','Deceased','Tested']
plot_types = ['plot','bar']

city_url="https://api.covid19india.org/csv/latest/districts.csv"
city_req=requests.get(city_url).content
city_data=pd.read_csv(io.StringIO(city_req.decode('utf-8')),parse_dates = ["Date"],index_col="Date",dayfirst = True)
city_df =city_data["2020-06-01":]
city_df['Tested'].fillna(0,inplace=True)
city_df = city_df.astype(conv_dict)
city_df['Active'] = city_df['Confirmed']-city_df['Recovered']-city_df['Deceased']
all_cities = city_df['District'].unique()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    html.H1(children='COVID-19 Analysis Project',style={'text-align': 'center','backgroundColor':'#ECC3C3'}),

    html.Div(children='''
        This is a COVID-19 analysis project made on Python Dash framework using data analysis libraries like pandas,plotly and APIs.
        It is made for educational purposes only and we have used api.covid19india.org to grt the dataset for analysis.
    ''',style={'text-align': 'center'}),
    html.Br(),
    html.Div(
        [
            dcc.Dropdown(
                id="sta1",
                options=[{
                    'label': i,
                    'value': i
                } for i in all_states],
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
                value='plot'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='graph-with-slider'),
    html.Br(),
    html.Div(
        [
            dcc.Dropdown(
                id="input3",
                options=[{
                    'label': i,
                    'value': i
                } for i in all_states],
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
                } for i in all_states],
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
                } for i in type_list],
                value='Active'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    html.Br(),
    html.Div(children=''' The comparison between two states. '''),
    html.Br(),
    dcc.Graph(id = 'graph2'),
    html.Br(),
    html.Div(
        [
            dcc.Dropdown(
                id="input6",
                options=[{
                    'label': i,
                    'value': i
                } for i in all_cities],
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
                } for i in all_cities],
                value='Basti'),
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
                } for i in type_list],
                value='Active'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    html.Br(),
    html.Div(children=''' The comparison between two Cities. '''),
    html.Br(),
    dcc.Graph(id = 'graph3')
])
@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('sta1','value'),
     Input('input2','value')])
def update_figure(sta1,input2):
    state = df[df['State'] == sta1]
    state['Dates'] = df.index.unique()
    fig = px.line(state, x='Dates', y=['Confirmed', 'Active', 'Recovered', 'Deceased'])

    if input2=='bar':
        fig = px.bar(state, x='Dates', y=['Confirmed','Active','Recovered','Deceased'])

    fig.update_layout(transition_duration=500)
    return fig
@app.callback(
    Output('graph2', 'figure'),
    [Input('input3','value'),
     Input('input4','value'),
     Input('input5','value')])
def update2(input3,input4,input5):
    input3 = str(input3)
    input4 = str(input4)
    input5 = str(input5)
    state1 = df[df['State'] == input3]
    state2 = df[df['State'] == input4]
    dfresult = state1
    dfresult[input3] = state1[input5]
    dfresult[input4] = state2[input5]
    dfresult['Dates'] = df.index.unique()
    fig = px.line(dfresult,x='Dates',y=[input3,input4])
    fig.update_layout(transition_duration=500)
    return fig

@app.callback(
    Output('graph3', 'figure'),
    [Input('input6','value'),
     Input('input7','value'),
     Input('input8','value')])
def update3(input6,input7,input8):
    input6 = str(input6)
    input7 = str(input7)
    input8 = str(input8)
    city1 = city_df[city_df['District'] == input6]
    city2 = city_df[city_df['District'] == input7]
    dfresult = city1
    dfresult[input6] = city1[input8]
    dfresult[input7] = city2[input8]
    dfresult['Dates'] = df.index.unique()
    fig = px.line(dfresult,x='Dates',y=[input6,input7])
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)