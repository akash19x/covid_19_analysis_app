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
    state_data = state_df[state_df['State'] == state]
    return state_data


def get_given_city_data(city_df, city):
    city_data = city_df[city_df['District'] == city]
    return city_data


def get_state_data():
    state_url = "https://api.covid19india.org/csv/latest/states.csv"
    state_data = requests.get(state_url).content
    state_cleaned_data = pd.read_csv(io.StringIO(state_data.decode('utf-8')), parse_dates=["Date"], index_col="Date",
                                     dayfirst=True)
    state_df = state_cleaned_data["2020-06-20":]
    state_df['Tested'].fillna(0, inplace=True)
    state_df = state_df.astype(conv_dict)
    state_df['Active'] = state_df['Confirmed'] - state_df['Recovered'] - state_df['Deceased']
    all_states = state_df['State'].unique()
    return state_df, all_states


def get_city_data():
    city_url = "https://api.covid19india.org/csv/latest/districts.csv"
    city_data = requests.get(city_url).content
    city_cleaned_data = pd.read_csv(io.StringIO(city_data.decode('utf-8')), parse_dates=["Date"], index_col="Date",
                                    dayfirst=True)
    city_df = city_cleaned_data["2020-06-20":]
    city_df['Tested'].fillna(0, inplace=True)
    city_df.astype(conv_dict)
    city_df['Active'] = city_df['Confirmed'] - city_df['Recovered'] - city_df['Deceased']
    all_cities = city_df['District'].unique()
    return city_df, all_cities
