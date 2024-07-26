import pyautogui
import time

from pynput.mouse import*
from tkinter import*

app =Tk()
app.title("macro")

pos_lab = Label(app,text="Mouse pointer",width=50)
pos_lab.grid(row=1,column=1,columnspan=3)

def pos_view():
        x_pos, y_pos = app.winfo_pointerx(), app.winfo_pointery()
        pos_lab.config(text=f"Mouse positon X:{x_pos} / Y: {y_pos}")
        app.after(50, pos_view)  

btn_pos = Button(app, text="마우스위치 표시", command= pos_view)
btn_pos.grid(row=2,column=1,columnspan=3)

####################################################################

lab_x = Label(app,text= "x좌표")
lab_x.grid(row=3 , column=1,padx=10, pady=10)
ent_x = Entry(app,width=5)
ent_x.grid(row=3, column=2,padx=10, pady=10)

lab_y = Label(app,text= "y좌표")
lab_y.grid(row=4 , column=1,padx=10, pady=10)
ent_y = Entry(app,width=5)
ent_y.grid(row=4, column=2,padx=10, pady=10)


def moveTo():
        move_x = int(ent_x.get())
        move_y = int(ent_y.get())
        pyautogui.moveTo(move_x,move_y,duration=0.1)

btn_change = Button(app,text="이동",command=moveTo)
btn_change.grid(row = 3, column=3, rowspan=2)

app.mainloop()
