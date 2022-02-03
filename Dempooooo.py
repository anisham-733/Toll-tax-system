from tkinter import *
from PIL import ImageTk,Image
win=Tk()
win.geometry('700x850')

win.config(background='#262626')
bg=ImageTk.PhotoImage(Image.open("Admin_bg2.jpg"))

l=Label(win,image=bg,background='#262626').place(relx=0.01,rely=0.03,relheight=1.2,relwidth=0.98)
win.iconbitmap('icons/Admin_panel2.ico')
def change(clr):
    win.configure(background=clr)
    print(clr)
btn1=Button(win,text="RED",command=change("red"))
btn1.pack(pady=10)

btn2=Button(win,text="GREEN",command=change("green"))
btn2.pack(pady=20)

btn3=Button(win,text="BLACK",command=change("black"))
btn3.pack(pady=30)

btn4=Button(win,text="YELLOW",command=change("yellow"))
btn4.pack(pady=40)

btn5=Button(win,text="BLUE",command=change("blue"))
btn5.pack(pady=50)

win.mainloop()