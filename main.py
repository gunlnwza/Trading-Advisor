import tkinter as tk
import random

from scripts.data.twelve_data import get_data, make_df
from scripts.display import draw_price
from scripts.model import tell_buy_or_sell


def get_advice():
    timeframe = stringvar_timeframe.get()
    from_symbol = stringvar_base_currency.get()
    to_symbol = stringvar_quote_currency.get()

    data = get_data(timeframe, from_symbol, to_symbol)
    if data["status"] != "ok":
        print("An error occured")
        return
    df = make_df(data)

    advice = tell_buy_or_sell(df)
    label_result.config(text=f"You should {advice} {timeframe} {from_symbol}/{to_symbol} !")
    draw_price(price_df=df, x="datetime", y="close", title=f"{timeframe} {from_symbol}/{to_symbol}")


window = tk.Tk()
window.title("Trading Advisor")
window.geometry("300x150")


# The dropdown menus part
frame_infomation = tk.Frame()

base_currencies = ["USD", "AUD", "CAD", "CHF", "EUR", "GBP", "JPY", "THB"]
quote_currencies = base_currencies.copy()
stringvar_base_currency = tk.StringVar(value=base_currencies[0])
stringvar_quote_currency = tk.StringVar(value=quote_currencies[0])

timeframes = ["M1", "M5", "M15", "M30", "H1", "H4", "D1", "W1", "MO1"]
stringvar_timeframe = tk.StringVar(value=timeframes[0])

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
button_ask = tk.Button(master=window, text="Ask", width=6, command=get_advice)
button_ask.pack(pady=(0, 10))


# the label part
label_result = tk.Label(window, text="...")
label_result.pack()


window.mainloop()
