import pandas as pd
import requests
import json


def get_data(timeframe="D1", from_symbol="EUR", to_symbol="USD", debug=False):
    # get data from twelve data api

    if timeframe == "MO1":
        interval = "1month"
    elif timeframe == "W1":
        interval = "1week"
    else:
        interval = "1day"

    symbol = f"{from_symbol}/{to_symbol}"

    api_key = "0f84a727ff3d48aebe7ac0fd79d38fde"
    url = f"https://api.twelvedata.com/time_series?apikey={api_key}&interval={interval}&symbol={symbol}&format=JSON"

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
    print(data)
    print()
    print(list(data.values()))
    meta_data, dates = list(data.values())
    rows = []

    for date, ohlc in list(dates.items())[::-1]:
        row = {
            "date": date, 
            "open": float(ohlc["1. open"]), 
            "high": float(ohlc["2. high"]), 
            "low": float(ohlc["3. low"]), 
            "close": float(ohlc["4. close"])
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])

    return df


def get_df(timeframe="D1", from_symbol="EUR", to_symbol="USD"):
    # main get_df function that makes api call

    data = get_data(timeframe, from_symbol, to_symbol)
    df = make_df(data)

    return df


