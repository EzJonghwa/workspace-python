from tkinter import *

def sel():
    selection = "선택 항목 :"+str(var.get())
    label_a.config(text=selection)

app = Tk()

label_q = Label(app, text="1. 가장 배우기 쉬운 언어는?")
label_q.pack()

#정수형 변수
var = IntVar()
Radiobutton(app, text="Python", variable=var, value=1, command=sel).pack(anchor=E)
Radiobutton(app, text="Java", variable=var, value=2, command=sel).pack(anchor=E)
Radiobutton(app, text="C", variable=var, value=3,command=sel).pack(anchor=E)

# anchor =상하 좌우 정렬 W = 왼쪽 정렬 / E = 우측 정렬
label_a = Label(app,text="")
label_a.pack()

app.mainloop()