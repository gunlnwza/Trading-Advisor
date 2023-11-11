from sklearn.ensemble import RandomForestRegressor 

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import requests
import json


# PRICE FUNCTIONS ------------------------------------------------------------


def get_data(timeframe="D1", from_symbol="EUR", to_symbol="USD"):
    # get data from api and return the prices

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
    # save data from api as json to directory

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


def load_data(filename="temp.json"):
    # load the saved data in directory

    data = json.load(open(filename))
    return data


def get_df(timeframe="D1", from_symbol="EUR", to_symbol="USD"):
    # main get_df function

    data = get_data(timeframe, from_symbol, to_symbol)
    meta_data, dates = list(data.values())
    rows = []

    for date, ohlc in list(dates.items())[::-1]:
        row = {"date": date, "open": ohlc["1. open"], "high": ohlc["2. high"], "low": ohlc["3. low"], "close": ohlc["4. close"]}
        rows.append(row)

    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])

    return df


def get_df_from_filename(filename="temp.json"):
    # get_df function for debugging

    data = load_data("temp.json")
    meta_data, dates = list(data.values())
    rows = []

    for date, ohlc in list(dates.items())[::-1]:
        row = {"date": date, "open": ohlc["1. open"], "high": ohlc["2. high"], "low": ohlc["3. low"], "close": ohlc["4. close"]}
        rows.append(row)

    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])

    return df


# MODEL FUNCTIONS ------------------------------------------------------------


def preprocess(df):
    # return a df with all the necessary features and target for training, also drop rows with nan values
    
    new_df = df.copy()
    new_df = new_df[["close"]]
    new_df["close-1"] = new_df["close"].shift(-1)
    new_df.dropna(inplace=True)

    return new_df


def train_and_show_future():
    # TODO: make 2 separate functions: (return a trained model) and (plotting the predictions)

    df = get_df_from_filename()
    df = preprocess(df)
    print(df)
    model = RandomForestRegressor(n_estimators=100, min_samples_split=10, random_state=0)


train_and_show_future()
