import pandas as pd
import requests
import io

conv_dict = {
    'Recovered': int,
    'Deceased': int,
    'Confirmed': int,
    'Tested': int
}


def get_dates(data):
    return data.index.unique()


def get_given_state_data(state_df, state):
    return state_df[state_df.loc[:, 'State'] == state]


def get_given_city_data(city_df, city):
    return city_df[city_df.loc[:, 'District'] == city]


def get_state_data_latest():
    state_df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise.csv")[['State', 'Confirmed', 'Recovered', 'Deaths', 'Active']]
    return state_df


def get_state_data():
    state_url = "https://api.covid19india.org/csv/latest/states.csv"
    state_data = requests.get(state_url).content
    state_cleaned_data = pd.read_csv(io.StringIO(state_data.decode('utf-8')), parse_dates=["Date"], index_col="Date",
                                     dayfirst=True)
    state_df = state_cleaned_data.loc["2020-06-20":]
    state_df.loc[:, 'Tested'].fillna(0, inplace=True)
    state_df = state_df.astype(conv_dict)
    state_df.loc[:, 'Active'] = state_df.loc[:, 'Confirmed'] - state_df.loc[:, 'Recovered'] - state_df.loc[:, 'Deceased']
    all_states = state_df.loc[:, 'State'].unique()
    return state_df, all_states


def get_city_data():
    city_url = "https://api.covid19india.org/csv/latest/districts.csv"
    city_data = requests.get(city_url).content
    city_cleaned_data = pd.read_csv(io.StringIO(city_data.decode('utf-8')), parse_dates=["Date"], index_col="Date",
                                    dayfirst=True)
    city_df = city_cleaned_data.loc["2020-06-20":]
    city_df.loc[:, 'Tested'].fillna(0, inplace=True)
    city_df.astype(conv_dict)
    city_df.loc[:, 'Active'] = city_df.loc[:, 'Confirmed'] - city_df.loc[:, 'Recovered'] - city_df.loc[:, 'Deceased']
    all_cities = city_df.loc[:, 'District'].unique()
    return city_df, all_cities
