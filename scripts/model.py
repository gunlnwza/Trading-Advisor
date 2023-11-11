import matplotlib.pyplot as plt
import pandas as pd

from sklearn.ensemble import RandomForestRegressor

from data import get_df_from_filename


def preprocess(df):
    # return a df with all the necessary features and target for training, also drop rows with nan values
    
    new_df = df.copy()
    new_df = new_df[["close"]]
    new_df["close-1"] = new_df["close"].shift(-1)
    new_df.dropna(inplace=True)

    return new_df


def preprocess_v2(df):
    new_df = df.copy()
    new_df = new_df[["close"]]
    new_df["close-1"] = new_df["close"].shift(-1)
    new_df.dropna(inplace=True)

    return new_df


def get_Xy(df):
    # separate X and y, y is the rightmost column

    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    return X, y


def train_and_show_future(df):
    # TODO: make 2 separate functions: (return a trained model) and (plotting the predictions)

    df = preprocess(df)
    X, y = get_Xy(df)

    train_test_index = 80

    X_train, X_test = X.iloc[:train_test_index], X.iloc[train_test_index:]
    y_train, y_test = y.iloc[:train_test_index], y.iloc[train_test_index:]

    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)

    y_predict = model.predict(X_test)

    plt.figure(figsize=(8, 6))
    plt.xticks(rotation=30)
    plt.plot(df["close"])

    plt.plot([i + train_test_index + 1 for i in range(len(y_test))], y_test)
    plt.plot([i + train_test_index + 1 for i in range(len(y_predict))], y_predict)
    plt.legend(["Close", "Test", "Predict"])
    
    plt.show()


def tell_buy_or_sell(df):
    result = ""