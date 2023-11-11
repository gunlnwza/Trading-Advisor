import matplotlib.pyplot as plt


def draw_price(price_df, x="datetime", y="close", title=""):
    # show a graph of the close price

    plt.figure(figsize=(8, 6))
    plt.plot(price_df[x], price_df[y])
    plt.xticks(rotation=30)
    plt.title(title)
    
    plt.show(block=False)
