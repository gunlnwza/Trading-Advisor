import tkinter as tk
import random

from scripts.data import get_data, make_df
from scripts.display import draw_close


def get_advice():
    timeframe = stringvar_timeframe.get()
    from_symbol = stringvar_base_currency.get() 
    to_symbol = stringvar_quote_currency.get()

    data = get_data(timeframe, from_symbol, to_symbol)
    df = make_df(data)

    draw_close(df, f"{timeframe} {from_symbol} {to_symbol}")


window = tk.Tk()
window.title("Trading Advisor")
window.geometry("300x150")


# The dropdown menus part
frame_infomation = tk.Frame()

base_currencies = ["USD", "EUR", "GBP", "AUD"]
quote_currencies = base_currencies.copy()
stringvar_base_currency = tk.StringVar(value=base_currencies[1])
stringvar_quote_currency = tk.StringVar(value=quote_currencies[0])

label_pair = tk.Label(master=frame_infomation, text="Pair:")
optionmenu_base_currency = tk.OptionMenu(frame_infomation, stringvar_base_currency, *base_currencies)
optionmenu_quote_currency = tk.OptionMenu(frame_infomation, stringvar_quote_currency, *quote_currencies)
label_pair.grid(row=0, column=0, sticky="e")
optionmenu_base_currency.grid(row=0, column=1, padx=10)
optionmenu_quote_currency.grid(row=0, column=2)

timeframes = ["D1", "W1", "M1"]
stringvar_timeframe = tk.StringVar(value=timeframes[0])

label_timeframe = tk.Label(frame_infomation, text="Timeframe:")
entry_timeframe = tk.OptionMenu(frame_infomation, stringvar_timeframe, *timeframes)
label_timeframe.grid(row=2, column=0, sticky="e")
entry_timeframe.grid(row=2, column=1)

frame_infomation.pack(padx=10, pady=10)


# the button part
button_ask = tk.Button(master=window, text="Ask", width=6, command=get_advice)
button_ask.pack(pady=(0, 10))


window.mainloop()
