import pandas as pd
import requests
import json


def api_get_data(timeframe="D1", from_symbol="EUR", to_symbol="USD", data_points=100, debug=False):
    # get data from twelve data api

    translation = {
        "M1": "1min",
        "M5": "5min",
        "M15": "15min",
        "M30": "30min",
        "H1": "1h",
        "H4": "4h",
        "D1": "1day",
        "W1": "1week",
        "MO1": "1month"
    }
    if timeframe in translation:
        interval = translation[timeframe]
    else:
        interval = "1day"

    symbol = f"{from_symbol}/{to_symbol}"

    api_key = "0f84a727ff3d48aebe7ac0fd79d38fde"
    url = f"https://api.twelvedata.com/time_series?apikey={api_key}&interval={interval}&symbol={symbol}&outputsize={data_points}&format=JSON"

    req = requests.get(url)
    data = req.json()

    if debug:
        json.dump(data, open("temp.json", "w"))

    return data


def load_data(filename="temp.json"):
    # load the saved data in directory

    data = json.load(open(filename))
    return data


def make_df(data):
    meta, values, status = list(data.values())

    df = pd.DataFrame(values)
    df["datetime"] = pd.to_datetime(df["datetime"])
    for col in ("open", "high", "low", "close"):
        df[col] = pd.to_numeric(df[col])
    df = df.iloc[::-1]
    df = df.reset_index(drop=True)

    return df


def api_get_df(timeframe="D1", from_symbol="EUR", to_symbol="USD"):
    # main get_df function that makes api call

    data = api_get_data(timeframe, from_symbol, to_symbol)
    df = make_df(data)

    return df
