from tkinter import *

app = Tk()
app.title("환전기")


am_label = Label(app, text="금액")
am_label.grid(row=0 , column=0, padx=10, pady=10)
am_entry = Entry(app)
am_entry.grid(row=0, column=1, padx=10, pady=10)

from_cur_var = StringVar(app)
from_cur_var.set("KRW") # 기본으로 표시하고 싶은 내용
to_cur_label = Label(app, text="To:")
to_cur_label.grid(row=2, column=0, padx=10, pady=10)
from_cur_menu = OptionMenu(app, ("KRW","USD")
from_cur_menu.grid(row=1, column=1, padx=10, pady=10)




app.mainloop()