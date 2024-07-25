import pyautogui
import time

from pynput.mouse import*
from tkinter import*

app =Tk()

def position_move():
        x_amount = ent_x.get()



pos_lab = Label(app,text="Mouse pointer",width=50)
pos_lab.grid(row=1,column=1,columnspan=3)

def pos_view():
        x_pos, y_pos = pyautogui.position()
        pos_lab.config(text=f"Mouse positon X:{x_pos} / Y: {y_pos}")

btn = Button(app, text="마우스위치 표시", command= pos_view)
btn.grid(row=2,column=1,columnspan=3)

lab_x = Label(app,text= "x좌표")
lab_x.grid(row=3 , column=1,padx=10, pady=10)
ent_x = Entry(app,width=5)
ent_x.grid(row=3, column=2,padx=10, pady=10)

lab_y = Label(app,text= "y좌표")
lab_y.grid(row=4 , column=1,padx=10, pady=10)
ent_y = Entry(app,width=5)
ent_y.grid(row=4, column=2,padx=10, pady=10)

btn_change = Button(app,text="이동")
btn_change.grid(row = 3, column=3, rowspan=2)

app.mainloop()
