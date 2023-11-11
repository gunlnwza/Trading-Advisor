import matplotlib.pyplot as plt


def draw_close(price_df, title=""):
    # show a graph of the close price

    plt.figure(figsize=(8, 6))
    plt.plot(price_df["date"], price_df["close"])
    plt.xticks(rotation=30)
    plt.title(title)
    
    plt.show()
