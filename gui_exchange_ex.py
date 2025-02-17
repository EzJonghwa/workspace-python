from tkinter import *

def convert_currency():
   print("환전 기능 영역")


# 환율 설정 (예시: 1 USD = 1300 KRW)
exchange_rate = 1300


# Tkinter 윈도우 설정
window = Tk()
window.title("Currency Converter")

# 금액 입력
amount_label = Label(window, text="Amount:")
amount_label.grid(row=0, column=0, padx=10, pady=10)
amount_entry = Entry(window)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

# From 통화 선택
from_currency_var = StringVar(window)
from_currency_var.set("KRW")
from_currency_label = Label(window, text="From:")
from_currency_label.grid(row=1, column=0, padx=10, pady=10)
from_currency_menu = OptionMenu(window, from_currency_var, "KRW", "USD")
from_currency_menu.grid(row=1, column=1, padx=10, pady=10)

# To 통화 선택
to_currency_var = StringVar(window)
to_currency_var.set("USD")
to_currency_label = Label(window, text="To:")
to_currency_label.grid(row=2, column=0, padx=10, pady=10)
to_currency_menu = OptionMenu(window, to_currency_var, "KRW", "USD")
to_currency_menu.grid(row=2, column=1, padx=10, pady=10)

# 변환 버튼
convert_button = Button(window, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# 결과 출력
result_label = Label(window, text="Converted Amount: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
