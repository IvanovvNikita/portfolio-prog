import getweatherdata
import pytest
import os

api_key = os.environ['API_KEY']


def test_without_key():
    assert getweatherdata.get_weather_data(
        "moscow") is None, \
        " Для получения данных необходимо задать значение для api_key "


def test_in_riga():
    assert getweatherdata.get_weather_data("Riga",
                                           api_key) is not None, \
        " Type of response is not none while using the key "


def test_type_of_res():
    assert type(getweatherdata.get_weather_data("Riga",
                                                api_key)) is str, \
        " Type of response is not none while using the key "


def test_args_error():
    assert getweatherdata.get_weather_data(
        '') is None, \
        " There should be one positional argument: 'city' and one keyword argument 'key_arg'"


def test_pos_arg_error():
    assert getweatherdata.get_weather_data('',
                                           api_key) is None, \
        " There should be one positional argument: 'city' "


def test_coords_dim():
    import json

    assert len(
        json.loads(getweatherdata.get_weather_data('Riga', api_key)).get('coord')) == 2, \
        " Dimension is 2: lon and lat "


def test_temp_type():
    import json

    assert type(json.loads(getweatherdata.get_weather_data('Riga', api_key)).get(
        'feels_like')) is float, \
        " Error with type of feels_like attribute "


inp_params_1 = "city, api_key, expected_country"
exp_params_countries = [("Chicago", api_key, 'US'),
                        ("Saint Petersburg", api_key, 'RU'),
                        ("Dakka", api_key, 'BD'), ("Minsk", api_key, 'BY'),
                        ("Kioto", api_key, 'JP'), ("Anchorage", api_key, 'US'),
                        ("Havana", api_key, 'CU')]


@pytest.mark.parametrize(inp_params_1, exp_params_countries)
def test_countries(city, api_key, expected_country):
    import json

    assert json.loads(getweatherdata.get_weather_data(city, api_key)).get('country',
                                                                              'NoValue') == expected_country, \
        " Error with country code "


#
#
inp_params_2 = "city, api_key, expected_time"
exp_params_timezones = [("Chicago", api_key, 'UTC-6'),
                        ("Saint Petersburg", api_key, 'UTC+3'),
                        ("Dakka", api_key, 'UTC+6'),
                        ("Minsk", api_key, 'UTC+3'),
                        ("Kioto", api_key, 'UTC+9'),
                        ("Anchorage", api_key, 'UTC-9'),
                        ("Havana", api_key, 'UTC-5')]


@pytest.mark.parametrize(inp_params_2, exp_params_timezones)
def test_utc_time(city, api_key, expected_time):
    import json
    assert json.loads(getweatherdata.get_weather_data(city, api_key)).get('timezone',
                                                                              'NoValue') == expected_time, \
        " Error with timezone "