import matplotlib.pyplot as plt
import pandas as pd
import random

from sklearn.ensemble import RandomForestRegressor


def preprocess(price_df):
    # return a df with all the necessary features and target for training, also drop rows with nan values
    
    new_df = price_df.copy()

    new_df["close-1"] = new_df["close"].shift(-1)

    new_df = new_df[["close", "close-1"]]
    new_df.dropna(inplace=True)

    return new_df


def preprocess_v2(price_df):
    new_df = price_df.copy()

    new_df["sma10"] = new_df["close"].rolling(window=10).mean()
    #new_df["sma20"] = new_df.rolling(window=20).mean()

    new_df["ratio10"] = new_df["close"] / new_df["ratio10"]
    new_df["ratio10-1"] = new_df["ratio10"].shift(-1)

    new_df = new_df[["ratio10", "ratio10-1"]]
    new_df.dropna(inplace=True)

    return new_df


def get_Xy(df):
    # separate X and y, y is the rightmost column

    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    return X, y


def get_model(price_df):
    # return trained model

    df = preprocess(price_df)
    X, y = get_Xy(df)

    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X, y)

    return model


def get_model_rel_close(price_df):
    # train and predict relative close price

    df = preprocess_v2(price_df)
    X, y = get_Xy(df)

    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X, y)

    return model


def get_predictions_rel_close(model, price_df):
    pass