from tkinter import *

def up_label(*args):
    selection= "선택 항목 : " + str(op_var.get())
    lab_op_answer.config(text=selection)

app = Tk()

label_q = Label(app, text= "가장 배우기 쉬운 언어는?")
label_q.pack()

op = ["Python", "Pascal", "Scratch"]
op_var = StringVar(app)
op_var.set(op[0])
op_menu = OptionMenu(app, op_var, *op)
op_menu.pack()

lab_op_answer = Label(app, text="")
lab_op_answer.pack()
op_var.trace_add("write",up_label )
app.mainloop()