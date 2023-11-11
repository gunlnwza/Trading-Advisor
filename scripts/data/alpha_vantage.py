import pandas as pd
import requests
import json


def get_data(timeframe="D1", from_symbol="EUR", to_symbol="USD"):
    # get data from alpha vantage api

    if timeframe == "M1":
        function = "FX_MONTHLY"
    elif timeframe == "W1":
        function = "FX_WEEKLY"
    else:
        function = "FX_DAILY"

    api_key = "FTNDJSKCBSX6HZBX"
    url = f"https://www.alphavantage.co/query?function={function}&from_symbol={from_symbol}&to_symbol={to_symbol}&apikey={api_key}"

    req = requests.get(url)
    data = req.json()

    return data


def save_data(timeframe="D1", from_symbol="EUR", to_symbol="USD", filename="temp.json"):
    # save data from alpha vantage api as json to directory

    if timeframe == "M1":
        function = "FX_MONTHLY"
    elif timeframe == "W1":
        function = "FX_WEEKLY"
    else:
        function = "FX_DAILY"

    api_key = "FTNDJSKCBSX6HZBX"
    url = f"https://www.alphavantage.co/query?function={function}&from_symbol={from_symbol}&to_symbol={to_symbol}&apikey={api_key}"

    req = requests.get(url)
    data = req.json()
    json.dump(data, open(filename, "w"))


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
