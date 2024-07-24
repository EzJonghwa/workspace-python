from tkinter import *

def move_left(event):
    canvas.move(ball, -5,0)
def move_right(event):
    canvas.move(ball, 5,0)
def move_up(event):
    canvas.move(ball, 0,-5)
def move_down (event):
    canvas.move(ball, 0,5)

def move_left2(event):
    canvas.move(ball2, -5,0)
def move_right2(event):
    canvas.move(ball2, 5,0)
def move_up2(event):
    canvas.move(ball2, 0,-5)
def move_down2 (event):
    canvas.move(ball2, 0,5)



app = Tk()

canvas = Canvas(app, width=400 , height= 300)
canvas.pack()

ball = canvas.create_oval(100, 150, 150, 200, fill="red")

app.bind('<Left>', move_left)
app.bind('<Right>', move_right)
app.bind('<Up>', move_up)
app.bind('<Down>', move_down)

ball2 = canvas.create_oval(200, 250, 150, 200, fill="white")
app.bind('<a>', move_left2)
app.bind('<d>', move_right2)
app.bind('<w>', move_up2)
app.bind('<s>', move_down2)
app.mainloop()