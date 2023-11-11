import matplotlib.pyplot as plt
import pandas as pd
import random

from sklearn.ensemble import RandomForestRegressor


def preprocess(price_df):
    # return a df with all the necessary features and target for training, also drop rows with nan values
    
    new_df = price_df.copy()
    new_df = new_df[["close"]]
    new_df["close-1"] = new_df["close"].shift(-1)
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
