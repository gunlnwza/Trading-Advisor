import matplotlib.pyplot as plt


def draw_price(price_df, x="datetime", y="close", title=""):
    # show a graph of the close price

    plt.figure(title, figsize=(8, 6))
    plt.plot(price_df[x], price_df[y])
    plt.xticks(rotation=30)
    plt.title(title)

    fig_manager = plt.get_current_fig_manager()
    fig_manager.window.wm_geometry("+500+100")
    plt.show(block=False)


def show_future(model, price_df, x="datetime", y="close", title=""):
    # show the future predicted by model

    plt.figure(title, figsize=(8, 6))

    plt.plot(price_df[x], price_df[y])

    plt.xticks(rotation=30)
    plt.title(title)

    fig_manager = plt.get_current_fig_manager()
    fig_manager.window.wm_geometry("+500+100")
    plt.show()


if __name__ == "__main__":
    from model import get_model
    from data.twelve_data import load_data, make_df

    data = load_data()
    df = make_df(data)
    model = get_model(df)
    print(df)

    show_future(model, df)
