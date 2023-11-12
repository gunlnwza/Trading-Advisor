import tkinter as tk
import random

from scripts.data.twelve_data import api_get_data, make_df, load_data
from scripts.display import show_future, draw_price, show_future_rel_close
from scripts.model import get_model, get_predictions


def update_label_advice(advice, timeframe, from_symbol, to_symbol):
    if advice == "BUY":
        fg = "green"
    elif advice == "SELL":
        fg = "red"
    else:
        fg = "black"
    label_advice.config(fg=fg)
    text = f"You should {advice} {timeframe} {from_symbol}/{to_symbol} !"
    label_advice.config(text=text)


def get_advice(price_df, predictions):
    # say BUY if price will go up, say SELL if price will go down
    
    pass


def button_ask_pressed():
    timeframe = stringvar_timeframe.get()
    from_symbol = stringvar_base_currency.get()
    to_symbol = stringvar_quote_currency.get()

    if from_symbol == to_symbol:
        label_advice.config(text="You must select different currencies")
        return

    data = api_get_data(timeframe, from_symbol, to_symbol)
    if data["status"] != "ok":
        label_advice.config(text="An error occured: cannot get API data")
        return

    price_df = make_df(data)
    model = get_model(price_df)

    predictions = get_predictions(model, price_df)
    print(predictions)
    
    advice = get_advice(price_df, predictions)
    update_label_advice(advice, timeframe, from_symbol, to_symbol)
    

window = tk.Tk()
window.title("Trading Advisor")
window.geometry("300x150")


# The dropdown menus part
frame_infomation = tk.Frame()

base_currencies = ["USD", "AUD", "CAD", "CHF", "EUR", "GBP", "JPY", "THB"]
quote_currencies = base_currencies.copy()
stringvar_base_currency = tk.StringVar(value="EUR")
stringvar_quote_currency = tk.StringVar(value="USD")

timeframes = ["M1", "M5", "M15", "M30", "H1", "H4", "D1", "W1", "MO1"]
stringvar_timeframe = tk.StringVar(value="D1")

label_pair = tk.Label(master=frame_infomation, text="Pair:")
optionmenu_base_currency = tk.OptionMenu(frame_infomation, stringvar_base_currency, *base_currencies)
optionmenu_quote_currency = tk.OptionMenu(frame_infomation, stringvar_quote_currency, *quote_currencies)
optionmenu_base_currency.config(width=5)
optionmenu_quote_currency.config(width=5)
label_pair.grid(row=0, column=0, sticky="e")
optionmenu_base_currency.grid(row=0, column=1, sticky="ew", padx=5)
optionmenu_quote_currency.grid(row=0, column=2, sticky="ew")

label_timeframe = tk.Label(frame_infomation, text="Timeframe:")
optionmenu_timeframe = tk.OptionMenu(frame_infomation, stringvar_timeframe, *timeframes)
optionmenu_timeframe.config(width=5)
label_timeframe.grid(row=2, column=0, sticky="e")
optionmenu_timeframe.grid(row=2, column=1, sticky="ew", padx=5)

frame_infomation.pack(padx=10, pady=10)


# the button part
button_ask = tk.Button(master=window, text="Ask", width=6, command=button_ask_pressed)
button_ask.pack(pady=(0, 10))


# the label part
label_advice = tk.Label(window, text="...")
label_advice.pack()


window.mainloop()
