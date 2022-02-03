from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import Employee_Dashboard
from connection import *
import checkmain
class Login_Tollmain:

    def submit(self):
        
        conn = connect()
        cr = conn.cursor()
        self.password=self.e2.get("1.0",'end-1c')
        self.tollid=self.e1.get("1.0",'end-1c')
        
        if self.password=='' or self.tollid=='':
            messagebox.showerror("","Kindly enter the fields")
        else:
            
            stat=f'select * from tollplaza where tollid="{self.tollid}" and password="{self.password}"'
            cr.execute(stat)
            res=cr.fetchone()
            if res==None:
                messagebox.showerror("","Login not successful",parent=self.root)
                self.root.destroy()
            else:
                messagebox.showinfo("","Login successful",parent=self.root)
                checkmain.change_loginstatus(status=True,id=self.e1.get("1.0",'end-1c'))
                self.root.destroy()
                Employee_Dashboard.emp_Dashboard(self.tollid)
        
    def __init__(self):
            self.root=Tk()
            width=650
            height=600
            screen_width=self.root.winfo_screenwidth()
            screen_height=self.root.winfo_screenheight()
            x=(screen_width/2)-(width/2)
            y=(screen_height/2)-(height/2)
            self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
            self.root.title('LogIn')
            self.root.resizable(0,0)
            self.root.iconbitmap('icons/emp_login.ico')

            self.root.configure(background='#262626')

            Label(self.root,text='Log In',font=('Helvetica',42,'bold'),bg='#262626',foreground="#F0F6FC").place(relx=0.04,rely=0.02)
    
            Label(self.root,text="Toll Plaza Id : ",font=("Helvetica",22,'bold'),bg='#262626',foreground='#58A6FF').place(relx=0.09,rely=0.24)
     
            self.canvas=Canvas(self.root,width=400,height=50,bg='#262626',borderwidth=0,highlightbackground='#262626',highlightthickness=0)
            self.canvas.place(relx=0.15,rely=0.34)
            
            self.canvas.create_line(2,25,300,25,fill='#A0BACC',tags='line')

            self.e1=Text(self.root,width=30,height=0.5,borderwidth=0,font=("Helvetica",15),background="#262626",foreground='white')
            self.e1.place(relx=0.15,rely=0.34)
            self.e1.config(insertbackground='white')

            Label(self.root,text="Password : ",font=("Helvetica",22,'bold'),bg='#262626',foreground='#58A6FF').place(relx=0.09,rely=0.48)
            self.canvas1=Canvas(self.root,width=400,height=50,bg='#262626',borderwidth=0,highlightbackground='#262626',highlightthickness=0)
            self.canvas1.place(relx=0.15,rely=0.58)
            self.canvas1.create_line(2,25,300,25,fill='#A0BACC',tags='line')

            self.e2=Text(self.root,width=30,height=0.5,borderwidth=0,bg='#262626',font=("Helvetica",15),foreground='white')
            self.e2.tag_configure("hidden", elide=1,background='white')
            self.e2.place(relx=0.15,rely=0.58)
            self.e2.config(insertbackground='white')

            self.b1=Button(self.root,text="Login",font=("Helvetica",16,'bold'),borderwidth=2,bg='#238636',
                                activebackground='#238636',activeforeground='#ffffff',foreground='#ffffff',command=self.submit)
            self.b1.place(relx=0.72,rely=0.78,relwidth=0.22,relheight=0.12)
            self.root.mainloop()

# Login_Tollmain()