from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import connection
from PIL import ImageTk,Image


class changePass:

    def changeAdminPass(self):
        self.email = self.e1.get("1.0",'end-1c')
        self.oldPass = self.e2.get("1.0",'end-1c')
        self.newPass = self.e3.get("1.0",'end-1c')
        #self.a=login.login_main.email
        #print(res)
        # print(self.password,self.email)
        conn = connection.connect()
        cr = conn.cursor()
        if self.newPass == '' and self.oldPass == '':
            showerror('','Please Enter the data',parent=self.root)
        else:
            q = 'select * from admin where email="{}" and password="{}"'.format(self.email, self.oldPass)
            cr.execute(q)
            result = cr.fetchone()
            if result == None:
                showerror('','Invalid Old Password')
            else:
                q = 'update admin set password="{}" where email="{}"'.format(self.newPass,self.email)
                cr.execute(q)
                conn.commit()
                showinfo('', 'Password Changed Successfully',parent=self.root)
                


    def __init__(self):
        self.root = Toplevel()
        width = 650
        height = 650
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        self.root.title('Change Administrator Password')
        self.root.resizable(0, 0)
        self.root.iconbitmap('icons/login_icon.ico')
        self.root.configure(background='#262626')



        Label(self.root, text='Change Password', font=('Helvetica', 42, 'bold'), bg='#262626',foreground="#F0F6FC").place(relx=0.04, rely=0.02)

        Label(self.root, text="Email : ", font=("Helvetica", 22, 'bold'), bg='#262626',
              foreground='#58A6FF').place(relx=0.09, rely=0.24)

        self.canvas = Canvas(self.root, width=400, height=50, bg='#262626', borderwidth=0,
                             highlightbackground='#262626', highlightthickness=0)
        self.canvas.place(relx=0.15, rely=0.34)

        self.canvas.create_line(2, 25, 300, 25, fill='#A0BACC', tags='line')

        self.e1 = Text(self.root, width=30, height=0.5, borderwidth=0, font=("Helvetica", 15), background="#262626",
                       foreground='white')
        self.e1.place(relx=0.15, rely=0.34)
        self.e1.config(insertbackground='white')

        Label(self.root, text="Old Password : ", font=("Helvetica", 22, 'bold'), bg='#262626', foreground='#58A6FF').place(
            relx=0.09, rely=0.44)
        self.canvas1 = Canvas(self.root, width=400, height=50, bg='#262626', borderwidth=0,
                              highlightbackground='#262626', highlightthickness=0)
        self.canvas1.place(relx=0.15, rely=0.54)
        self.canvas1.create_line(2, 25, 300, 25, fill='#A0BACC', tags='line')

        self.e2 = Text(self.root, width=30, height=0.5, borderwidth=0, bg='#262626', font=("Helvetica", 15),
                       foreground='white')
        self.e2.tag_configure("hidden", elide=1, background='white')
        self.e2.place(relx=0.15, rely=0.54)
        self.e2.config(insertbackground='white')
        Label(self.root, text="New Password : ", font=("Helvetica", 22, 'bold'), bg='#262626',
              foreground='#58A6FF').place(
            relx=0.09, rely=0.64)
        self.canvas2 = Canvas(self.root, width=400, height=50, bg='#262626', borderwidth=0,
                              highlightbackground='#262626', highlightthickness=0)
        self.canvas2.place(relx=0.15, rely=0.74)
        self.canvas2.create_line(2, 25, 300, 25, fill='#A0BACC', tags='line')

        self.e3 = Text(self.root, width=30, height=0.5, borderwidth=0, bg='#262626', font=("Helvetica", 15),
                       foreground='white')
        self.e3.tag_configure("hidden", elide=1, background='white')
        self.e3.place(relx=0.15, rely=0.74)
        self.e3.config(insertbackground='white')

        self.b1 = Button(self.root, text="Reset", font=("Helvetica", 14, 'bold'), borderwidth=2, bg='#238636',
                         activebackground='#238636', activeforeground='#ffffff', foreground='#ffffff',
                         command=self.changeAdminPass)
        self.b1.place(relx=0.72, rely=0.88, relwidth=0.2, relheight=0.1)

        back_img=ImageTk.PhotoImage(Image.open("icon1.png"))
        self.back_button=Button(self.root,image=back_img,background='#262626',activebackground='#262626'
                            ,borderwidth=2,command=self.root.destroy)

        self.back_button.place(relx=0.04,rely=0.92,relwidth=0.025,relheight=0.03)

        self.root.grab_set()
        self.root.transient()
        self.root.mainloop()

# changePass()
