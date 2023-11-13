import matplotlib.pyplot as plt
import pandas as pd


def draw_price(price_df, x="datetime", y="close", title=""):
    # show a graph of the close price

    plt.figure(title, figsize=(8, 6))

    plt.plot(price_df[x], price_df[y])

    plt.xticks(rotation=30)
    plt.title(title)

    fig_manager = plt.get_current_fig_manager()
    fig_manager.window.wm_geometry("+500+100")
    plt.show(block=False)


def show_future(model, price_df, predict_points=10, x="datetime", y="close", title=""):
    # show the future predicted by model

    plt.figure(title, figsize=(8, 6))

    plt.plot(price_df[y], label="Actual Close")

    future_predictions = []

    last_close = price_df["close"].iloc[-1]

    for i in range(predict_points):
        future_predictions.append(last_close)
        last_close = model.predict(pd.DataFrame({"close": [last_close]}))[0]

    future_indices = [i - 1 for i in range(len(price_df), len(price_df) + predict_points)]

    plt.plot(future_indices, future_predictions, label="Predicted Close", linestyle="--")
    plt.xticks(rotation=30)
    plt.title(title)
    plt.title(title)
    plt.legend()

    plt.get_current_fig_manager().window.wm_geometry("+500+100")
    plt.show()


def show_future_rel_close(model, price_df, predict_points=10, x="datetime", y="close", title=""):
    # show the future predicted by model

    plt.figure(title, figsize=(8, 6))
    plt.plot(price_df[y], label="Actual Close")

    future_predictions = []

    last_close = price_df["close"].iloc[-1]

    for i in range(predict_points):
        future_predictions.append(last_close)
        last_close = model.predict(pd.DataFrame({"close": [last_close]}))[0]

    future_indices = [i - 1 for i in range(len(price_df), len(price_df) + predict_points)]

    plt.plot(future_indices, future_predictions, label="Predicted Close", linestyle="--")
    plt.xticks(rotation=30)
    plt.title(title)
    plt.title(title)
    plt.legend()

    fig_manager = plt.get_current_fig_manager()
    fig_manager.window.wm_geometry("+500+100")
    plt.show()


def plot_price_and_predictions(price_df, predictions, plot_points=None, title=""):
    # plot the last <plot_points> of price
    
    plt.figure(figsize=(8, 6))
    plt.title(title)
    if plot_points:
        plt.plot(price_df["close"].iloc[-plot_points:], label="Actual Close")
    else:
        plt.plot(price_df["close"], label="Actual Close")

    future_indices = [i + len(price_df) - 1 for i in range(len(predictions))]
    plt.plot(future_indices, predictions, label="Predicted Close", linestyle="--")

    plt.xticks(rotation=30)
    plt.legend()

    plt.get_current_fig_manager().window.wm_geometry("+500+100")
    plt.show()
