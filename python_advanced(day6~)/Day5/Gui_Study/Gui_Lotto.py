import tkinter as tk
from tkinter import messagebox
import lotto

lto = tk.Tk()
lto.title("로또번호 생성기")
lto.geometry("180x180")

txt = tk.Entry(lto)
txt.grid(row=0,column=0)

def fn_click():
    nm = int(txt.get()) 
    messagebox.showinfo("Lotto number", lotto.lotto_maker(nm))

btn = tk.Button(lto,text="생성",command=fn_click)
btn.grid(row=1, column=0, columnspan=2, sticky="ew")
lto.mainloop()

