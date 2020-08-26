from utils import get_dates, get_state_data, get_city_data, get_given_state_data, get_given_city_data
import pytest


def test_get_state_data():
    expected_output = ['State', 'Confirmed', 'Recovered', 'Deceased', 'Other', 'Tested', 'Active']
    result = list(get_state_data()[0].columns)
    assert result == expected_output


def test_get_city_data():
    expected_output = ['State', 'District', 'Confirmed', 'Recovered', 'Deceased', 'Other', 'Tested', 'Active']
    result = list(get_city_data()[0].columns)
    assert result == expected_output


def test_get_Dates():
    data = get_state_data()[0]
    expected_output = '2020-07-07'
    assert any(i == expected_output for i in list(get_dates(data)))


def test_get_given_State_data():
    state_df = get_state_data()[0]
    state_data = get_given_state_data(state_df, 'Uttar Pradesh')
    output_columns = ['State', 'Confirmed', 'Recovered', 'Deceased', 'Other', 'Tested', 'Active']
    assert (list(state_data.columns) == output_columns) and (all(state_data['State'] == 'Uttar Pradesh'))


def test_get_given_city_data():
    city_df = get_city_data()[0]
    city_data = get_given_city_data(city_df, 'Lucknow')
    output_columns = ['State', 'District', 'Confirmed', 'Recovered', 'Deceased', 'Other', 'Tested', 'Active']
    assert (list(city_data.columns) == output_columns) and (all(city_data['District'] == 'Lucknow'))

@pytest.mark.duplicate_test_to_fail
def test_get_given_city_dataw():
    city_df = get_city_data()[0]
    city_data = get_given_city_data(city_df, 'Lucknow')
    output_columns = ['State', 'District', 'Confirmed', 'Recovered', 'Deceased', 'Other', 'Tested', 'Active']
    assert (list(city_data.columns) == output_columns) and (all(city_data['District'] == 'Ldsjckjb'))

