from sklearn.ensemble import RandomForestRegressor 

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import requests
import json


# PRICE FUNCTIONS ------------------------------------------------------------


def get_prices(timeframe="D1", from_symbol="EUR", to_symbol="USD"):
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

    prices = list(data.values())[1]

    return prices


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


def load_prices(filename="temp.json"):
    # load the price from saved data in directory

    data = load_data(filename)
    prices = list(data.values())[1]

    return prices


# MODEL FUNCTIONS ------------------------------------------------------------


def preprocess(prices):
    df = pd.DataFrame()

    df["Date"] = prices.keys()

    return df


def train_and_show_future(timeframe, from_symbol, to_symbol):
    model = RandomForestRegressor(n_estimators=100, min_samples_split=10, random_state=0)

    print("\rGetting Price", end="")
    prices = get_prices(timeframe, from_symbol, to_symbol)

    print("\rPreprocessing", end="")
    df = preprocess(prices)
    print("\r", end="")

    print(df)

