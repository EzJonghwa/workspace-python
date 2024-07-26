import pyautogui
import time

from pynput.mouse import*
from tkinter import*

def update_mouse_position_label():
    x, y = root.winfo_pointerx(), root.winfo_pointery()
    position_label.config(text=f"현재 좌표: x={x}, y={y}")
    root.after(100, update_mouse_position_label)  # 100ms마다 업데이트

root = Tk()
root.title("마우스 좌표 출력 프로그램")

position_label =Label(root, text="마우스 좌표:")
position_label.pack()

update_mouse_position_label()  # 좌표 업데이트 시작

root.mainloop() 