import tkinter as tk # tk로 별칭사용
from tkinter import messagebox
root = tk.Tk() # 새로운 인스턴스 설정 : Tk= gui환경 만들기
root.title("my tkinter window") # 윈도우창 이릅
root.geometry("300x350") # 크기, 해상도 설정
#단순 텍스트 출력 label
lbl = tk.Label(root, text="이름:")
lbl.grid(row=0, column=0)
# entry = 입력창
txt= tk.Entry(root)
txt.grid(row=0, column=1)

def fn_click():
    nm = txt.get() # entry 값을 가져옴
    print(nm)
    messagebox.showinfo("login", nm + "님 반갑습니다")
# button = 버튼 
btn = tk.Button(root,text="로그인",command=fn_click)
btn.grid(row=1,column=0, columnspan=2, sticky="ew") # sticky="ew" == 수평 확장

root.mainloop()
